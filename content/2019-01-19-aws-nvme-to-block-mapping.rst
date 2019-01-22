AWS nvme to block mapping
################################################################

:author: Russell Ballestrini
:slug: aws-nvme-to-block-mapping
:date: 2019-01-19 14:50
:tags: Code, DevOps
:status: published

Recently at work I transitioned our fleet from Ubuntu 14.04 LTS to Ubuntu 18.04 LTS. During the process I noticed an issue with our newer generation AWS EC2 "nitro" based instance types (specifically ``c5.2xlarge``).

AWS was presenting my ``root`` block device as ``/dev/nvme1n1`` and my ``data`` device as ``/dev/nvme0n1``. For obvious reasons, this seemingly random and out-of-order assignment breaks my provisioning scripts.

After much research and deep thought, I came up with a solid solution.

I found a barely documented tool called ``ebsnvme-id`` on the official Amazon Linux AMI and wrote a wrapper (``nvme-to-block-mapping``) to iterate over all possible combinations of ``/dev/nvme[0-26]n1`` to create a symlink to the block mapping selected when we launch the EC2 instance.

Since we have control over the block mapping, we end up with consistent and known symlink which we may confidently pass to our provisioning scripts when the time comes to partition, format, and use the block devices.

To save you time, I have added these scripts to this blog post!

**Please consider** `donating here <https://www.paypal.me/russellbal/5>`_ **if my work has helped you!**

Place the following two scripts into your AMI under ``/usr/sbin/`` and trigger the wrapper just once prior to using the devices (don't worry the wrapper script is idempotent, running it more than once won't break anything).

.. raw:: html

 <iframe width="560" height="315" src="https://www.youtube.com/embed/_OYInsj7SYw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


nvme-to-block-mapping
=========================

`/usr/sbin/nvme-to-block-mapping </uploads/2019/nvme-to-block-mapping>`_ (click for file):

