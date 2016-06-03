How to rescue logs and config from a failed Citrix NetScaler App Gateway
########################################################################
:date: 2012-05-11 00:05
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: how-to-rescue-logs-and-config-from-a-failed-citrix-netscaler-app-gateway
:status: published

Today our production Citrix NetScaler broke. The box wouldn't boot and
our only backup copy of the config was on the NetScaler itself.

Being the only Unix guy around I attempted to help out the admins
working the outage. I SSH'd into the development NetScaler and noticed
it runs on FreeBSD.

I suggested fetching the Hard drive and mounting it on a Linux computer.
The NetScaler has one SATA (not SAS) disk so my desktop was compatible.

I installed the disk in the Linux tower and mounted the filesystem using
the following command:

``mount --read-only --type=ufs  --test-opts ufstype=44bsd /dev/sda5 /mnt``

Once mounted I was able to SCP interesting files to a safe location.

Warning, this procedure might void your warranty. If in doubt, call
support first.
