#!/usr/bin/python

from Tkinter import *

class SmtpTestApp:
    "smtptest main window"

    def __init__(self, root):
        root.title("smtptest")
        root.geometry("%dx%d" % (640, 480))

        self.root = root
        self.frame = Frame(root)

        self.add_menu()
        self.add_status("Not connected.")

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

    def connect(self):
        d = ConnectDialog(self.root)
        self.root.wait_window(d.top)

    def hello(self):
        print "Hello!"

    def status_msg(self, text):
        "Set window status message"

        self.status_string.set(text)

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
        menu_file.add_command(label="Connect...", command=self.connect)
        menu_file.add_command(label="Disconnect", command=self.hello, state=DISABLED)
        menu_file.add_separator()
        menu_file.add_command(label="Quit", command=self.hello)
        menubar.add_cascade(label="File", menu=menu_file)

        # "Help" menu
        menu_help = Menu(menubar, tearoff=0)
        menu_help.add_command(label="About", command=self.hello)
        menubar.add_cascade(label="Help", menu=menu_help)

        root.config(menu=menubar)

    def add_status(self, text=""):
        self.status_string = StringVar()
        self.status_string.set(text)
        status_label = Label(self.root, textvariable=self.status_string, bd=1, relief=SUNKEN, anchor=W)
        status_label.pack(side=BOTTOM, fill=X)


class ConnectDialog:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        
        Label(self.top, text="Server:").grid(row=0, column=0, sticky=E, padx=2)
        self.entry_server = Entry(self.top)
        self.entry_server.grid(row=0, column=1, sticky=E, padx=2)

        Label(self.top, text="Port:").grid(row=1, column=0, sticky=E, padx=2)
        self.entry_port = Entry(self.top)
        self.entry_port.grid(row=1, column=1, sticky=E, padx=2)

        Button(self.top, text="Connect", command=self.connect)\
            .grid(row=2, column=0)
        Button(self.top, text="Cancel", command=self.cancel)\
            .grid(row=2, column=1)

    def connect(self):
        self.top.destroy()

    def cancel(self):
        self.top.destroy()


root = Tk()
app = SmtpTestApp(root)
root.mainloop()
