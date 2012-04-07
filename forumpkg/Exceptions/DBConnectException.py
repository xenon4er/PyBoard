#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyBoardException import *

class DBConnectException(PyBoardException):
   def __init__(self):
      self.message = 'Cannot connect to MySQL.</br>Check your server or config'
      self.text = ''

