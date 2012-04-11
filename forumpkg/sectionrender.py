#!/usr/bin/env python
# -*- coding:utf-8 -*-

def rendermessage(tmpr, db, x):
   udata = db.Run("select name from users where users_id = " + str(x[3]))   
   tmp = tmpr.MkPageFromFile("templates/inner_templates/msg_tmp.xml", {'number' : str(x[0]), 'number' : str(x[0]),'text' : str(x[1]) , 'date' : str(x[2]), 'username' :  udata[0][0] })
   return tmp 

def rendermssgs(config, db, tmpr, prnt_id):
   res = ''
   sql = "select msg_id, text, create_date, fk_sndr_usr_id from messages where fk_msg_prnt_id  = " + str(prnt_id)+ " union select msg_id, text, create_date, fk_sndr_usr_id from messages where msg_id =" + str(prnt_id) + " order by 3"
   data = db.Run(sql)      

   if len(data) != 0:
      res += '<b>Themes:</b></br><table width = 100% border = 1>'
      for x in data:
         res += rendermessage(tmpr, db, x) 

      res += '</table>'
   else:
      res += '</br>No themes'


   
   return res

def rendersections(config, db, tmpr, prnt_id=None):
   if prnt_id == -1:
      prnt_id=None
   res = '<h5  align = right><a href = index.py?action=newtheme&value=' + str(prnt_id) + '>[New Theme]</a></h6>'   
   res += '<h2>Sections:</h2>'
   sql = "select sct_name, description, sct_id from sections where fk_sct_prnt_id "
   if prnt_id == None:
      sql += "is NULL"
   else:
      sql += "=" + str(prnt_id)
   data = db.Run(sql)


   if len(data) != 0:
      for x in data:
         tmp = tmpr.MkPageFromFile("templates/inner_templates/section_tmp.xml", {'section_name' : str(x[0]), 'section_desc' : str(x[1]), 'sect_href' :  'index.py?action=showsection&value=' + str(x[2]) })
         res += tmp 
   else:
      res += 'No sections'
   

   sql = "select msg_id, text, create_date, fk_sndr_usr_id from messages where fk_msg_prnt_id is NULL and fk_sct_id "
   if prnt_id == None:
      sql += "is NULL"
   else:
      sql += "=" + str(prnt_id)
   data = db.Run(sql)   

   if len(data) != 0:
      res += '<b>Themes:</b></br><table width = 100% border = 1>'
      for x in data:
         res += rendermessage(tmpr, db, x) 
      res += '</table>'
   else:
      res += '</br>No themes'

   return res
