Build RPM or DEB packages for Node.js using Jenkins and FPM
#############################################################

:author: Russell Ballestrini
:slug: rpm-deb-packages-for-nodejs-using-jenkins-and-fpm
:date: 2016-11-24 15:30
:tags: Code, DevOps
:status: published

This blog post assumes you already have:

* a Jenkins master and none or many build servers
* FPM installed on the build servers
* Node.js installed on the build servers

I add *jenkins-build.sh* in the root of the Node.js code repo:

.. code-block:: bash

 # example usage: JOB_NAME=example-api BUILD_NUMBER=101 bash jenkins-build.sh

 # download and build nodejs application and 3rd party modules.
 npm rebuild
 npm install -l

 version=$(cat package.json | python -c 'import sys, json; print json.load(sys.stdin)["version"]')

 # change directory down below checkout directory
 cd ..

 # create an RPM using fpm.
 #   JOB_NAME     = jenkins job name
 #   BUILD_NUMBER = jenkins auto incremented build number
 /usr/local/bin/fpm \
     -s dir -t rpm \
     --name "$JOB_NAME" \
     --iteration "$BUILD_NUMBER" \
     --version "$version" \
     --vendor "Example, Inc" \
     --rpm-user="node"  --deb-user="node" \
     --rpm-group="node" --deb-group="node" \
     --directories "/opt/$JOB_NAME" \
     "$JOB_NAME/$JOB_NAME.service=/lib/systemd/system/" \
     "$JOB_NAME=/opt/"

 # make a copy of the rpm with generic name (without version or build).
 cp *.rpm "$JOB_NAME.rpm"

 # mv both the rpm and genericly named rpm to the workdir so jenkins can archive it.
 mv *.rpm "$JOB_NAME"
 
Then in the Jenkins job, I have the following `execute shell` tasks:

.. code-block:: bash

 # clean out old rpms.
 rm -f *.rpm
 
 # download all 3rd party Node.js modules and package into an installable RPM.
 bash jenkins-build.sh
 
I then simply upload the rpm to an S3 repo which is accessible to my API hosts.

The same basic strategy may be used for other languages with subtle differences to the build script.
