Configuration Management and the Golden Image
#############################################
:date: 2014-02-21 17:19
:author: Russell Ballestrini
:tags: DevOps, Greatest Hits, Opinion
:slug: configuration-management-and-the-golden-image
:status: published

When operations first became a thing, system administrators stood up
servers using a base image from their favourite distribution. Things
were done manually. Some administrators created their own distros, some
wrote customised shell scripts to be run once-and-only-once to provision
software and settings. This method worked, but it was slow, manual, and
the human element caused defects. Then the request came in to stand up
100 servers the exact same way.

| System admins resolved this large request by coming up with a Standard
  Operating Environment (SOE) image which would end up becoming the
  "golden image". This golden image was the source of truth, and we
  built hundreds, thousands of machines this way. All systems were the
  same, or rather started out the same, but it didn't take long for
  deviations occur.
|  (Norton Ghost, DD, ISOs)
|  http://en.wikipedia.org/wiki/Standard\_Operating\_Environment

The golden image by itself was a flawed idea. The task of creating a
golden image was difficult and required a lot of work. Not only was it
technical, but there was a lot of politics involved in what was worthy
of inclusion. We didn't want to add cruft to every machine. Also the
golden image was only updated every couple of years, so it would quickly
become outdated and it still required provisioning scripts. Systems
already in production didn't get configuration updates that were
recently added to the golden image. There had to be a better way, and
there was...

| Some novel and smart system administrators who also knew how to
  program decided that they didn't want to maintain a golden image and
  deal with all the headaches involved and opted to use the light weight
  distribution image and then build sophisticated remote execution
  software to manage and maintain each server's configuration. Later on
  they built configuration management systems on top of this remote
  execution layer and were finally able to keep each system up-to-date,
  regardless of when it was deployed. They were geniuses and everyone
  who knew anything quickly rushed to implement remote execution and
  configuration management. It was the right way to manage servers,
  until the cloud drifted in.
|  (SaltStack, Ansible, Puppet, Chef, CFEngine)

In the day of cloud computing, we needed to scale up and down servers in
seconds. A complex configuration manifest could take hours to run from
start to finish. Configuration management was too slow. Each server
needed to download, install, and configure the software stack, in
real-time. Sure we could spin up multiple machines in parallel, but it
was still slow. We started to look back at the golden age of the golden
image, when a server was built and booted in moments. How could we pair
the speed of the golden image with the flexibility of configuration
management?

| In the future could we use configuration management manifests and
  revision control to document how to build the golden image and then
  take a snapshot? Could we overlay multiple layers or dataset of images
  on top of each other? Perhaps we take a step way back and create
  golden images with a combination of a highly customizable distribution
  like Gentoo and configuration management.
|  (Joyant SmartOS zone datasets, Docker container images, Vagrant box
  files, AWS AMI, Digital Ocean Snapshots, etc)
