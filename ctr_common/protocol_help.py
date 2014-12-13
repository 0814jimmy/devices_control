#coding:utf-8
'''
Created on 2014-12-13

@author: harryhu
'''

from ctr_json.json_help import json_help
from ctr_pack_unpack.struct_help import package_help
from protocol.register_protocol import register_request
from protocol.register_protocol import register_response
from protocol.heart_beat_protocol import heart_beat_protocol_request
from ctr_common.protocol_type import enum_protocol_type
import time

class protocol_help(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.c_json = json_help()
        self.c_struct = package_help()
        
    def make_register_request_package(self):
        cregister_request = register_request()
        #base_protocol
        cregister_request.client_id = self.client_id
        return cregister_request
    
    def make_register_response_package(self, register_result):
        cregister_response = register_response()
        cregister_response.request_result = register_result
        return cregister_response
    
    def make_heart_beat_request_package(self):
        cheart_beat_request = heart_beat_protocol_request()
        cheart_beat_request.client_id = self.client_id
        return cheart_beat_request

    def pack_package(self, object_class):
        byte_package_body = ""
        try:
            #self.c_json.clear_map()
            json_map = self.c_json.add("protocol_class", object_class)
            str_json_buffer = self.c_json.json_encode(json_map)
            
            #self.c_struct.clear_all()
            #self.c_struct.set_json_buffer(str_json_buffer)
            #pack
            byte_package_body = self.c_struct.struct_pack(str_json_buffer)
        except Exception, e:
            print e
        return byte_package_body
    #被复写
    def create_client(self, client_info, map_protocol):
        pass
    
    
    def heart_beat(self):
        c_heartbeat_request_package = self.make_heart_beat_request_package()
        self.transport.write(self.pack_package(c_heartbeat_request_package))

    
    def protocol_do(self, json_buffer_list):
        for json_buffer in json_buffer_list:
            try:
                json_object = self.c_json.json_decode(json_buffer)
                map_protocol = json_object['protocol_class']
                #各种协议的处理
                #1_1、server
                #注册请求协议
                if map_protocol['protocol_type'] == enum_protocol_type.register_request:
                    #1、注册
                    print map_protocol
                    client_info = self.transport.getPeer()
                    register_result = self.create_client(client_info, map_protocol)
                    #response
                    cregister_response_package = self.make_register_response_package(register_result)
                    self.transport.write(self.pack_package(cregister_response_package))

                #1_2、client
                #注册响应协议
                if map_protocol['protocol_type'] == enum_protocol_type.register_response:
                    #心跳
                    if map_protocol.has_key("request_result") and map_protocol["request_result"] == 0:
                        print "-----------start heart-----------"
                        self.heart_beat_task.start(2)
                    else:
                        #断开连接重连
                        self.transport.loseConnection()
                #心跳协议
                if map_protocol['protocol_type'] == enum_protocol_type.heart_beat_request:
                    #更新client_list
                    print map_protocol["client_id"],map_protocol['protocol_type'],time.strftime('%Y%m%d%H%M%S')
                    pass
                    
            except Exception, e:
                print json_buffer
                print e
    
        