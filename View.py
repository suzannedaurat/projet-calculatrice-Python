#!/usr/bin/env python
# -*- coding: utf-8 -*$

from Tkinter import *
from Controller import Controller
from Model import Model

class View(Frame):

    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)

        self.value = StringVar()
        self.entree = Entry(self, textvariable=self.value)
        self.entree.grid(columnspan=3)
        self.entree.insert(0, "0")

        self.equal_button = Button(self, text='=', bg='red',command=lambda : Model.calculate('=', self.value))
        self.equal_button.grid(row=4, column=2)

        self.plus_button = Button(self, text='+', bg='green', command=lambda:Controller.buttonClick('+', self.value))
        self.plus_button.grid(row=4, column=3)

        self.one_button = Button(self, text='1', bg='pink', fg='red', cursor='heart', command=lambda:Controller.buttonClick('1', self.value))
        self.one_button.grid(row=1, column=1)

        self.two_button = Button(self, text='2', bg='pink', fg='red', cursor='heart', command=lambda:Controller.buttonClick('2', self.value))
        self.two_button.grid(row=1, column=2)

        self.three_button = Button(self, text='3', bg='pink', fg='red', cursor='heart',command=lambda:Controller.buttonClick('3', self.value))
        self.three_button.grid(row=1, column=3)

        self.four_button = Button(self, text='4', bg='pink', fg='red', cursor='heart',command=lambda:Controller.buttonClick('4', self.value))
        self.four_button.grid(row=2, column=1)

        self.five_button = Button(self, text='5', bg='pink', fg='red', cursor='heart', command=lambda:Controller.buttonClick('5', self.value))
        self.five_button.grid(row=2, column=2)

        self.six_button = Button(self, text='6', bg='pink', fg='red', cursor='heart', command=lambda:Controller.buttonClick('6', self.value))
        self.six_button.grid(row=2, column=3)

        self.seven_button = Button(self, text='7', bg='pink', fg='red', cursor='heart',command=lambda:Controller.buttonClick('7', self.value))
        self.seven_button.grid(row=3, column=1)

        self.eight_button = Button(self, text='8', bg='pink', fg='red', cursor='heart', command=lambda:Controller.buttonClick('8', self.value))
        self.eight_button.grid(row=3, column=2)

        self.nine_button = Button(self, text='9', bg='pink', fg='red', cursor='heart', command=lambda:Controller.buttonClick('9', self.value))
        self.nine_button.grid(row=3, column=3)

        self.zero_button = Button(self, text='0', bg='pink', fg='red', cursor='heart', command=lambda:Controller.buttonClick('0', self.value))
        self.zero_button.grid(row=4, column=1) 

        self.clear_button = Button(self, text='CLEAR', bg='lightgreen', fg='red', cursor='heart', command=lambda:Model.clear(self.value))
        self.clear_button.grid(rowspan=3) 

window = Tk()

calculette = View(window)

calculette.mainloop()

