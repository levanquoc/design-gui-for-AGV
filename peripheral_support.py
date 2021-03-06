#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#    Nov 02, 2020 02:09:46 PM +07  platform: Linux

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

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    showLineStatus()
    showHallInput()
def quit():
    print('peripheral_support.quit')
    root.destroy()
    sys.stdout.flush()
def showLineStatus():
    ledFont=[w.led1Front,w.led2Front,w.led3Front,w.led4Front,w.led5Front,w.led6Front,w.led7Front,w.led8Front]
    ledBack=[w.led1Back,w.led2Back,w.led3Back,w.led4Back,w.led5Back,w.led6Back,w.led7Back,w.led8Back]
    statusFront=[0,1,1,0,1,1,1,0]
    statusBack=[0,1,1,0,1,1,1,0]
    for i in range(0,len(statusFront)):
        if(statusFront[i]==0):
            ledFont[i].configure(background="white")
        else:    
            ledFont[i].configure(background="red")
    for i in range(0,len(statusBack)):
        if(statusBack[i]==0):
            ledBack[i].configure(background="white")
        else:    
            ledBack[i].configure(background="red")        
    root.after(1000,showLineStatus)
def showHallInput():
    hallinputStatus=[0,1]
    ledhallinput=[w.ledRight,w.ledLeft]
    for i in range(0,len(hallinputStatus)):
        if(hallinputStatus[i]==0):
            ledhallinput[i].configure(background="white")
        else:
            ledhallinput[i].configure(background='red')
    root.after(1000,showHallInput)        
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import peripheral
    peripheral.vp_start_gui()




