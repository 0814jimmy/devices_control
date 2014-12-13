#coding:utf-8
'''
Created on 2014-12-11

@author: harryhu
'''

from base_protocol import base_protocol_request
from ctr_common.protocol_type import enum_machine_type, enum_protocol_type, enum_client_type

class heart_beat_protocol_request(base_protocol_request):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.machine_type = enum_machine_type.pc
        self.protocol_type = enum_protocol_type.heart_beat_request
        self.client_type = enum_client_type.device_client
        self.protocol_reverse = 'heart_beat_protocol_request'
        