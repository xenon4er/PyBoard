#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import sha

def trylogin(cookie, db, login, passwd):
   sql = "select passwdhash, users_id from users where name = '" + login + "'"
   data = db.Run(sql)
   if len(data) == 0:
      return -1

   if str(data[0][0]) != str(sha.new(passwd).hexdigest()):
      return -2

   tmphash = sha.new(repr(time.time())).hexdigest()

   sql = "update users set tmphash = '" + str(tmphash) + "'"
   db.Run(sql)
   cookie['passwd'] = str(tmphash)
   cookie['userid'] = str(data[0][1])
   return 1

