#!/usr/bin/env python
# -*- coding:utf-8 -*-

def rendersections(config,db,tmpr):
   res = ''
   data = db.Run("select sct_name, description, sct_id from sections where fk_sct_prnt_id is NULL")

   for x in data:
      tmp = tmpr.MkPageFromFile("templates/inner_templates/section_tmp.xml", {'section_name' : str(x[0]), 'section_desc' : str(x[1]), 'sect_href' :  'index.py?showsection=' + str(x[2]) })
      res += tmp

   return res