.. code-block:: bash

 #!/bin/bash

 # for details:
 # https://russell.ballestrini.net/aws-nvme-to-block-mapping/

 # this will create a symlinks like:
 #
 #     /dev/nvme1n1 -> /dev/xvdh
 #
 # these ebs block device paths are set by stacker and assumed by ansible.
 #
 # if the device is non ebs, it will use the following mapping:
 non_ebs_mapping=("/dev/sdb1" "/dev/sdc1" "/dev/sdd1" "/dev/sde1" "/dev/sdf1" "/dev/sdg1")
 
 # nvme0n1 uses ${non_ebs_mapping[0]} (the 0 index item in the array)
 #
 #     /dev/nvme0n1 -> /dev/sdb1
 #
 # nvme3n1 uses ${non_ebs_mapping[3]} (the 3 index item in the array)
 #
 #     /dev/nvme3n1 -> /dev/sde1
 #
 
 # why we only iterate from 0 to 26:
 # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html
 for i in `seq 0 26`; do
     nvme_block_device="/dev/nvme${i}n1"
 
     # skip any nvme paths which don't exist.
     if [ -e  $nvme_block_device ]; then
 
         # get ebs block mapping device path set by stacker (or base AMI).
         mapping_device=$(/usr/sbin/ebsnvme-id ${nvme_block_device} --block-dev)
 
         # if the mapping_device is empty, it isn't an EBS device so
         # we will use the non_ebs_mapping to translate the device.
         if [[ -z "$mapping_device" ]]; then
             mapping_device="${non_ebs_mapping[$i]}"
         fi
 
         # if block mapping device path does not start with /dev/ fix it.
         if [[ "$mapping_device" != /dev/* ]]; then
             mapping_device="/dev/${mapping_device}"
         fi
 
         # if the block mapping device path already exists, skip it.
         if [ -e $mapping_device ]; then
             echo "path exists: ${mapping_device}"
 
         # otherwise, create a symlink from nvme block device to mapping device.
         else
             echo "symlink created: ${nvme_block_device} to ${mapping_device}"
             ln -s $nvme_block_device $mapping_device
         fi
     fi
 done


ebsnvme-id
=================


`/usr/sbin/ebsnvme-id </uploads/2019/ebsnvme-id>`_ (click for file):

.. code-block:: python

 #!/usr/bin/env python2.7
 
 # Copyright (C) 2017 Amazon.com, Inc. or its affiliates.
 # All Rights Reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License").
 # You may not use this file except in compliance with the License.
 # A copy of the License is located at
 #
 #    http://aws.amazon.com/apache2.0/
 #
 # or in the "license" file accompanying this file. This file is
 # distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
 # OF ANY KIND, either express or implied. See the License for the
 # specific language governing permissions and limitations under the
 # License.
 #
 # Reference:
 # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvme-ebs-volumes.html
 
 """
 Usage:
 Read EBS device information and provide information about
 the volume.
 """
 
 import argparse
 from ctypes import *
 from fcntl import ioctl
 import sys
 
 NVME_ADMIN_IDENTIFY = 0x06
 NVME_IOCTL_ADMIN_CMD = 0xC0484E41
 AMZN_NVME_VID = 0x1D0F
 AMZN_NVME_EBS_MN = "Amazon Elastic Block Store"
 
 class nvme_admin_command(Structure):
     _pack_ = 1
     _fields_ = [("opcode", c_uint8),      # op code
                 ("flags", c_uint8),       # fused operation
                 ("cid", c_uint16),        # command id
                 ("nsid", c_uint32),       # namespace id
                 ("reserved0", c_uint64),
                 ("mptr", c_uint64),       # metadata pointer
                 ("addr", c_uint64),       # data pointer
                 ("mlen", c_uint32),       # metadata length
                 ("alen", c_uint32),       # data length
                 ("cdw10", c_uint32),
                 ("cdw11", c_uint32),
                 ("cdw12", c_uint32),
                 ("cdw13", c_uint32),
                 ("cdw14", c_uint32),
                 ("cdw15", c_uint32),
                 ("reserved1", c_uint64)]
 
 class nvme_identify_controller_amzn_vs(Structure):
     _pack_ = 1
     _fields_ = [("bdev", c_char * 32),  # block device name
                 ("reserved0", c_char * (1024 - 32))]
 
 class nvme_identify_controller_psd(Structure):
     _pack_ = 1
     _fields_ = [("mp", c_uint16),       # maximum power
                 ("reserved0", c_uint16),
                 ("enlat", c_uint32),     # entry latency
                 ("exlat", c_uint32),     # exit latency
                 ("rrt", c_uint8),       # relative read throughput
                 ("rrl", c_uint8),       # relative read latency
                 ("rwt", c_uint8),       # relative write throughput
                 ("rwl", c_uint8),       # relative write latency
                 ("reserved1", c_char * 16)]
 
 class nvme_identify_controller(Structure):
     _pack_ = 1
     _fields_ = [("vid", c_uint16),          # PCI Vendor ID
                 ("ssvid", c_uint16),        # PCI Subsystem Vendor ID
                 ("sn", c_char * 20),        # Serial Number
                 ("mn", c_char * 40),        # Module Number
                 ("fr", c_char * 8),         # Firmware Revision
                 ("rab", c_uint8),           # Recommend Arbitration Burst
                 ("ieee", c_uint8 * 3),      # IEEE OUI Identifier
                 ("mic", c_uint8),           # Multi-Interface Capabilities
                 ("mdts", c_uint8),          # Maximum Data Transfer Size
                 ("reserved0", c_uint8 * (256 - 78)),
                 ("oacs", c_uint16),         # Optional Admin Command Support
                 ("acl", c_uint8),           # Abort Command Limit
                 ("aerl", c_uint8),          # Asynchronous Event Request Limit
                 ("frmw", c_uint8),          # Firmware Updates
                 ("lpa", c_uint8),           # Log Page Attributes
                 ("elpe", c_uint8),          # Error Log Page Entries
                 ("npss", c_uint8),          # Number of Power States Support
                 ("avscc", c_uint8),         # Admin Vendor Specific Command Configuration
                 ("reserved1", c_uint8 * (512 - 265)),
                 ("sqes", c_uint8),          # Submission Queue Entry Size
                 ("cqes", c_uint8),          # Completion Queue Entry Size
                 ("reserved2", c_uint16),
                 ("nn", c_uint32),            # Number of Namespaces
                 ("oncs", c_uint16),         # Optional NVM Command Support
                 ("fuses", c_uint16),        # Fused Operation Support
                 ("fna", c_uint8),           # Format NVM Attributes
                 ("vwc", c_uint8),           # Volatile Write Cache
                 ("awun", c_uint16),         # Atomic Write Unit Normal
                 ("awupf", c_uint16),        # Atomic Write Unit Power Fail
                 ("nvscc", c_uint8),         # NVM Vendor Specific Command Configuration
                 ("reserved3", c_uint8 * (704 - 531)),
                 ("reserved4", c_uint8 * (2048 - 704)),
                 ("psd", nvme_identify_controller_psd * 32),     # Power State Descriptor
                 ("vs", nvme_identify_controller_amzn_vs)]  # Vendor Specific
 
 class ebs_nvme_device:
     def __init__(self, device):
         self.device = device
         self.ctrl_identify()
 
     def _nvme_ioctl(self, id_response, id_len):
         admin_cmd = nvme_admin_command(opcode = NVME_ADMIN_IDENTIFY,
                                        addr = id_response,
                                        alen = id_len,
                                        cdw10 = 1)
 
         with open(self.device, "rw") as nvme:
             ioctl(nvme, NVME_IOCTL_ADMIN_CMD, admin_cmd)
 
     def ctrl_identify(self):
         self.id_ctrl = nvme_identify_controller()
         self._nvme_ioctl(addressof(self.id_ctrl), sizeof(self.id_ctrl))
 
         if self.id_ctrl.vid != AMZN_NVME_VID or self.id_ctrl.mn.strip() != AMZN_NVME_EBS_MN:
             raise TypeError("[ERROR] Not an EBS device: '{0}'".format(self.device))
 
     def get_volume_id(self):
         vol = self.id_ctrl.sn
 
         if vol.startswith("vol") and vol[3] != "-":
             vol = "vol-" + vol[3:]
 
         return vol
 
     def get_block_device(self, stripped=False):
         dev = self.id_ctrl.vs.bdev
 
         if stripped and dev.startswith("/dev/"):
             dev = dev[5:]
 
         return dev
 
 if __name__ == "__main__":
     parser = argparse.ArgumentParser(description="Reads EBS information from NVMe devices.")
     parser.add_argument("device", nargs=1, help="Device to query")
 
     display = parser.add_argument_group("Display Options")
     display.add_argument("-v", "--volume", action="store_true",
             help="Return volume-id")
     display.add_argument("-b", "--block-dev", action="store_true",
             help="Return block device mapping")
     display.add_argument("-u", "--udev", action="store_true",
             help="Output data in format suitable for udev rules")
 
     if len(sys.argv) < 2:
         parser.print_help()
         sys.exit(1)
 
     args = parser.parse_args()
 
     get_all = not (args.udev or args.volume or args.block_dev)
 
     try:
         dev = ebs_nvme_device(args.device[0])
     except (IOError, TypeError) as err:
         print >> sys.stderr, err
         sys.exit(1)
 
     if get_all or args.volume:
         print "Volume ID: {0}".format(dev.get_volume_id())
     if get_all or args.block_dev or args.udev:
         print dev.get_block_device(args.udev)

.. contents::
