#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Oct 21, 2020 05:44:45 AM GMT  platform: Windows NT
#    Oct 21, 2020 05:59:08 AM GMT  platform: Windows NT

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

def pinInformation():
    print('selectInformation_support.pinInformation')
    import information
    information.create_INFORMATION(root)
    sys.stdout.flush()

def eixt():
    print('selectInformation_support.eixt')
    root.destroy()
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import selectInformation
    selectInformation.vp_start_gui()




