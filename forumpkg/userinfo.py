#!/usr/bin/env python
# -*- coding:utf-8 -*-

class User:
   def __init__(self, usr_id, db=None):
      self.guest = True
      self.usr_id = usr_id
      self.usr_name = '<Guest>'
      self.email = None

      if usr_id != None:
         self.guest = False
         sql = "select name from users where users_id = " + str(usr_id)
         data = db.Run(sql)
         self.name = data[0][0]
         
         
