#coding:utf-8
'''
Created on 2014-12-10

@author: harryhu
'''
from ctr_json.json_help import json_help

class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

if __name__ == '__main__':
    c_json = json_help()
    c_json.add(1, 'jimmy')
    c_json.add(2, 22)
    c_json.add(3, [111,222])
    c_json.add(4, {'hello':'hi','我':'你'})
    c_json.add(5, [111,222])
    c_json.delete(5)
    c_person = person(25, ' 胡耀')
    c_json.add(5, c_person)
    json_str = c_json.json_encode()
    print json_str, type(json_str)
    DictMap = c_json.json_decode_self()
    print DictMap,type(DictMap)
    c_personBack = DictMap['5']
    chinese_word = DictMap['4']
    print c_personBack.age,c_personBack.name
    print str(DictMap['4'])
    for key,value in DictMap['4'].items():
        print key.encode("utf-8"),value.encode("utf-8")
        
    

    pass