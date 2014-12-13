#coding:utf-8
'''
Created on 2014-12-10

@author: harryhu
'''
import struct

class package_help(object):
    
    def __init__(self):
        self.str_json_buffer = ""
        self.format = ""
        self.byte_buffer_length = 0
        self.byte_buffer = None
    
    def clear_all(self):
        self.str_json_buffer = ""
        self.format = ""
        self.byte_buffer_length = 0
        self.byte_buffer = None
        
    def set_json_buffer(self, str_json_buffer):
        self.str_json_buffer = str_json_buffer
        self.format = "i%ds" % len(self.str_json_buffer)
 
    def add_json_buffer(self, str_json_buffer):
        self.str_json_buffer = str_json_buffer
        self.format = "i%ds" % len(self.str_json_buffer)
        
        byte_buffer_length = struct.calcsize(self.format)
        self.byte_buffer_length += byte_buffer_length
        self.byte_buffer += struct.pack(self.format, byte_buffer_length, self.str_json_buffer)
        if len(self.byte_buffer) == self.byte_buffer_length:
            print "struct_pack success"
            return self.byte_buffer
        else:
            raise
        
    def struct_pack(self, str_json_buffer):
        str_json_buffer = str_json_buffer
        __format = "i%ds" % len(str_json_buffer)
        byte_buffer_length = struct.calcsize(__format)
        #self.format = 'i4si9s'
        byte_buffer = struct.pack(__format, byte_buffer_length, str_json_buffer)
        #
        if len(byte_buffer) == byte_buffer_length:
            return byte_buffer
        else:
            print "struct_pack fail", len(byte_buffer), byte_buffer_length
            raise
    def struct_pack_self(self):
        self.byte_buffer_length = struct.calcsize(self.format)
        #self.format = 'i4si9s'
        self.byte_buffer = struct.pack(self.format, self.byte_buffer_length, self.str_json_buffer)
        #
        if len(self.byte_buffer) == self.byte_buffer_length:
            return self.byte_buffer
        else:
            print "struct_pack fail", len(self.byte_buffer), self.byte_buffer_length
            raise
    '''
            先获取头4字节，计算包长度是不是match，如果match再调用struck_unpack
    1、多包
    2、缺省包等处理
    '''
    def struct_unpack_try(self, str_buffer_bytes):
        json_package_list = []
        try:
            while len(str_buffer_bytes) >= 4:
                (package_length,) = struct.unpack('i', str_buffer_bytes[:4])
                #buffer_length = len(str_buffer_bytes)
                if package_length <= len(str_buffer_bytes):
                    print "parse package"
                    package = str_buffer_bytes[4:package_length]
                    str_buffer_bytes = str_buffer_bytes[package_length:]
                    json_package_list.append(self.struct_unpack(package))
                else:
                    print "Pack length not enough, wait for next receive"
                    break
        except Exception, e:
            print e
            
        print 'Buffer length:', len (str_buffer_bytes)
        return json_package_list, str_buffer_bytes
            
     
    def struct_unpack(self, byte_package_body):
        str_format = "%ss" % len(byte_package_body)
        (str_json_buffer,) = struct.unpack(str_format, byte_package_body)
        return str_json_buffer

