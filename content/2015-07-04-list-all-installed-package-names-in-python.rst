List all installed package names in Python
##########################################

:date: 2015-07-04 22:15
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: list-all-installed-package-names-in-python
:status: published

.. code-block:: python

    pkgs = lambda : list(__import__('pkg_resources').working_set)

    pkg_names = lambda : [x.project_name for x in pkgs()]

    pkg_versions = lambda : [x.project_name + '==' + x.version for x in pkgs()]

.. code-block:: python

    >>> pkg_names()
    ['ansible', 'pycrypto', 'PyYAML', 'Jinja2', '...truncated...', 'virt-back', 'Werkzeug', 'xmltodict']

.. code-block:: python

    >>> pkg_versions()
    ['ansible==1.7', 'pycrypto==2.6.1', '...truncated...', 'virt-back==0.1.0', 'xmltodict==0.9.2']
