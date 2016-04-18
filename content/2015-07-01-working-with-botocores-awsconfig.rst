Working with botocore's ~/.aws/config
#####################################
:date: 2015-07-01 18:14
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: working-with-botocores-awsconfig
:status: published

I ran into a `bug <https://github.com/boto/botocore/issues/435>`__ in
botocore and this post will serve to document a work around as well as
show how to use botocore session object to work with the values stored
in ~/.aws/config.

Pretend you have an aws config with two accounts for two separate
projects, like so:

\*~/.aws/config:\*

::

    [profile project1]
    account_id = 111111111111
    aws_access_key_id=THISISNOTMYACCESSKEY1
    aws_secret_access_key=THISISNOTMYSECRETKEY1
    # Optional, to define default region for this profile.
    region=us-west-1

    [profile project2]
    account_id = 222222222222
    aws_access_key_id=THISISNOTMYACCESSKEY2
    aws_secret_access_key=THISISNOTMYSECRETKEY2
    # Optional, to define default region for this profile.
    region=us-west-2

.. raw:: html

   </p>

Now instead of using a single object, we create multiple objects, one
for each profile we intend to use.

::

    >>> import botocore.session
    >>> session1 = botocore.session.get_session()
    >>> session2 = botocore.session.get_session()
    >>> session1.profile = 'project1'
    >>> session2.profile = 'project2'
    >>> session1.get_credentials().access_key
    'THISISNOTMYACCESSKEY1'
    >>> session2.get_credentials().access_key
    'THISISNOTMYACCESSKEY2'

.. raw:: html

   </p>

Also figured out how to get at the \`account\_id\` integer:

::

    >>> session1.get_scoped_config()['account_id']
    '111111111111'

.. raw:: html

   </p>

Here is another algorithm that returns a list of sessions objects, one
for each profile listed in the config.

::

    >>> import botocore.session
    >>> sessions = []
    >>> aws_config = botocore.session.get_session().full_config
    >>> for profile_name in aws_config['profiles']:
    ...     session = botocore.session.get_session()
    ...     session.profile = profile_name
    ...     sessions.append(session)

.. raw:: html

   </p>
