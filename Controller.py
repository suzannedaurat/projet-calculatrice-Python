#!/usr/bin/env python
# -*- coding: utf-8 -*$

from Tkinter import *

task = ""
#display input
class Controller:

    @staticmethod
    def buttonClick(number, val):
        global task
        task = str(task) + str(number)
        val.set(task)
