#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi

import cgitb

import forumpkg.templater as templater

from forumpkg.Exceptions.PyBoardException import *

from forumpkg.Exceptions.DBConnectException import *

from forumpkg.sectionrender import *

tmpr = templater.Templater()

try:

   import config as conf

   import forumpkg.mysqlwork as mysql
   try:
      db = mysql.MySQLWork(host=conf.conf['dbhost'], user=conf.conf['dbuser'], passwd=conf.conf['dbpassword'], db=conf.conf['dbname'])
   except:
      raise DBConnectException()
      
   
   print "Content-Type: text/html"
   print   
   
   form = cgi.FieldStorage() # instantiate only once!
   
   data = db.Run("select text from settings  where st_key = 'ForumName'")
   title = data[0][0]#default title
   
   action = form.getfirst('action', 'empty')

   content = ''

   if action == 'showsection':
      numberofsec = form.getfirst('value', 'empty')
      if numberofsec != 'empty':
         content = rendersections(conf.conf,db,tmpr,int(numberofsec))         

   if content == '':   
      content = rendersections(conf.conf,db,tmpr)

   print tmpr.MkPageFromFile("templates/simpletemplate/tmp.xml", {'title' : title, 'content' : content})
   

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
