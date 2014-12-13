#coding:utf-8
'''
Created on 2014-12-11

@author: harryhu
'''

class enum_machine_type(object):
    pc = "pc"
    tv = "tv"

class enum_protocol_type(object):
    base_protocol_request = "base_protocol_request"
    base_protocol_response = "base_protocol_response"
    
    register_request = "register_request"
    register_response = "register_response"
    
    heart_beat_request = "heart_beat_request"
    
    

class enum_client_type(object):
    device_client = "device_client"
    ctr_client = "control_client"
    
class client(object):
    def __init__(self):
        self.twisted_protocol = None
        self.ip = ""
        self.port = 0
        self.client_id = None#唯一标识
        self.client_type = None#device,control
        self.machine_type = None#pc,tv


class task(object):
    def __init__(self):
        self.task_id = 0
        self.client_id = None
        self.command = ""
        self.param = ""