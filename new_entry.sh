#!/bin/bash

if [ "$1" = "" ]
  then
    echo "you need to pass a slug"
    exit
fi

THESLUG=$1
THEDATE1=`date +%Y-%m-%d`
THEDATE2=`date +"%Y-%m-%d %H:%M"`
THEFILE="content/$THEDATE1-$THESLUG.rst"

# if the entry does not exist, make a copy from template
if [ ! -f $THEFILE ];
then
    cp "template_new_entry.rst" "$THEFILE"
    sed -i "s/THEDATE/$THEDATE2/g" "$THEFILE" 
    sed -i "s/THESLUG/$THESLUG/g" "$THEFILE" 
fi

vim "$THEFILE"
