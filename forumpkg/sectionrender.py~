#!/usr/bin/env python
# -*- coding:utf-8 -*-

def rendermssgs(config, db, tmpr, section , prnt_id=None):
   res = ''
   return res

def rendersections(config, db, tmpr, prnt_id=None):
   res = '<h2>Sections:</h2>'
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

   return res
