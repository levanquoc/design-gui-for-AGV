#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Oct 21, 2020 06:37:02 AM GMT  platform: Windows NT

import sys

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

import setting_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = SETTING (root)
    setting_support.init(root, top)
    root.mainloop()

w = None
def create_SETTING(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_SETTING(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = SETTING (w)
    setting_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_SETTING():
    global w
    w.destroy()
    w = None

class SETTING:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 24 -weight bold"

        top.geometry("1920x1017+379+195")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("SETTING")
        top.configure(background="#d9d9d9")

        self.settingLabelframe = tk.LabelFrame(top)
        self.settingLabelframe.place(relx=0.005, rely=0.039, relheight=0.919
                , relwidth=0.972)
        self.settingLabelframe.configure(relief='groove')
        self.settingLabelframe.configure(font=font9)
        self.settingLabelframe.configure(foreground="black")
        self.settingLabelframe.configure(text='''SETTING''')
        self.settingLabelframe.configure(background="#408080")

        self.Label1 = tk.Label(self.settingLabelframe)
        self.Label1.place(relx=0.145, rely=0.193, height=139, width=479
                , bordermode='ignore')
        self.Label1.configure(background="#8080c0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SPEED''')

        self.Entry1 = tk.Entry(self.settingLabelframe)
        self.Entry1.place(relx=0.439, rely=0.193, height=137, relwidth=0.222
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ececec")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="#000000")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="#000000")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





