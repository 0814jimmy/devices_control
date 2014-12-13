#coding:utf-8
'''
Created on 2014-12-11

@author: harryhu
'''
from base_protocol import base_protocol_request, base_protocol_response
from ctr_common.protocol_type import enum_machine_type, enum_protocol_type, enum_client_type

class register_request(base_protocol_request):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.machine_type = enum_machine_type.pc
        self.protocol_type = enum_protocol_type.register_request
        self.client_type = enum_client_type.device_client
        self.protocol_reverse = 'hello server'
        

class register_response(base_protocol_response):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.machine_type = enum_machine_type.pc
        self.protocol_type = enum_protocol_type.register_response
        self.client_type = enum_client_type.device_client
        self.protocol_reverse = 'hello client'