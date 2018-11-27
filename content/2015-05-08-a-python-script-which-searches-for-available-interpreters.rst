A Python script which searches for available interpreters
#########################################################
:date: 2015-05-08 10:34
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: a-python-script-which-searches-for-available-interpreters
:status: published
:summary:

This post describes how to write a polyglot -- in this case a script
which runs as valid Bash or Python, to search for available Python
interpreters.

The script initially runs as Bash but upon finding a first match, the
script will call itself again this time using the expected Python
interpreter in interactive mode!

And now, for the polyglot code:

::

    #!/bin/sh

    # reinvoke this script with bpython -i, ipython -i, or python -i
    # reference: https://unix.stackexchange.com/a/66242
    ''':'
    if type bpython >/dev/null 2>/dev/null; then
      exec bpython -i "$0" "$@"
    elif type ipython >/dev/null 2>/dev/null; then
      exec ipython -i "$0" "$@"
    else
      exec python -i "$0" "$@"
    fi
    '''
    from helpers import (
      base_parser,
      get_hvpc_from_args,
    )
    parser = base_parser('Interactive Python interpreter & connection to hvpc')
    args = parser.parse_args()
    hvpc = get_hvpc_from_args(args)
    print('\nYou now have access to the hvpc object, for example: hvpc.roles\n')

In this case you can see that we setup the interactive interpreter's
environment to create an hvpc (Husky VPC) object for exploration.

If you want a pure python version that doesn't use a bash/python
polygot, checkout this code I wrote:
https://github.com/russellballestrini/botoform/blob/master/botoform/plugins/repl.py
