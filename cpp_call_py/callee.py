#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Hello(s):
    print "Hello World"
    print s

def Add(a, b):
    print 'a=', a
    print 'b=', b
    return a + b

class Test:
    def __init__(self):
        print "Init"
    def SayHello(self, name):
        print "Hello,", name
        return name