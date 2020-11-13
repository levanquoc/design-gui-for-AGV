#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Oct 19, 2020 03:34:57 AM GMT  platform: Windows NT
#    Oct 19, 2020 03:57:20 AM GMT  platform: Windows NT
#    Nov 03, 2020 10:22:49 AM +07  platform: Linux

from tkinter import messagebox
import sys
import os
import pickle

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    os.system('dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show')
   

def login():
    print('login_support.login')

    data = pickle.loads(open("asti.pickle","rb").read())
    print(data)
    if (w.userNameEntry.get()==data['username']) and (w.passWordEntry.get()==data['password']):
        print('True')
        #to do something
        
        import setting
        setting.create_SETTING(root)
        w.userNameEntry.delete(0,'end')
        w.passWordEntry.delete(0,'end')
        
        #os.system('dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide')
    else:
        messagebox.showinfo("Notification","Username or password is incorrect, please re-enter",parent=root)
        
        w.userNameEntry.delete(0,'end')
        w.passWordEntry.delete(0,'end')
        
    sys.stdout.flush()

def quitLogin():
    print('login_support.quitLogin')
    sys.stdout.flush()
    root.destroy()
    os.system('dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide')
    

def reset():
    print('login_support.reset')
    data = pickle.loads(open("asti.pickle","rb").read())
    if (w.userNameEntry.get()==data['username']) and (w.passWordEntry.get()==data['password']):
        #to do something
        import reset
        reset.create_reset(root)
        w.userNameEntry.delete(0,'end')
        w.passWordEntry.delete(0,'end')
    else:
        messagebox.showinfo("Notification","Username or password is incorrect, please re-enter",parent=root)
        w.userNameEntry.delete(0,'end')
        w.passWordEntry.delete(0,'end')    
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
    

if __name__ == '__main__':
    import login
    login.vp_start_gui()





