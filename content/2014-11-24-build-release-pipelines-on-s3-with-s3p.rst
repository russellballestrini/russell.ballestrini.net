Build release pipelines on S3 with s3p
######################################
:date: 2014-11-24 14:39
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: build-release-pipelines-on-s3-with-s3p
:status: published

This weekend I finished my first sprint on s3p which is a Python library
and CLI application that manages release pipelines on AWS S3. I put a
lot of effort into the
`readme.rst <https://github.com/russellballestrini/s3p/blob/master/readme.rst>`__
file, so look there for usage and examples.

The main purpose of s3p is to use code to enforce process when promoting
releases in the pipeline. Another goal was to make the CLI tool dead
simple to use. As a side effect, I ended up using composition to extend
boto.s3's Key and Bucket classes to produce
`S3Release <https://github.com/russellballestrini/s3p/blob/master/s3p/release.py>`__
and
`S3Pipeline <https://github.com/russellballestrini/s3p/blob/master/s3p/pipeline.py>`__.

I plan to incorporate s3p into Teamcity build jobs. At work I would like
to use s3p to replace bash+s3cmd in pipeline management. Once s3p has a
bit more production use, I will likely sprint on it again.
