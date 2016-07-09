Migrating from WordPress to Pelican
##################################################

:author: Russell Ballestrini
:slug: migrating-from-wordpress-to-pelican
:date: 2015-11-15 15:39
:tags: Code, DevOps
:status: published
:summary:
  Five hints to save time during your migration from WordPress.

Its finally happening. I'm moving this blog from WordPress to Pelican.
This task has persisted on my TODO list for over two years.

During the process of the move, I'm going to use this post to dump hints:

.. contents:: Hints:


WordPress XML to JSON
====================================

I wrote `this tool to convert Wordpress XML dumps to JSON <https://github.com/russellballestrini/wordpress-xml-to-json>`_.
The tool is opinionated and removes lots of data.


Pelican-import
====================================

A tool to convert WordPress .xml into .rst or .md files (ReStructuredText or MarkDown) is
`pelican-import <http://docs.getpelican.com/en/latest/importer.html>`_.

I suggest checking it out, even if you do not plan to use Pelican as your static site generator.

Add date to post filenames
====================================

After using `pelican-import <http://docs.getpelican.com/en/latest/importer.html>`_ I had about 150 `.rst` files and I decided to put the date in the filename, so I wrote this short bash script tool to do the renames:

.. code-block:: bash

  files=`ls *.rst`

  for file in $files:
    do
      the_date=`grep ':date:' "$file" | awk '{ print $2; }'`
      mv "$file" "$the_date-$file"
    done

Alter category to tags
====================================

category and tags have different meanings and assumptions between wordpress and pelican.  As a result I decided to change all my categories to tags using this command:

.. code-block:: bash

  sed -i'' -e 's/:category:/:tags:/g' *.rst
  
Alter attachment and image paths 
====================================

fix paths to images / uploads to remove wp-content:

.. code-block:: bash

  sed -i'' -e 's/\/wp-content//g' *.rst

