#coding:utf-8
'''
Created on 2014-12-11

@author: harryhu
'''

from ctr_common.protocol_type import enum_protocol_type

class base_protocol_request(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.protocol_type = enum_protocol_type.base_protocol_request
        self.client_id = ""

class base_protocol_response(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.protocol_type = enum_protocol_type.base_protocol_response
        self.request_result = ""