#!/usr/bin/env python
# -*- coding:utf-8 -*-

class PyBoardException(Exception):
   def __init__(self):
      self.message = 'PyBoard Failed :('
      self.text = ''

