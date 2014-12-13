#coding:utf-8
'''
Created on 2014-12-11

@author: harryhu
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(sys.argv[0])))

from pc_client_protocol import pc_client_protocol_factory
#from twisted.internet.protocol import ClientCreator
from twisted.internet import reactor

class pc_client(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def run(self):
#        c = ClientCreator(reactor, pc_client_protocol_factory())
#        c.connectTCP('localhost', 2014, 30)
        reactor.connectTCP('localhost', 2014, pc_client_protocol_factory())
        reactor.run()


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    cpc_client = pc_client()
    cpc_client.run()