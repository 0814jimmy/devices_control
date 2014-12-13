#coding:utf-8
'''
Created on 2014-12-11

@author: harryhu
'''

from twisted.internet.protocol import ServerFactory, defer
from twisted.protocols.basic import LineReceiver 
from ctr_pack_unpack.struct_help import package_help
from ctr_common.protocol_help import protocol_help

from ctr_common.protocol_type import client
class server_protocol(LineReceiver, protocol_help):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        protocol_help.__init__(self)
        self.setRawMode()
        self.data_buffer = ""
        self.c_struct = package_help()
        
    #overwrite
    def connectionMade(self):
        self.client_struct = client()
        self.client_struct.twisted_protocol = self
        
        pass
    
    def connectionLost(self, reason):
        print "lost_reason",reason
        self.factory.delete_client(self.client_struct)
    
    def rawDataReceived(self, data):
        #parse protocol
        self.data_buffer += data
        #这边要改成异步,再加上同步
        json_buffer_list, left_package = self.c_struct.struct_unpack_try(self.data_buffer)
        self.data_buffer = left_package
        self.protocol_do(json_buffer_list)
        #self.factory.parse_protocol_deferred.addCallback(self.protocol_do)
        #self.factory.parse_protocol_deferred.callback(json_buffer_list)
        
    def create_client(self, client_info, map_protocol):
        #加锁
        try:
            self.client_struct.ip = client_info.host
            self.client_struct.port = client_info.port
            #type tcp/udp
            self.client_struct.client_type = map_protocol["client_type"]
            self.client_struct.machine_type = map_protocol["machine_type"]
            self.client_struct.client_id = map_protocol["client_id"]
            self.factory.add_client(self.client_struct)
        except Exception, e:
            print map_protocol
            print e
            return -1
        return 0

class server_protocol_factory(object, ServerFactory):
    
    protocol = server_protocol
    def __init__(self):
        self.map_clients = {}
        self.map_task = {}
        
        self.task_deferred = defer.Deferred()
        self.parse_protocol_deferred = defer.Deferred()
        
        #self.parse_protocol_deferred.callback
    def add_client(self, client):
        if client:
            self.map_clients[client.client_id] = client
        for key,value in self.map_clients.items():
            print key,value
        pass
    
    def delete_client(self, client):
        if client and self.map_clients.has_key(client.client_id):
            self.map_clients.pop(client.client_id)
        for key,value in self.map_clients.items():
            print key,value
        pass
    
    def update_client(self, client):
        if client and self.map_clients.has_key(client.client_id):
            self.map_clients[client.client_id] = client
        else:
            raise
    
    def add_task(self, task_id, task):
        self.map_task[task_id] = task
    
    def delete_task(self, task_id):
        if self.map_task.has_key(task_id):
            self.map_task.pop(task_id)
    def update_task(self, task_id, task):
        if self.map_task.has_key(task_id):
            self.map_task[task_id] = task
        else:
            raise




