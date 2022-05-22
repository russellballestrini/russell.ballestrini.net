Ubuntu 22.04 Letsencrypt Docker Hints
################################################################

:author: Russell Ballestrini
:slug: ubuntu-22-04-letsencrypt-docker-hints
:date: 2022-05-20 20:10
:tags: Code, DevOps
:status: published

letsencrypt certbot is now installable via snap (the deb apt repository is no longer maintained).

alternatively you can use certbot via docker if you plan to use the ``certonly`` mode.

I did run into some issues & I will document my workarounds here:

.. code-block:: bash

  domains=(
      example.com
      shop.example.com
  )
 
  for domain in ${domains[*]}; do
      echo "certifying: $domain"
  
      IFS='.' read -r -a domain_parts <<< "$domain"
  
      domain_parts_length=${#domain_parts[@]}
  
      if [ "$domain_parts_length" -eq 2 ]
      then
          # https://eff-certbot.readthedocs.io/en/stable/install.html#running-with-docker
          docker run -it --rm --name certbot \
              -v "/etc/letsencrypt:/etc/letsencrypt" \
              -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
              -v "/var/log/letsencrypt:/var/log/letsencrypt" \
              -v "/www:/www" \
              certbot/certbot certonly -v --renew-by-default --webroot -w /www -d $domain -d www.$domain
      else
          # https://eff-certbot.readthedocs.io/en/stable/install.html#running-with-docker
          docker run -it --rm --name certbot \
              -v "/etc/letsencrypt:/etc/letsencrypt" \
              -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
              -v "/var/log/letsencrypt:/var/log/letsencrypt" \
              -v "/www:/www" \
              certbot/certbot certonly -v --renew-by-default --webroot -w /www -d $domain
      fi
  
      # copy certificate links to a known file path and extention.
      cp /etc/letsencrypt/live/$domain/fullchain.pem /etc/letsencrypt/live/$domain/crt.crt
      cp /etc/letsencrypt/live/$domain/privkey.pem /etc/letsencrypt/live/$domain/key.key
  done

  # use minionfs to stage all certificates onto the salt master.
  salt-call cp.push_dir "/etc/letsencrypt/live/" glob='*.crt'
  salt-call cp.push_dir "/etc/letsencrypt/live/" glob='*.key

So the key is the ``-v`` mounts, I needed one for my ``webroot`` of ``/www`` & one for logs.

This is different or not assumed in the official guide notes.


Additionally on Ubuntu 22.04 LTS in Linode, I was not any to use the ``-v`` mounts until I ran these commands:
  
.. code-block:: bash

  sudo su - root

  mkdir /sys/fs/cgroup/systemd
  mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd

The mount command never persists across reboots so you will want the following ``/etc/fstab`` entry:

Brian Amedro ended up modifying grub to avoid loading the certain systemd subsystem which were found to cause us the trouble:

https://github.com/docker/for-linux/issues/219#issuecomment-817318014

For now i will place the ``mkdir`` & ``mount`` commands into the renew script since the fstab solution doesn't work

because the directory doesn't exist, gets deleted on each reboot so it isn't present during boot mount time.

/etc/fstab

.. code-block:: bash

  cgroup    /sys/fs/cgroup/systemd    cgroup    defaults
