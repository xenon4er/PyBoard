#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import os

import cgi

import cgitb

import Cookie

import hashlib

import sha

import shelve

import forumpkg.templater as templater

import forumpkg.login as logon

import forumpkg.registration as reg

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
   cookiesinfo = ReadCookies(cookie, db)

   userinfo = 'Some string :) '
   if cookiesinfo['userinfo'].guest:
      userinfo = 'You are guest</br>' + tmpr.MkPageFromFile("templates/inner_templates/login.xml", {})
   else:
      userinfo = 'Hello, ' + cookiesinfo['userinfo'].__str__() + '</br><a href = index.py?action=exit><i>Exit</i><a/>'


   content = ''

   form = cgi.FieldStorage() # instantiate only once!
   action = form.getfirst('action', 'empty')

   statusline = ''

   if action == 'showsection':
      numberofsec = form.getfirst('value', 'empty')
      if numberofsec != 'empty':
         content = rendersections(conf.conf,db,tmpr,int(numberofsec))         

   elif action == 'login':
      usr_login = form.getfirst('login', 'empty')
      usr_passwd = form.getfirst('passwd', 'empty')
      usr_id = logon.trylogin(cookie, db, usr_login, usr_passwd)
      if usr_id == -1:
         userinfo = 'User not exist</br>' + tmpr.MkPageFromFile("templates/inner_templates/login.xml", {})
      if usr_id == -2:
         userinfo = 'Wrong password</br>' + tmpr.MkPageFromFile("templates/inner_templates/login.xml", {})
      if usr_id == 1:
         print 'location: index.py'

   elif action == 'exit':
      cookie['userid'] = '0'
      cookie['passwd'] = '0'
      print cookie
      print 'location: index.py'

   elif action == 'registration':
      #if 'nlogin' not in form:
      genderline = ''
      data = db.Run("select * from genders")
      for x in data:
         genderline += '<input type="radio" name="ngender" value="' + str(x[0]) + '" />' + x[1] + '</br>'

      if 'nlogin' in form:
         regres = reg.TryRegister(db, form)
         if regres == -1:
            statusline = 'This login already exists'
         if regres == -2:
            statusline = 'This email already exists'
         if regres == -3:
            statusline = 'Choose gender!'
         if regres == -4:
            statusline = 'inner error'
         if regres == 1:
            print 'location: index.py'


      content = tmpr.MkPageFromFile("templates/inner_templates/registration.xml", {'statusline' : statusline, 'text' : '', 'gender' : genderline})
         
   elif action == 'showmessage':
      numberofsec = form.getfirst('value', 'empty')
      if numberofsec != 'empty':
         content = rendermssgs(conf.conf,db,tmpr,int(numberofsec))         

   if content == '':   
      content = rendersections(conf.conf,db,tmpr)

   # The SimpleCookie instance is a mapping
   cookie['lastvisit'] = str(time.time())

   # Output the HTTP message containing the cookie
   print cookie
   
   print "Content-Type: text/html"
   print   
      
   tmpdict = {'title' : title, 'content' : content, 'server_time' : str(time.asctime(time.localtime())), 'lastvisit' : cookiesinfo['lastvisit'] + '</br> queryes used: ' + str(db.CountOfQuery()), 'userinfo' : userinfo }

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
