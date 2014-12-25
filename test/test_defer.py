#coding:utf-8
'''
Created on 2014-12-15

@author: harryhu
'''
import time 
from twisted.internet.defer import Deferred

def successHandle(result):
    print 'It is success:'
    time.sleep(3)
    print result

def failedHandle(reason):
    print 'Error.'

def test1():
    d = Deferred()
    # add a callback/errback pair to the chain
    d.addCallbacks(successHandle, failedHandle)
    # fire the chain with a normal result
    d.callback('Successful')

    print "Finished test1"
if __name__ == '__main__':
    
    test1()