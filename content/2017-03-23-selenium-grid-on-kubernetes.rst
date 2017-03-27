Selenium grid on Kubernetes
################################################################

:author: Russell Ballestrini
:slug: selenium-grid-on-kubernetes
:date: 2017-03-23 16:48
:tags: Code, DevOps
:status: published

This post continues from where we left off on 
`the Minikube guide </minikube/>`_. 
If you do not already have a Kubernetes cluster, you should read that first.

Selenium Grid allows you to build a cluster of Selenium nodes.
Today we will create a Selenium cluster with 1 hub and 4 nodes on Kubernetes.

Selenium Hub
===============

Let's launch the hub:

.. code-block:: bash

 kubectl run selenium-grid --image selenium/hub --port 4444

.. code-block:: bash

 kubectl get pods

For fun and learning, we may use `kubectl` exec for container introspection:

.. code-block:: bash

 kubectl exec selenium-grid-3216163580-7pqtx -- ps aux

As you can see we have a `java` process running

.. code-block:: bash

 kubectl exec selenium-grid-3216163580-7pqtx -- ps aux
 USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
 seluser      1  0.0  0.1  18044  2688 ?        Ss   17:20   0:00 /bin/bash /opt/bin/entry_point.sh
 seluser      7  0.1  3.1 2928868 64864 ?       Sl   17:20   0:13 java -jar /opt/selenium/selenium-server-standalone.jar -role hub -hubConfig /opt/selenium/config.json
 seluser     87  0.0  0.1  34424  2856 ?        Rs   20:54   0:00 ps aux 

We may also look at the config file and test the service internally:

.. code-block:: bash

 # inspect the selenium config file.
 kubectl exec selenium-grid-3216163580-7pqtx -- cat /opt/selenium/config.json

 # see if selenium is really listening on port 4444.
 kubectl exec selenium-grid-3216163580-7pqtx -- wget 127.0.0.1:4444 -O -

To access the `deployment` externally, we need to expose it:

.. code-block:: bash

 kubectl get services
 kubectl expose deployment selenium-grid --type=NodePort
 kubectl get services

My deployment was exposed here:

.. code-block:: bash

 http://192.168.99.100:31136/grid/console

To find out where your deployment was exposed:

.. code-block:: bash

 minikube service selenium-grid --url

You may open this URI in a web browser.


Selenium Node
==============

Lets spin up a Selenium Chrome node:

.. code-block:: bash

 kubectl run selenium-node-chrome --image selenium/node-chrome #--replicas=2

Now lets look at the `pods` to see what is running:

.. code-block:: bash

 kubectl get pods
 NAME                                    READY     STATUS             RESTARTS   AGE
 selenium-grid-3216163580-7pqtx          1/1       Running            1          3d
 selenium-node-chrome-4019562870-mcpfg   0/1       CrashLoopBackOff   6          6m

Eek, `CrashLoopBackOff`, that doesn't sound good.

To troubleshoot, use the following commands: 

.. code-block:: bash

 kubectl describe pod selenium-node-chrome

This command lets us review the Kubernetes level logs.

Everything looks correct so lets look at the Docker level logs:

.. code-block:: bash
 
 kubectl logs selenium-node-chrome-4019562870-mcpfg
 Not linked with a running Hub container

Ok, the error `Not linked with a running Hub container` looks like a Selenium Node error message.

Docker has a `--link` flag to link containers together, Kubernetes doesn't have this.
After some research, it seems `--link` manages ENV vars.

You can see the environment vars of a `pod` using this command:

.. code-block:: bash

 kubectl exec selenium-grid-3216163580-7pqtx -- printenv

The `selinum-node-chrome` docker image expects some ENV vars and if it doesn't get them, it goes into a crash loop.

I reached out over IRC in the #Kubernetes and #Selenium channels to ask about the ENV vars needed.
A really helpful user named `smccarthy` linked me to this:

 https://github.com/kubernetes/kubernetes/tree/master/examples/selenium

Apparently one of the example Kubernetes clusters is a Selenium Grid setup!

Looking over the example, I found the ENV vars that the selenium-node containers expect:

 * HUB_PORT_4444_TCP_ADDR
 * HUB_PORT_4444_TCP_PORT

Man, why would they put the port (4444) in the key?

Anyways, we pass these key/values when creating the container like this:

.. code-block:: bash

 kubectl run selenium-node-chrome --image selenium/node-chrome --env="HUB_PORT_4444_TCP_ADDR=selenium-grid" --env="HUB_PORT_4444_TCP_PORT=4444"

Kubernetes will use service discovery to resolve selenium-grid to the service (pods) running the hub!

If you refresh the hub browser window, you should see a connected Chrome Node, like this:

.. image:: /uploads/2017/selenium-grid-on-kubernetes.png
   :width: 500

Now we can scale up and down the cluster using this command:

.. code-block:: bash

 kubectl get pods
 NAME                                    READY     STATUS    RESTARTS   AGE
 selenium-grid-3216163580-7pqtx          1/1       Running   1          4d
 selenium-node-chrome-3809274356-tjj18   1/1       Running   0          49m
 
.. code-block:: bash

 kubectl scale deployment selenium-node-chrome --replicas=4
 deployment "selenium-node-chrome" scaled
 
.. code-block:: bash

 kubectl get pods
 NAME                                    READY     STATUS              RESTARTS   AGE
 selenium-grid-3216163580-7pqtx          1/1       Running             1          4d
 selenium-node-chrome-3809274356-1fdr5   0/1       ContainerCreating   0          2s
 selenium-node-chrome-3809274356-g0gjg   0/1       ContainerCreating   0          2s
 selenium-node-chrome-3809274356-m0b1t   1/1       Running             0          2s
 selenium-node-chrome-3809274356-tjj18   1/1       Running             0          1h

If you referesh the hub browser window, you should see 4 connected Chrome nodes!

.. image:: /uploads/2017/selenium-grid-on-kubernetes-scaled.png
   :width: 500
