Filter Salt Stack Return Data Output
####################################
:date: 2014-03-13 18:21
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: filter-salt-stack-return-data-output
:status: published

Sometimes you only want to see what has changed, and that is OK.

Create a file like this:

**filter.py**

    ::

        #!/usr/bin/python

        from json import loads
        from json import dumps

        import fileinput

        stdin_lines = [line for line in fileinput.input()]

        ret = loads(''.join(stdin_lines))

        for minion_id, data in ret.items():
            print(minion_id)
            print('='*len(minion_id))
            for key, value in ret[minion_id].items():
                if value['changes'] or value['result'] == False:
                    print('')
                    print(dumps(value, indent=4))
                    print('')

Make the file executable:

    ::

        chmod 755 filter.py

Execute your remote execution like this:

    ::

        sudo salt-call --out=json state.highstate | ./filter.py

    .. raw:: html

       </p>

    ::

        sudo salt '*' --out=json  --timeout=60 --static state.highstate | ./filter.py

    .. raw:: html

       </p>

    The flags ``--timeout=60`` and ``--static`` will cause the Salt
    command to block until the specified seconds for each minion to
    return results. We then pipe the returned JSON into our
    ``filter.py`` script to filter out only the changes and failures!

Profit!

Change the conditional depending on what you want. For example, for just
failures do this:

    ::

        if value['result'] == False:

    .. raw:: html

       </p>

Example output:

    ::

        # sudo salt 'graphite.foxhop.net' --out=json --static --timeout=60 state.highstate | ./filter.py

        graphite.foxhop.net
        ===================

        {
            "comment": "File /tmp/taco updated",
            "__run_num__": 15,
            "changes": {
                "diff": "New file",
                "mode": "0640"
            },  
            "name": "/tmp/taco",
            "result": true
        }   

    .. raw:: html

       </p>
