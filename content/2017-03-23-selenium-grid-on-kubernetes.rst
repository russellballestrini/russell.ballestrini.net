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

.. contents::

Selenium Hub
===============

Let's launch the hub:

.. code-block:: bash

 kubectl get pods
 kubectl run selenium-grid --image selenium/hub:2.53.1 --port 4444
 kubectl get pods

To access the ``deployment`` externally, we need to expose it:

.. code-block:: bash

 kubectl get services
 kubectl expose deployment selenium-grid --type=NodePort
 kubectl get services

My deployment was exposed here:

.. code-block:: bash

 http://192.168.99.100:31136/grid/console

To find out where your ``deployment`` was exposed:

.. code-block:: bash

 minikube service selenium-grid --url

You may open this URI in a web browser

Selenium Hub Overlearning
--------------------------------

You can skip this section or try it for extra credit.

We may use ``kubectl`` exec for container introspection:

.. code-block:: bash

 kubectl exec selenium-grid-3216163580-7pqtx -- ps aux

As you can see we have a ``java`` process running

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
 
You can even shell into the container:

.. code-block:: bash

 kubectl exec -it elenium-grid-3216163580-7pqtx -- /bin/bash

Exit out of the container and lets setup some Selenium Nodes!



Selenium Node
==============

Lets spin up a Selenium Chrome node:

.. code-block:: bash

 kubectl get pods
 kubectl run selenium-node-chrome --image selenium/node-chrome:2.53.1 --env="HUB_PORT_4444_TCP_ADDR=selenium-grid" --env="HUB_PORT_4444_TCP_PORT=4444"
 kubectl get pods

Kubernetes will use service discovery to resolve ``selenium-grid`` to the service (pods) running the hub!

If you refresh the hub browser window, you should see a connected Chrome Node, like this:

.. image:: /uploads/2017/selenium-grid-on-kubernetes.png
   :width: 500
   
Selenium Node Overlearning
----------------------------------

You can skip this section or try it for extra credit.

The first time I tried to launch a Selenium node and I had trouble.

I ran this:

.. code-block:: bash

 kubectl get pods
 kubectl run selenium-node-chrome --image selenium/node-chrome:2.53.1
 kubectl get pods

The new ``pod`` went into status ``CrashLoopBackOff``:

.. code-block:: bash

 NAME                                    READY     STATUS             RESTARTS   AGE
 selenium-grid-3216163580-7pqtx          1/1       Running            1          3d
 selenium-node-chrome-4019562870-mcpfg   0/1       CrashLoopBackOff   6          6m

To troubleshoot, I used the following commands: 

.. code-block:: bash

 kubectl describe pod selenium-node-chrome

This command lets us review the Kubernetes level logs.
Everything looked correct so lets look at the Docker level logs:

.. code-block:: bash
 
 kubectl logs selenium-node-chrome-4019562870-mcpfg
 Not linked with a running Hub container

Ok, the error ``Not linked with a running Hub container`` looks like a Selenium Node error message.

Docker has a ``--link`` flag to link containers together, Kubernetes doesn't have this.
After some research, it seems ``--link`` manages ENV vars.

You can see the environment vars of a ``pod`` using this command:

.. code-block:: bash

 kubectl exec selenium-grid-3216163580-7pqtx -- printenv

I learned that the ``selinum-node-chrome`` docker image expects some ENV vars and if it doesn't get them, it goes into a crash loop.

I reached out over IRC in the ``#Kubernetes`` and ``#Selenium`` channels to ask about the ENV vars needed.
A really helpful user named `smccarthy` linked me to this:

 https://github.com/kubernetes/kubernetes/tree/master/examples/selenium

Apparently one of the example Kubernetes clusters is a Selenium Grid setup!

Looking over the example, I found the ENV vars that the selenium-node containers expect: ``HUB_PORT_4444_TCP_ADDR`` and ``HUB_PORT_4444_TCP_PORT``

Man, why would they put the port (4444) in the key?

Anyways, we pass these key/values when creating the container like this:

.. code-block:: bash

 kubectl run selenium-node-chrome --image selenium/node-chrome:2.53.1 --env="HUB_PORT_4444_TCP_ADDR=selenium-grid" --env="HUB_PORT_4444_TCP_PORT=4444"



Selenium Scale
==============

Now we can scale up and down the Selenium Grid cluster. Lets scale the ``deployment`` to 4 ``replica`` node-chrome ``pods``.

.. code-block:: bash

 kubectl get pods
 kubectl scale deployment selenium-node-chrome --replicas=4
 kubectl get pods

Finally, if you refresh the hub browser window, you should see 4 connected Chrome nodes!

.. image:: /uploads/2017/selenium-grid-on-kubernetes-scaled.png
   :width: 500

If you liked this post, leave me a message in the comments!

