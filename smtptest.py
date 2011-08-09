#!/usr/bin/python

from Tkinter import *
from gui_support import *

class SmtpTestApp:
    "smtptest main window"

    def __init__(self, root):
        root.title("smtptest")
        root.geometry("%dx%d" % (640, 480))

        self.root = root
        self.frame = Frame(root)

        self.add_menu()
        self.add_status("Not connected.")

        self.frame.pack()

    def connect(self):
        d = ConnectDialog(self.root, "Connect to server")

    def about(self):
        d = AboutDialog(self.root, "About smtptest")

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
        menu_help.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=menu_help)

        root.config(menu=menubar)

    def add_status(self, text=""):
        self.status_string = StringVar()
        self.status_string.set(text)
        status_label = Label(self.root, textvariable=self.status_string, bd=1, relief=SUNKEN, anchor=W)
        status_label.pack(side=BOTTOM, fill=X)


class ConnectDialog(ModalDialog):
    def body(self, master):
        Label(master, text="Server:").grid(row=0, column=0, sticky=E, padx=2)
        self.entry_server = Entry(master)
        self.entry_server.grid(row=0, column=1, sticky=E, padx=2)

        Label(master, text="Port:").grid(row=1, column=0, sticky=E, padx=2)
        self.entry_port = Entry(master)
        self.entry_port.grid(row=1, column=1, sticky=E, padx=2)

    def apply(self):
        server = self.entry_server.get()
        port = self.entry_port.get()
        print server, port


class AboutDialog(ModalDialog):
    BUTTONS = ButtonTypes.OK
    
    def body(self, master):
        text = Text(master, padx=10, pady=10, width=52, height=5, relief=FLAT, wrap=WORD)
        hyperlink = HyperlinkManager(text)

        text.insert(INSERT, "A simple interactive SMTP testing tool."
                    + " Please see the Github project page for information"
                    + " and source code:\n\n")
        hyperlink.insert_url(INSERT, "https://github.com/markshroyer/smtptest/")
        text.config(state=DISABLED)

        # Cause I'll be damned if I know how to actually specify a
        # transparent background for a Text widget in Tk...
        text.config(bg=get_system_bg())
        text.config(font=get_system_font())
        
        text.pack()


root = Tk()
app = SmtpTestApp(root)
root.mainloop()
