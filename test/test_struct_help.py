#coding:utf-8
'''
Created on 2014-12-10

@author: harryhu
'''
from ctr_json.json_help import json_help
from ctr_pack_unpack.struct_help import package_help

class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

class car:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        
if __name__ == '__main__':
    #json
    c_json = json_help()
    c_person = person(25, ' 胡耀')
    c_json.add(5, c_person)
    #pack_unpack
    #json_encode
    str_json_buffer = c_json.json_encode()
    print str_json_buffer
    #set package
    c_struct = package_help()
    c_struct.set_json_buffer(str_json_buffer)
    #pack
    byte_package_body = c_struct.struct_pack()
    #add pack
    byte_package_body = c_struct.add_json_buffer(str_json_buffer)
    #add car
    c_json1 = json_help()
    c_car = car(25000, ' 宝马')
    c_json1.add(5, c_car)
    str_json_buffer_car = c_json1.json_encode()
    byte_package_body = c_struct.add_json_buffer(str_json_buffer_car)
    '''
    transport here
    '''
    #unpack
    json_list, byte_package_body = c_struct.struct_unpack_try(byte_package_body)
    for item in json_list:
        print item,type(item)
    #print c_json.json_decode(str_json_buffer)
    pass