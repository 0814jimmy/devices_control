#coding:utf-8
'''
Created on 2014-12-11

@author: harryhu
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(sys.argv[0])))

from twisted.internet import reactor
#from twisted.internet.epollreactor import EPollReactor
#from twisted.internet.selectreactor import SelectReactor
#from twisted.internet.protocol import Protocol,ClientFactory,defer

from server_protocol import server_protocol_factory


class server(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def run(self):
        reactor.listenTCP(2014, server_protocol_factory())
        reactor.run()


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    cserver = server()
    cserver.run()