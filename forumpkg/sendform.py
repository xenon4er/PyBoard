#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

def rend(tmpr, db, userinfo, prnt_id):
   data = db.Run('select fk_sct_id from messages where msg_id = ' + str(prnt_id) )
   return tmpr.MkPageFromFile("templates/inner_templates/send_msg.xml", {'user_id' : str( userinfo.usr_id), 'prnt' : str(prnt_id), 'sct' : str(data[0][0])} )

def newtheme(tmpr, db, userinfo, prnt_id):

   return tmpr.MkPageFromFile("templates/inner_templates/newtheme.xml", {'user_id' : str( userinfo.usr_id), 'prnt' : 'None', 'sct' : prnt_id} )


def mktheme(db, cookie, form):
   sql = "select tmphash from users where users_id = " + str(cookie['userid'].value) + ";"
   data = db.Run(sql)
   if (len(data) == 1) and ((data[0][0]) == (cookie['passwd'].value)):
      if form.getfirst('sct', 'empty') == 'None':
         sctp = 'NULL'
      else:
         sctp = form.getfirst('sct', 'empty')
         
      sql = "insert into messages (text, create_date, fk_msg_prnt_id, fk_sndr_usr_id, fk_sct_id, fk_msg_st_id )\
            values ('" + form.getfirst('text', 'empty') + "' , NOW() , NULL," + str(cookie['userid'].value) + ",  %s ,1)" % sctp
      data = db.Run(sql)

def send(db, cookie, form):
   sql = "select tmphash from users where users_id = " + str(cookie['userid'].value) + ";"
   data = db.Run(sql)
   if (len(data) == 1) and ((data[0][0]) == (cookie['passwd'].value)):
      if form.getfirst('sct', 'empty') == 'None':
         sctp = 'NULL'
      else:
         sctp = form.getfirst('sct', 'empty')
         
      sql = "insert into messages (text, create_date, fk_msg_prnt_id, fk_sndr_usr_id, fk_sct_id, fk_msg_st_id )\
            values ('" + form.getfirst('text', 'empty') + "' , NOW() , " + form.getfirst('prnt', 'empty') + "," + str(cookie['userid'].value) + ",  %s ,1)" % sctp
      data = db.Run(sql)
