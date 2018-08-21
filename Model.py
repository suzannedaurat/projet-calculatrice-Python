#!/usr/bin/env python
# -*- coding: utf-8 -*$

from Tkinter import *
from math import *

class Model:

    @staticmethod
    def calculate(number, val):
        data = val.get()
        result = eval(data) #need to find a way to avoid using eval()
        val.set(result)

    @staticmethod
    def clear(val):
        global task
        task = 0
        val.set(task)
        
