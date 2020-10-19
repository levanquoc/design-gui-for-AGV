#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Oct 19, 2020 02:40:19 AM GMT  platform: Windows NT

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

import main_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 24"

        top.geometry("1920x1017+-254+44")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("AGV ROBOT SYSTEM")
        top.configure(background="#c0c0c0")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=-0.016, rely=-0.01, relheight=0.326
                , relwidth=1.016)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#E93474")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.logoasti = tk.Label(self.Frame1)
        self.logoasti.place(relx=-0.051, rely=0.181, height=199, width=795)
        self.logoasti.configure(activebackground="#f9f9f9")
        self.logoasti.configure(activeforeground="black")
        self.logoasti.configure(background="#E93474")
        self.logoasti.configure(disabledforeground="#a3a3a3")
        self.logoasti.configure(font="-family {Rockwell Condensed} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.logoasti.configure(foreground="#000000")
        self.logoasti.configure(highlightbackground="#d9d9d9")
        self.logoasti.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../gui_arv/a.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.logoasti.configure(image=_img0)
        self.logoasti.configure(text='''Label''')

        self.agvrobotsystem = tk.Label(self.Frame1)
        self.agvrobotsystem.place(relx=0.359, rely=0.09, height=261, width=1218)
        self.agvrobotsystem.configure(activebackground="#E93474")
        self.agvrobotsystem.configure(activeforeground="white")
        self.agvrobotsystem.configure(activeforeground="black")
        self.agvrobotsystem.configure(background="#E93474")
        self.agvrobotsystem.configure(cursor="fleur")
        self.agvrobotsystem.configure(disabledforeground="#a3a3a3")
        self.agvrobotsystem.configure(font="-family {Times New Roman} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.agvrobotsystem.configure(foreground="#000000")
        self.agvrobotsystem.configure(highlightbackground="#d9d9d9")
        self.agvrobotsystem.configure(highlightcolor="black")
        self.agvrobotsystem.configure(text='''AGV ROBOT SYSTEM''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.315, relheight=0.827, relwidth=1.004)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#7A88C0")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.selectLanguage = tk.LabelFrame(self.Frame2)
        self.selectLanguage.place(relx=0.038, rely=0.178, relheight=0.541
                , relwidth=0.327)
        self.selectLanguage.configure(relief='groove')
        self.selectLanguage.configure(font="-family {Lucida Sans Unicode} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.selectLanguage.configure(foreground="black")
        self.selectLanguage.configure(text='''SELECT LANGUAGE''')
        self.selectLanguage.configure(background="#7A88C0")
        self.selectLanguage.configure(highlightbackground="#d9d9d9")
        self.selectLanguage.configure(highlightcolor="#646464646464")

        self.vietButton = tk.Button(self.selectLanguage)
        self.vietButton.place(relx=0.111, rely=0.374, height=184, width=207
                , bordermode='ignore')
        self.vietButton.configure(activebackground="#ececec")
        self.vietButton.configure(activeforeground="#000000")
        self.vietButton.configure(background="#d9d9d9")
        self.vietButton.configure(command=main_support.vietSetting)
        self.vietButton.configure(disabledforeground="#a3a3a3")
        self.vietButton.configure(font="-family {Segoe UI} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.vietButton.configure(foreground="#000000")
        self.vietButton.configure(highlightbackground="#d9d9d9")
        self.vietButton.configure(highlightcolor="black")
        self.vietButton.configure(pady="0")
        self.vietButton.configure(text='''VIE''')

        self.engButton = tk.Button(self.selectLanguage)
        self.engButton.place(relx=0.566, rely=0.374, height=184, width=207
                , bordermode='ignore')
        self.engButton.configure(activebackground="#ececec")
        self.engButton.configure(activeforeground="#000000")
        self.engButton.configure(background="#d9d9d9")
        self.engButton.configure(command=main_support.engSetting)
        self.engButton.configure(disabledforeground="#a3a3a3")
        self.engButton.configure(font="-family {Segoe UI} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.engButton.configure(foreground="#000000")
        self.engButton.configure(highlightbackground="#d9d9d9")
        self.engButton.configure(highlightcolor="black")
        self.engButton.configure(pady="0")
        self.engButton.configure(text='''ENG''')

        self.selectOption = tk.LabelFrame(self.Frame2)
        self.selectOption.place(relx=0.477, rely=0.166, relheight=0.553
                , relwidth=0.441)
        self.selectOption.configure(relief='groove')
        self.selectOption.configure(font="-family {Segoe UI} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.selectOption.configure(foreground="black")
        self.selectOption.configure(text='''SELECT OPTION''')
        self.selectOption.configure(background="#7A88C0")
        self.selectOption.configure(highlightbackground="#d9d9d9")
        self.selectOption.configure(highlightcolor="black")

        self.settingButton = tk.Button(self.selectOption)
        self.settingButton.place(relx=0.036, rely=0.413, height=184, width=217
                , bordermode='ignore')
        self.settingButton.configure(activebackground="#ececec")
        self.settingButton.configure(activeforeground="#000000")
        self.settingButton.configure(background="#d9d9d9")
        self.settingButton.configure(command=main_support.setting)
        self.settingButton.configure(disabledforeground="#a3a3a3")
        self.settingButton.configure(font="-family {Segoe UI} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.settingButton.configure(foreground="#000000")
        self.settingButton.configure(highlightbackground="#d9d9d9")
        self.settingButton.configure(highlightcolor="black")
        self.settingButton.configure(pady="0")
        self.settingButton.configure(text='''SETTING''')

        self.showButton = tk.Button(self.selectOption)
        self.showButton.place(relx=0.341, rely=0.409, height=184, width=237
                , bordermode='ignore')
        self.showButton.configure(activebackground="#ececec")
        self.showButton.configure(activeforeground="#000000")
        self.showButton.configure(background="#d9d9d9")
        self.showButton.configure(command=main_support.show)
        self.showButton.configure(disabledforeground="#a3a3a3")
        self.showButton.configure(font="-family {Segoe UI} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.showButton.configure(foreground="#000000")
        self.showButton.configure(highlightbackground="#d9d9d9")
        self.showButton.configure(highlightcolor="black")
        self.showButton.configure(pady="0")
        self.showButton.configure(text='''INFORMATION''')

        self.peripheralButton = tk.Button(self.selectOption)
        self.peripheralButton.place(relx=0.682, rely=0.409, height=184, width=237
                , bordermode='ignore')
        self.peripheralButton.configure(activebackground="#ececec")
        self.peripheralButton.configure(activeforeground="#000000")
        self.peripheralButton.configure(background="#d9d9d9")
        self.peripheralButton.configure(command=main_support.peripheral)
        self.peripheralButton.configure(disabledforeground="#a3a3a3")
        self.peripheralButton.configure(font="-family {Segoe UI} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.peripheralButton.configure(foreground="#000000")
        self.peripheralButton.configure(highlightbackground="#d9d9d9")
        self.peripheralButton.configure(highlightcolor="black")
        self.peripheralButton.configure(pady="0")
        self.peripheralButton.configure(text='''PERIPHERAL''')

        self.exitButton = tk.Button(self.Frame2)
        self.exitButton.place(relx=0.923, rely=0.0, height=124, width=147)
        self.exitButton.configure(activebackground="#ececec")
        self.exitButton.configure(activeforeground="#000000")
        self.exitButton.configure(background="#d9d9d9")
        self.exitButton.configure(command=main_support.quit)
        self.exitButton.configure(disabledforeground="#a3a3a3")
        self.exitButton.configure(font=font9)
        self.exitButton.configure(foreground="#000000")
        self.exitButton.configure(highlightbackground="#d9d9d9")
        self.exitButton.configure(highlightcolor="black")
        self.exitButton.configure(pady="0")
        self.exitButton.configure(text='''EXIT''')

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





