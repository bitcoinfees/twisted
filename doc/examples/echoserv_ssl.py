
# Twisted, the Framework of Your Internet
# Copyright (C) 2001 Matthew W. Lefkowitz
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from OpenSSL import SSL

class ServerContextFactory:
    
    def getContext(self):
        """Create an SSL context.
        
        This is a sample implementation that loads a certificate from a file 
        called 'server.pem'."""
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        ctx.use_certificate_file('server.pem')
        ctx.use_privatekey_file('server.pem')
        return ctx


if __name__ == '__main__':
    import echoserv, sys
    from twisted.internet.protocol import Factory
    from twisted.internet.app import Application
    from twisted.internet import ssl
    from twisted.python import log
    log.startLogging(sys.stdout)
    from echoserv_ssl import ServerContextFactory
    factory = Factory()
    factory.protocol = echoserv.Echo
    app = Application("echo-ssl")
    app.listenSSL(8000, factory, ServerContextFactory())
    app.run(save=0)
