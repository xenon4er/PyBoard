#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import os

import cgi

import cgitb

import Cookie

import userinfo

def ReadCookies(cookie, db):
   cookie_string = os.environ.get('HTTP_COOKIE')
   lastvisit = 'Welcome! (First visit or cookies disabled)'
   usrinf = userinfo.User(None)
   if cookie_string:
      cookie.load(cookie_string)
      if cookie['lastvisit'] != None :
         lasttime = float(cookie['lastvisit'].value)
         lastvisit = 'Last visit:' + str( time.asctime(time.localtime(lasttime)) )
      if ('userid' in cookie ) and ('passwd' in cookie) and (cookie['userid'].value) :
         sql = "select tmphash from users where users_id = " + str(cookie['userid'].value) + ";"
         data = db.Run(sql)
         if (len(data) == 1) and ((data[0][0]) == (cookie['passwd'].value)):

            usrinf = userinfo.User(int(cookie['userid'].value), db)
   res = {}
   res ['lastvisit'] = lastvisit
   res ['userinfo'] = usrinf
   return res
