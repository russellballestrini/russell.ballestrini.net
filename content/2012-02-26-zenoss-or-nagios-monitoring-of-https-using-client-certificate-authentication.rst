Zenoss or Nagios monitoring of HTTPS using client certificate authentication
############################################################################
:date: 2012-02-26 19:21
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: zenoss-or-nagios-monitoring-of-https-using-client-certificate-authentication
:status: published

I recently needed to monitor an HTTPS API for response time and
availability. At first I planned to just use the Nagios check\_http
command.

After gathering more requirements I learned that the API was protected
by client certificate authentication. After some research I quickly
found that no solution existed to monitor HTTP protected by client
certs. I needed to write my own plugin.

This is the python plugin I came up with:
**check\_http\_client\_cert.py**

::

    #!/usr/bin/python

    """Nagios/Zenoss client cert https checker"""

    import httplib
    from optparse import OptionParser
    from time import time
    from sys import exit

    def request( hostname, port, cert_file, path ):
        """request a resource and return response object"""
        try:
            c = httplib.HTTPSConnection( hostname, port, cert_file=cert_file )
            c.request( "GET", path )
            return c.getresponse()
        except:
            return False

    if __name__ == '__main__':
        parser = OptionParser()
        parser.add_option('-H', '--hostname', dest='hostname')
        parser.add_option('-p', '--port', dest='port')
        parser.add_option('-c', '--cert_file', dest='cert_file')
        parser.add_option('-P', '--path', dest='path',
        help="Path relative to root, like /image/search")

        o, args = parser.parse_args()
        #print o
       
        start = time() 
        r = request( o.hostname, o.port, o.cert_file, o.path )
        elapse = time() - start

        if r:
            if r.status >= 200 and r.status < 400:
                print "HTTP OK:", r.status, r.reason, "|time=" + str(elapse) + "s;;;"
                exit( 0 )
            print "HTTP Critical:", r.status, r.reason
     
        exit( 2 )
