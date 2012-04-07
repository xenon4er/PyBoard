#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import sha

def trylogin(cookies, db, login, passwd):
   sql = "select passwdhash, users_id from users where users_name = " + login
   data = db.Run(sql)
   if len(data) == 0:
      return -1

   if data[0][0] != passwd:
      return -2
   tmphash = sha.new(repr(time.time())).hexdigest()
   sql = "update users set tmphash = " + str(tmphash)
   db.Run(sql)
   cookie['passwd'] = tmphash
   cookie['userid'] = str(data[0][1])
   return 1

