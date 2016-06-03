Change default gateway on all SmartOS Zones and KVM guests
##########################################################
:date: 2015-06-01 20:34
:author: Russell Ballestrini
:tags: Uncategorized
:slug: change-default-gateway-on-all-smartos-zones-and-kvm-guests
:status: published
:summary:

Today I needed to change the default gateway on every Zone and KVM guest
on my SmartOS hypervisor because I switched my ISP and as a result my
gateway changed from 192.168.1.254 to 192.168.1.1. After changing one
guest I got lazy and put together this script.

**update-all-gateways.sh**

::

    for VM in `vmadm list -p -o alias,uuid`

      do
        # create an array called VM_PARTS splitting on ':'
        IFS=':' VM_PARTS=($VM)

        # create some helper varibles for alias and uuid
        alias=${VM_PARTS[0]}
        uuid=${VM_PARTS[1]}

        mac=`vmadm get $uuid | json nics | json -a mac`

        echo "
    {
       \"update_nics\": [
          {
            \"mac\": \"$mac\",
            \"gateway\": \"192.168.1.1\"
          }
       ]
    }
    " | vmadm update $uuid
    done

.. raw:: html

   </p>

::

    [root@hypervisor /opt/setup-jsons/updates]# bash update-all-gateways.sh 
    Successfully updated VM 211b992b-a448-40b4-94c9-xxxxxxxxxxxx
    Successfully updated VM 31baa6a5-aa98-4750-80df-xxxxxxxxxxxx
    Successfully updated VM 65d176b4-c36d-4cbf-b6ed-xxxxxxxxxxxx
    Successfully updated VM aa0f603c-9572-4cb0-b96f-xxxxxxxxxxxx
    Successfully updated VM ad928301-f3e1-4fe8-a1c1-xxxxxxxxxxxx
    Successfully updated VM b82a257e-5628-46db-aee4-xxxxxxxxxxxx
    Successfully updated VM da72b638-51de-4d7d-9853-xxxxxxxxxxxx
    Successfully updated VM ee42bf30-51ce-4ae2-915b-xxxxxxxxxxxx

You are welcome!

Also to change the global zone (head node) default gateway, edit
/usbkey/config and then run the following commands:

::

    [root@hypervisor /]# route delete default 192.168.1.254
    delete net default: gateway 192.168.1.254

    [root@hypervisor /]# route add default 192.168.1.1
    add net default: gateway 192.168.1.1

    [root@hypervisor /]# netstat -r
