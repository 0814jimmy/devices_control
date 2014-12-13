#coding:utf-8
'''
Created on 2014-12-11

@author: harryhu
'''
from twisted.internet.protocol import ClientFactory#,defer
from twisted.protocols.basic import LineReceiver

from ctr_common.protocol_help import protocol_help
from ctr_pack_unpack.struct_help import package_help
from twisted.internet import task
import sys
import time
class pc_client_protocol(LineReceiver, protocol_help):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        protocol_help.__init__(self)
        self.data_buffer = ""
        self.setRawMode()
        self.c_struct = package_help()
        #init config file
        try:
            self.client_id = sys.argv[1]
        except:
            self.client_id = time.strftime("%Y%m%d%H%M%S")
        
        self.heart_beat_task = None
        
    def connectionMade(self):
        #初始化心跳
        self.heart_beat_task = task.LoopingCall(self.heart_beat)
        #注册
        cregister_request_package = self.make_register_request_package()
        self.transport.write(self.pack_package(cregister_request_package))
        
    def connectionLost(self, reason):
        print "lost_reason",reason

    def rawDataReceived(self, data):
        #parse protocol
        self.data_buffer += data
        #这边要改成异步,再加上同步
        json_buffer_list, left_package = self.c_struct.struct_unpack_try(self.data_buffer)
        self.data_buffer = left_package
        self.protocol_do(json_buffer_list)
                
class pc_client_protocol_factory(object, ClientFactory):
    protocol = pc_client_protocol
    def __init__(self):
        pass
    
    def startedConnecting(self, connector):
        """Called when a connection has been started.

        You can call connector.stopConnecting() to stop the connection attempt.

        @param connector: a Connector object.
        """
        print "startedConnecting"

    def clientConnectionFailed(self, connector, reason):
        """Called when a connection has failed to connect.

        It may be useful to call connector.connect() - this will reconnect.

        @type reason: L{twisted.python.failure.Failure}
        """
        print "clientConnectionFailed",reason
        #reconnect
        connector.connect()
        
    def clientConnectionLost(self, connector, reason):
        """Called when an established connection is lost.

        It may be useful to call connector.connect() - this will reconnect.

        @type reason: L{twisted.python.failure.Failure}
        """
        print "clientConnectionLost",reason
        #reconnect
        connector.connect()








