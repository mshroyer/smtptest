#!/usr/bin/python

from Tkinter import *

class SmtpTestApp:
    "smtptest main window"

    def hello(self):
        print "Hello!"

    def add_entry(self, text):
        column, row = self.frame.grid_size()

        label = Label(self.frame, text=text)
        label.grid(row=row, column=0, sticky=E, padx=2)
        entry = Entry(self.frame)
        entry.grid(row=row, column=1, sticky=E+W)

    def add_menu(self):
        menubar = Menu(self.root)

        # "File" menu
        menu_file = Menu(menubar, tearoff=0)
        menu_file.add_command(label="Quit", command=self.hello)
        menubar.add_cascade(label="File", menu=menu_file)

        # "Help" menu
        menu_help = Menu(menubar, tearoff=0)
        menu_help.add_command(label="About", command=self.hello)
        menubar.add_cascade(label="Help", menu=menu_help)

        root.config(menu=menubar)

    def add_status(self):
        status = Label(self.root, text="", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

    def __init__(self, root):
        root.title("smtptest")
        root.geometry("%dx%d" % (640, 480))

        self.root = root
        self.frame = Frame(root)

        self.add_menu()
        self.add_status()

        serverLabel = Label(self.frame, text="Server:")
        serverLabel.grid(row=0, column=0, sticky=E, padx=2)
        serverEntry = Entry(self.frame)
        serverEntry.grid(row=0, column=1, sticky=E+W, padx=2)
        portLabel = Label(self.frame, text="Port:")
        portLabel.grid(row=0, column=2, sticky=E, padx=2)
        portEntry = Entry(self.frame)
        portEntry.insert(0, "25")
        portEntry.grid(row=0, column=3, sticky=E+W, padx=2)
        connect = Button(self.frame, text="Connect")
        connect.grid(row=0, column=4, sticky=E, padx=2)

        self.frame.pack()

root = Tk()
app = SmtpTestApp(root)
root.mainloop()
