#!/usr/bin/env python
# -*- coding:utf-8 -*-

#-----------imports------------
import time

import os

import cgi

import cgitb

import Cookie

import forumpkg.templater as templater

import forumpkg.login as logon

import forumpkg.sendform as sendform

import forumpkg.registration as reg

from forumpkg.Exceptions.PyBoardException import *

from forumpkg.Exceptions.DBConnectException import *

from forumpkg.sectionrender import *

from forumpkg.cookieswork import *

tmpr = templater.Templater()#mk templater

#----------- end imports------------

#-----------defs--------------------

def GetSettings(db):#explode settings from db
   res = {}
   data = db.Run("select  st_key, text from settings")
   for x in data:
      res[x[0]] = x[1]

   return res
   
   

#-----------defs--------------------

try:#main 

   import config as conf#try to import config file

   import forumpkg.mysqlwork as mysql
   try:#try connect to db
      db = mysql.MySQLWork(host=conf.conf['dbhost'], user=conf.conf['dbuser'], passwd=conf.conf['dbpassword'], db=conf.conf['dbname'])
   except:
      raise DBConnectException()
      
   settings = GetSettings(db)

   cookie = Cookie.SimpleCookie()#create cookie object
   cookiesinfo = ReadCookies(cookie, db)#reading cookies


   #mk template dict
   tmpdict = {'title' : '', 'content' : '', 'server_time' : str(time.asctime(time.localtime())), 'lastvisit' : cookiesinfo['lastvisit'] + '</br> queryes used: ' + str(db.CountOfQuery()), 'userinfo' : 'Some string :) ' }
   

   tmpdict['title'] = settings['ForumName'] #default title
   
   if cookiesinfo['userinfo'].guest:#Indentefy user
      tmpdict['userinfo'] = 'You are guest</br>' + tmpr.MkPageFromFile("templates/inner_templates/login.xml", {})
   else:
      tmpdict['userinfo'] = 'Hello, ' + cookiesinfo['userinfo'].__str__() + '</br><a href = index.py?action=exit><i>Exit</i><a/>'

   #working with GET & POST
   form = cgi.FieldStorage() # instantiate only once!
   action = form.getfirst('action', settings['defaultaction'])

   #work with current action

   if action == 'showsection':#show secitons
      numberofsec = form.getfirst('value', 'empty')
      if numberofsec != 'empty':
         tmpdict['content'] = rendersections(conf.conf,db,tmpr,int(numberofsec))
      else:
         tmpdict['content'] = rendersections(conf.conf,db,tmpr)      

   elif action == 'login':#try to login
      usr_login = form.getfirst('login', 'empty')
      usr_passwd = form.getfirst('passwd', 'empty')
      usr_id = logon.trylogin(cookie, db, usr_login, usr_passwd)
      if usr_id == -1:
         tmpdict['userinfo'] = 'User not exist</br>' + tmpr.MkPageFromFile("templates/inner_templates/login.xml", {})
      if usr_id == -2:
         tmpdict['userinfo'] = 'Wrong password</br>' + tmpr.MkPageFromFile("templates/inner_templates/login.xml", {})
      if usr_id == 1:
         print 'location: index.py'

   elif action == 'exit':#logout
      cookie['userid'] = '0'
      cookie['passwd'] = '0'
      print cookie
      print 'location: index.py'

   elif action == 'registration':# try to register
      statusline = ''#status line for forms
      #if 'nlogin' not in form:
      genderline = ''#gender text
      data = db.Run("select * from genders")
      for x in data:
         genderline += '<input type="radio" name="ngender" value="' + str(x[0]) + '" />' + x[1] + '</br>'

      if 'nlogin' in form:#try to register
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


      tmpdict['content'] = tmpr.MkPageFromFile("templates/inner_templates/registration.xml", {'statusline' : statusline, 'text' : '', 'gender' : genderline})
         
   elif action == 'showmessage':#show messages
      numberofsec = form.getfirst('value', 'empty')
      if numberofsec != 'empty':
         tmpdict['content'] = rendermssgs(conf.conf,db,tmpr,int(numberofsec))         
      if not cookiesinfo['userinfo'].guest:
         tmpdict['content'] += sendform.rend(tmpr, db, cookiesinfo['userinfo'], numberofsec)

   elif action == 'sendmsg':#send messages
      sendform.send(db, cookie, form)
      print 'location: index.py?action=showmessage&value=' + form.getfirst('prnt', 'empty')

   elif action == 'newtheme':#form for create new theme
      numberofsec = form.getfirst('value', 'empty')
      tmpdict['content'] += sendform.newtheme(tmpr, db, cookiesinfo['userinfo'], numberofsec)

   elif action == 'mktheme':#try create new theme
      sendform.mktheme(db, cookie, form)
      print 'location: index.py?action=showsection' + form.getfirst('sct', '')


   # The SimpleCookie instance is a mapping
   cookie['lastvisit'] = str(time.time())# refresh last visit

   # Output the HTTP message containing the cookie
   print cookie#send cookie
   
   print "Content-Type: text/html"#send headers
   print   
      
#   tmpdict = {'title' : title, 'content' : content, 'server_time' : str(time.asctime(time.localtime())), 'lastvisit' : cookiesinfo['lastvisit'] + '</br> queryes used: ' + str(db.CountOfQuery()), 'userinfo' : userinfo }

   print tmpr.MkPageFromFile("templates/simpletemplate/tmp.xml", tmpdict)#send main template
   

except PyBoardException, e:#pyboard exception
   print "Content-Type: text/html"
   print   
   print tmpr.MkPageFromFile("templates/error/errmsg.xml", {'errmsg' : e.message, 'errtxt' : e.text})

except:#others exceptions
   
   if conf.conf['debug']:
      cgitb.handler()
   else:
      print '''\
            Something Wrong. Sorry
      '''
