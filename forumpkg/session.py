#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

class Session(object):

   def __init__(self, db, string_cookie, usr_id=None, expires=None):
      self.cookie = Cookie.SimpleCookie()
      self.cookie.load(string_cookie)

      if self.cookie.get('sid'):
         sid = self.cookie['sid'].value
         sql = "select sssn_id from sessions where sid =" + str(sid)
         data = db.Run(sql)
         if len(data) == 1:
            self.cookie.clear()
            db.Run("UPDATE sessions set last_active = " + str(time.time()))
         else:
            db.Run("INSERT into sessions (sid, fk_user_id, last_active) values (" + str(sid) +",  )")
         # Clear session cookie from other cookies
      else:
         self.cookie.clear()
         sid = sha.new(repr(time.time())).hexdigest()

      self.cookie['sid'] = sid
      
      self.set_expires(expires)

   def close(self):
      pass

   def set_expires(self, expires):
         
      self.cookie['sid']['expires'] = expires
