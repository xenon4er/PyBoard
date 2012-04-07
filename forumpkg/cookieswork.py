#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import os

import cgi

import cgitb

import Cookie


def ReadCookies(cookie):
   cookie_string = os.environ.get('HTTP_COOKIE')
   lastvisit = 'Welcome! (First visit or cookies disabled)'
   if cookie_string:
      cookie.load(cookie_string)
      if cookie['lastvisit'] != None :
         lasttime = float(cookie['lastvisit'].value)
         lastvisit = 'Last visit:' + str( time.asctime(time.localtime(lasttime)) )
   res = {}
   res ['lastvisit'] = lastvisit
   return res
