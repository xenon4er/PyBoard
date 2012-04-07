#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi

import cgitb

import forumpkg.templater as templater

tmpr = templater.Templater()

try:

   import config as conf

   import forumpkg.mysqlwork as mysql
   try:
      db = mysql.MySQLWork(host=conf.conf['dbhost'], user=conf.conf['dbuser'], passwd=conf.conf['dbpassword'], db=conf.conf['dbname'])
   except:
      print "Content-Type: text/html"
      print   
      print tmpr.MkPageFromFile("templates/error/errmsg.xml", {'errmsg' : 'Cannot connect to MySQL.</br>Check your server or config ', 'errtxt' : ''})
      exit()
   
   print "Content-Type: text/html"
   print   
   
   form = cgi.FieldStorage() # instantiate only once!
   
   print tmpr.MkPageFromFile("templates/simpletemplate/tmp.xml", {})
   
   
except:
   
   if conf.conf['debug']:
      cgitb.handler()
   else:
      print '''\
            Something Wrong. Sorry
      '''
