#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sha

def TryRegister(db, form):
   if 'ngender' not in form:
      return -3
   data = db.Run("select * from users where name = '" + str(form.getfirst('nlogin', 'empty')) + "'")
   if len(data) > 0:
      return -1

   data = db.Run("select * from users where email = '" + str(form.getfirst('nemail', 'empty')) + "'")
   if len(data) > 0:
      return -2

   sql = "INSERT INTO  users (users_id ,name ,passwdhash ,tmphash, email, avatar, fk_gndr_id ,fk_usr_st_id ,fk_cntr_id)\
   VALUES (NULL ,  '" + form.getfirst('nlogin', 'empty') + "',  '" + str(sha.new(str(form.getfirst('npasswd', 'empty'))).hexdigest()) + "' ,\
   '',  '" + form.getfirst('nemail', 'empty') + "', NULL ,  '" + str(form.getfirst('ngender', 'empty')) + "',  '1', NULL);"
   db.Run(sql)
   return 1
