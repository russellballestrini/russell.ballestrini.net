Prevent a certain program from running too long in bash
#######################################################
:date: 2012-06-13 09:45
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: prevent-a-certain-program-from-running-to-long-in-bash
:status: published

**Update** - I opensourced this script here: `bash kira <https://github.com/russellballestrini/bash-kira>`__

I came up this this script to kill certain programs after they run for
too long. This works like similar to a timeout. Warning this script is
pretty harsh and kills the program.

::

    #!/bin/bash
    PROGRAM=replace-with-program-name
    PIDSFILE=/tmp/kill-these.pids

    for pid in `pidof $PROGRAM`
      do
        if grep -q $pid $PIDSFILE
          then
            kill $pid
        fi
      done

    > $PIDSFILE

    for pid in `pidof $PROGRAM`
      do
        echo $pid >> $PIDSFILE
      done

Then I wrote a cronjob to kill hung programs:

::

    * * * * * /usr/local/sbin/killprogs.sh
