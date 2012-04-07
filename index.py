#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import os

import cgi

import cgitb

import Cookie

import forumpkg.templater as templater

from forumpkg.Exceptions.PyBoardException import *

from forumpkg.Exceptions.DBConnectException import *

from forumpkg.sectionrender import *

from forumpkg.cookieswork import *

tmpr = templater.Templater()

try:

   import config as conf

   import forumpkg.mysqlwork as mysql
   try:
      db = mysql.MySQLWork(host=conf.conf['dbhost'], user=conf.conf['dbuser'], passwd=conf.conf['dbpassword'], db=conf.conf['dbname'])
   except:
      raise DBConnectException()
      
   
   data = db.Run("select text from settings  where st_key = 'ForumName'")
   title = data[0][0]#default title
   
   cookie = Cookie.SimpleCookie()   
   cookiesinfo = ReadCookies(cookie)

   content = ''

   form = cgi.FieldStorage() # instantiate only once!
   action = form.getfirst('action', 'empty')

   if action == 'showsection':
      numberofsec = form.getfirst('value', 'empty')
      if numberofsec != 'empty':
         content = rendersections(conf.conf,db,tmpr,int(numberofsec))         

   if content == '':   
      content = rendersections(conf.conf,db,tmpr)

   # The SimpleCookie instance is a mapping
   cookie['lastvisit'] = str(time.time())

   # Output the HTTP message containing the cookie
   print cookie


   print "Content-Type: text/html"
   print   
      
   tmpdict = {'title' : title, 'content' : content, 'server_time' : str(time.asctime(time.localtime())), 'lastvisit' : cookiesinfo['lastvisit'] }

   print tmpr.MkPageFromFile("templates/simpletemplate/tmp.xml", tmpdict)
   

except PyBoardException, e:
   print "Content-Type: text/html"
   print   
   print tmpr.MkPageFromFile("templates/error/errmsg.xml", {'errmsg' : e.message, 'errtxt' : e.text})

except:
   
   if conf.conf['debug']:
      cgitb.handler()
   else:
      print '''\
            Something Wrong. Sorry
      '''
