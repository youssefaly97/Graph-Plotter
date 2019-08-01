# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 22:46:18 2019

@author: Youssef Aly
"""
#import tkinter as tk
#
#from tkinter import filedialog
#from tkinter import *
#import os
#
#def browse_button():
#    # Allow user to select a directory and store it in global var
#    # called folder_path
#    global folder_path
#    filename = filedialog.askdirectory()
#    folder_path.set(filename)
#    print(os.listdir(filename))
#    print(filename.split("/")[-1])
#
#
#root = Tk()
#folder_path = StringVar()
#lbl1 = Label(master=root,textvariable=folder_path)
#lbl1.grid(row=0, column=1)
#button2 = Button(text="Browse", command=browse_button)
#button2.grid(row=0, column=3)
#
#mainloop()


from tkinter import *
      
root = Tk() 
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu,tearoff=False) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu,tearoff=False) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 
mainloop() 
