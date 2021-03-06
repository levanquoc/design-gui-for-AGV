#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#    Nov 02, 2020 08:34:08 AM +07  platform: Linux

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

        top.geometry("735x455+0+0")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("AGV ROBOT SYSTEM")
        top.configure(background="#c0c0c0")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=-0.016, rely=-0.011, relheight=0.33
                , relwidth=1.016)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#EC449E")

        self.logoasti = tk.Label(self.Frame1)
        self.logoasti.place(relx=0.016, rely=0.06, height=131, width=354)
        self.logoasti.configure(activebackground="#f9f9f9")
        self.logoasti.configure(background="#E93474")
        self.logoasti.configure(font="-family {Rockwell Condensed} -size 24")
        photo_location = os.path.join(prog_location,"../../Quoc/gui/a.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.logoasti.configure(image=_img0)
        self.logoasti.configure(text='''Label''')

        self.agvrobotsystem = tk.Label(self.Frame1)
        self.agvrobotsystem.place(relx=0.509, rely=0.067, height=118, width=407)
        self.agvrobotsystem.configure(activebackground="#EC449E")
        self.agvrobotsystem.configure(background="#Ec449e")
        self.agvrobotsystem.configure(font="-family {Liberation Serif} -size 22 -weight bold")
        self.agvrobotsystem.configure(foreground="#99f443")
        self.agvrobotsystem.configure(text='''AGV ROBOT SYSTEM''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.316, relheight=0.851, relwidth=1.027)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#8AAAE5")
        self.Frame2.configure(highlightcolor="#d9d9d9")

        self.selectOption = tk.LabelFrame(self.Frame2)
        self.selectOption.place(relx=0.013, rely=0.155, relheight=0.478
                , relwidth=0.42)
        self.selectOption.configure(relief='groove')
        self.selectOption.configure(font="-family {DejaVu Sans} -size 15")
        self.selectOption.configure(foreground="#ffffff")
        self.selectOption.configure(text='''SELECT OPTION''')
        self.selectOption.configure(background="#8AAAE5")

        self.settingButton = tk.Button(self.selectOption)
        self.settingButton.place(relx=0.066, rely=0.346, height=64, width=87
                , bordermode='ignore')
        self.settingButton.configure(activebackground="#f9f9f9")
        self.settingButton.configure(background="#4A171E")
        self.settingButton.configure(command=main_support.setting)
        self.settingButton.configure(font="-family {DejaVu Sans} -size 10")
        self.settingButton.configure(foreground="#E2B144")
        self.settingButton.configure(pady="0")
        self.settingButton.configure(text='''SETTING''')

        self.showButton = tk.Button(self.selectOption)
        self.showButton.place(relx=0.379, rely=0.346, height=64, width=87
                , bordermode='ignore')
        self.showButton.configure(activebackground="#f9f9f9")
        self.showButton.configure(background="#4A171E")
        self.showButton.configure(command=main_support.show)
        self.showButton.configure(font="-family {DejaVu Sans} -size 9")
        self.showButton.configure(foreground="#E2B144")
        self.showButton.configure(pady="0")
        self.showButton.configure(text='''INFORMATION''')

        self.peripheralButton = tk.Button(self.selectOption)
        self.peripheralButton.place(relx=0.688, rely=0.346, height=64, width=87
                , bordermode='ignore')
        self.peripheralButton.configure(activebackground="#f9f9f9")
        self.peripheralButton.configure(background="#4A171E")
        self.peripheralButton.configure(command=main_support.peripheral)
        self.peripheralButton.configure(font="-family {DejaVu Sans} -size 10")
        self.peripheralButton.configure(foreground="#E2B144")
        self.peripheralButton.configure(pady="0")
        self.peripheralButton.configure(text='''PERIPHERAL''')

        self.exitButton = tk.Button(self.Frame2)
        self.exitButton.place(relx=0.834, rely=0.651, height=54, width=87)
        self.exitButton.configure(activebackground="#f9f9f9")
        self.exitButton.configure(background="#D2302C")
        self.exitButton.configure(command=main_support.quit)
        self.exitButton.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.exitButton.configure(foreground="#f7f7f9")
        self.exitButton.configure(pady="0")
        self.exitButton.configure(text='''EXIT''')

        self.timeLabel = tk.Label(self.Frame2)
        self.timeLabel.place(relx=0.041, rely=0.0, height=40, width=155)
        self.timeLabel.configure(activebackground="#f9f9f9")
        self.timeLabel.configure(background="#262223")
        self.timeLabel.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.timeLabel.configure(foreground="#ddc6b6")

        self.pinLabel = tk.Label(self.Frame2)
        self.pinLabel.place(relx=0.278, rely=0.0, height=41, width=116)
        self.pinLabel.configure(activebackground="#f9f9f9")
        self.pinLabel.configure(background="#262223")
        self.pinLabel.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.pinLabel.configure(foreground="#ddc6b6")

        self.speedLabel = tk.Label(self.Frame2)
        self.speedLabel.place(relx=0.487, rely=0.0, height=39, width=120)
        self.speedLabel.configure(activebackground="#f9f9f9")
        self.speedLabel.configure(background="#262223")
        self.speedLabel.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.speedLabel.configure(foreground="#ddc6b6")

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.874, rely=0.0, height=55, width=75)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=main_support.engSetting)
        photo_location = os.path.join(prog_location,"../../Quoc/gui/eng.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img1)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.775, rely=0.0, height=55, width=75)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(command=main_support.vietSetting)
        photo_location = os.path.join(prog_location,"../../Quoc/gui/vie.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img2)
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')

        self.selectControl = tk.LabelFrame(self.Frame2)
        self.selectControl.place(relx=0.517, rely=0.16, relheight=0.478
                , relwidth=0.384)
        self.selectControl.configure(relief='groove')
        self.selectControl.configure(font="-family {DejaVu Sans} -size 15")
        self.selectControl.configure(foreground="#ffffff")
        self.selectControl.configure(text='''CONTROL''')
        self.selectControl.configure(background="#8AAAE5")

        self.startButton = tk.Button(self.selectControl)
        self.startButton.place(relx=0.138, rely=0.286, height=71, width=91
                , bordermode='ignore')
        self.startButton.configure(background="#4A171E")
        self.startButton.configure(command=main_support.startProgram)
        self.startButton.configure(font="-family {DejaVu Sans} -size 12")
        self.startButton.configure(foreground="#E2B144")
        self.startButton.configure(text='''START''')

        self.stopButton = tk.Button(self.selectControl)
        self.stopButton.place(relx=0.586, rely=0.281, height=71, width=91
                , bordermode='ignore')
        self.stopButton.configure(background="#4A171E")
        self.stopButton.configure(command=main_support.stopProgram)
        self.stopButton.configure(font="-family {DejaVu Sans} -size 12")
        self.stopButton.configure(foreground="#E2B144")
        self.stopButton.configure(text='''STOP''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





