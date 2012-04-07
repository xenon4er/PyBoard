#!/usr/bin/env python

class Templater:
    
    def __init__(self):
        pass
    
    def MkPageFromFile(self,filename,dict):
        lines = open(filename).readlines()
   
        tmp = ''
   
        for x in lines:
            tmp +=x
   
        return self.MkPage( tmp , dict)
    
    def MkPage(self,template,dict):
        res = template#fix this
                
        for k, v in dict.iteritems():
            res = res.replace('{$' + k + '}', v)
        
        return res