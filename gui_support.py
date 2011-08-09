from Tkinter import *
import os, webbrowser

def get_system_bg(): return Label()['bg']
def get_system_font(): return Label()['font']

def enum(**enums):
    return type('Enum', (), enums)

ButtonTypes = enum(OK=0b00000001, CANCEL=0b00000010)

class ModalDialog(Toplevel):
    """Modal Tkinter dialog window

    A modal toplevel dialog box for Tkinter, modeled after the Dialog class
    presented in the tkinterbook:

    http://effbot.org/tkinterbook/

    """

    BUTTONS = ButtonTypes.OK | ButtonTypes.CANCEL

    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent
        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx() + 50,
                                  parent.winfo_rooty() + 50))
        self.initial_focus.focus_set()
        self.wait_window(self)

    def body(self, master):
        pass

    def buttonbox(self):
        box = Frame(self, padx=5, pady=5)

        if self.BUTTONS & ButtonTypes.OK:
            w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
            w.pack(side=LEFT, padx=5, pady=5)
            self.bind("<Return>", self.ok)

        if self.BUTTONS & ButtonTypes.CANCEL:
            w = Button(box, text="Cancel", width=10, command=self.cancel)
            w.pack(side=LEFT, padx=5, pady=5)
            self.bind("<Escape>", self.cancel)

        box.pack()

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()
        self.cancel()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def validate(self):
        return True

    def apply(self):
        pass


def web_action(url):
    return lambda: webbrowser.open(url)


class HyperlinkManager:
    """Hyperlink manager for text widgets

    A utility class for adding hyperlinks to a Tkinter text widget, based
    on the example found in the Tkinter book:

    http://effbot.org/zone/tkinter-text-hyperlink.htm

    """

    def __init__(self, text):
        self.text = text
        self.text.tag_config("hyper", foreground="blue", underline=1)
        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)
        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def insert_url(self, index, url, text=None):
        if text == None: text = url
        self.text.insert(index, text, self.add(web_action(url)))

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return
