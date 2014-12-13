#coding:utf-8
'''
Created on 2014-12-10

@author: harryhu
'''
import json

class json_help(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.json_map = {}
        self.json_str = ""
        self.json_dump = None
        pass
    
    def add(self, key, value):
        json_map = {}
        json_map[key] = value
        return json_map
    def add_self(self, key, value):
        self.json_map[key] = value
        return self.json_map
        
    def delete(self, key):
        if self.json_map.has_key(key):
            print "delete", key, self.json_map.pop(key)
    
    def clear_map(self):
        self.json_map.clear()
        
    def object2dict(self, obj):
        #convert object to a dict
        dictMap = {}
        dictMap['__class__'] = obj.__class__.__name__
        dictMap['__module__'] = obj.__module__
        dictMap.update(obj.__dict__)
        return dictMap
 
    def dict2object(self, dictMap):
        #convert dict to object
        if '__class__' in dictMap:
            class_name = dictMap.pop('__class__')
            module_name = dictMap.pop('__module__')
            #module = __import__(module_name)
            #class_ = getattr(module,class_name)
            args = dict((key.encode('utf-8'), value) for key, value in dictMap.items()) #get args
            #inst = class_(**args) #create new instance
            args['__class__'] = class_name
            args['__module__'] = module_name
            inst = args
        else:
            inst = dictMap  
        return inst
    
    def json_encode(self, json_map):
        #self.json_str = json.dumps(self.json_map, sort_keys=True, ensure_ascii=False, encoding='utf-8', default = self.object2dict)
        json_str = json.dumps(json_map, sort_keys=True, ensure_ascii=False, encoding='utf-8', default = self.object2dict)
        return json_str
    def json_encode_self(self):
        #self.json_str = json.dumps(self.json_map, sort_keys=True, ensure_ascii=False, encoding='utf-8', default = self.object2dict)
        self.json_str = json.dumps(self.json_map, sort_keys=True, ensure_ascii=False, encoding='utf-8', default = self.object2dict)
        return self.json_str
    
    def json_decode(self, json_str):
        json_dump = json.loads(json_str, encoding='utf-8', object_hook = self.dict2object)
        return json_dump
        #self.json_str = json.loads(self.json_dump)
    def json_decode_self(self):
        self.json_dump = json.loads(self.json_str, encoding='utf-8', object_hook = self.dict2object)
        return self.json_dump
        #self.json_str = json.loads(self.json_dump)
        