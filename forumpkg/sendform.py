#!/usr/bin/env python
# -*- coding:utf-8 -*-

def rend(tmpr, userinfo, prnt_id):
   return tmpr.MkPageFromFile("templates/inner_templates/send_msg.xml", {'user_id' : str( userinfo.usr_id), 'prnt' : str(prnt_id)} )

def send(db, cookies, text):
   pass
