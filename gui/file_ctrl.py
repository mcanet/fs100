#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#    Sep 26, 2020 11:38:09 AM +0800  platform: Windows NT

from fs100 import FS100
import sys
try:
    from tkinter import messagebox
except:
    import tkMessageBox as messagebox

try:
    from tkinter import filedialog
except:
    import tkFileDialog as filedialog

from fnmatch import filter

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

import file_ctrl_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    file_ctrl_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    file_ctrl_support.init(w, top, *args, **kwargs)
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
        font10 = "-family 細明體 -size 10 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        if __name__ == '__main__':
            top.geometry("860x640+433+263")
            top.title("New Toplevel")
            top.configure(background="#d9d9d9")
        else:
            global prog_location
            #prog_call = sys.argv[0]
            prog_call = __file__
            prog_location = os.path.split(prog_call)[0]

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.598, rely=0.139, relheight=0.72
                , relwidth=0.316)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="-family {Monospace} -size 10")
        if os.name == 'nt':
            self.Scrolledlistbox1.configure(font="-family {Consolas} -size 11")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=264)

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.598, rely=0.087, height=23, width=115)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Controller''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.836, rely=0.078, height=32, width=32)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"refresh.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img0)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''R''')
        self.Button1.configure(width=40)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.875, rely=0.078, height=32, width=32)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"delete.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img1)
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''D''')
        self.Button2.configure(width=40)

        self.Scrolledlistbox1_2 = ScrolledListBox(top)
        self.Scrolledlistbox1_2.place(relx=0.094, rely=0.139, relheight=0.72
                , relwidth=0.316)
        self.Scrolledlistbox1_2.configure(background="white")
        self.Scrolledlistbox1_2.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1_2.configure(font="-family {Monospace} -size 10")
        if os.name == 'nt':
            self.Scrolledlistbox1_2.configure(font="-family {Consolas} -size 11")
        self.Scrolledlistbox1_2.configure(foreground="black")
        self.Scrolledlistbox1_2.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1_2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1_2.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1_2.configure(selectforeground="black")
        self.Scrolledlistbox1_2.configure(width=264)

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.094, rely=0.017, height=63, width=235)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(wraplength="230")
        self.TLabel2.configure(text='''Tlabel''')
        self.TLabel2.configure(anchor='sw')

        self.Button1_3 = tk.Button(top)
        self.Button1_3.place(relx=0.371, rely=0.078, height=32, width=32)
        self.Button1_3.configure(activebackground="#ececec")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#d9d9d9")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"folder.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button1_3.configure(image=_img2)
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''F''')
        self.Button1_3.configure(width=40)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.432, rely=0.279, height=60, width=110)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''>''')
        self.Button3.configure(width=110)

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.432, rely=0.47, height=60, width=110)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''<''')

        self.robot = FS100('10.0.0.2')
        self.Button1.configure(command=self.on_refresh)
        self.Button2.configure(command=self.on_delete)
        self.Button1_3.configure(command=self.on_folder)
        self.Button3.configure(command=self.on_upload)
        self.Button4.configure(command=self.on_download)
        self.on_refresh()
        self.TLabel2.configure(text=prog_location)
        self.refresh_pc_job_list()

    def on_refresh(self):
        self.Scrolledlistbox1.delete(0, tk.END)
        jobs = []
        if FS100.ERROR_SUCCESS == self.robot.get_file_list('*.JBI', jobs):
            for j in jobs:
                self.Scrolledlistbox1.insert(tk.END, j)

    def on_delete(self):
        sel = self.Scrolledlistbox1.curselection()
        if len(sel) == 1:
            job = self.Scrolledlistbox1.get(sel[0])
            if job != '':
                if messagebox.askyesno("Delete Job", "Are you sure to delete\n'{}'?".format(job)):
                    if FS100.ERROR_SUCCESS == self.robot.delete_file(job):
                        self.on_refresh()

    def refresh_pc_job_list(self):
        self.Scrolledlistbox1_2.delete(0, tk.END)
        for f in filter(os.listdir(self.TLabel2.cget("text")), '*.[Jj][Bb][Ii]'):
            self.Scrolledlistbox1_2.insert(tk.END, f)

    def on_folder(self):
        initdir = self.TLabel2.cget("text")
        dir = filedialog.askdirectory(initialdir=initdir)
        if dir != '':
            self.TLabel2.configure(text=dir)
            self.refresh_pc_job_list()

    def on_download(self):
        sel = self.Scrolledlistbox1.curselection()
        if len(sel) == 1:
            fname = self.Scrolledlistbox1.get(sel[0])
            dir = self.TLabel2.cget("text")
            if FS100.ERROR_SUCCESS == self.robot.recv_file(fname, dir):
                self.refresh_pc_job_list()

    def on_upload(self):
        sel = self.Scrolledlistbox1_2.curselection()
        if len(sel) == 1:
            fname = self.Scrolledlistbox1_2.get(sel[0])
            dir = self.TLabel2.cget("text")
            if FS100.ERROR_SUCCESS == self.robot.send_file(dir + '/' + fname):
                self.on_refresh()


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





