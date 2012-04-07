#!/usr/bin/env python
# -*- coding:utf-8 -*-

def rendersections(config,db,tmpr):
   res = ''
   data = db.Run("select * from sections")
   for x in data:
      res += str(x)

   return res
