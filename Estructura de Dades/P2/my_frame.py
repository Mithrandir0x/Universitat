# -*- coding: iso-8859-15 -*-

#
# my_frame.py
#
# author: olopezsa13
#

from Tkinter import *

"""
This class is a custom type of tkinter's Frame. When instanced, it will
display the UB logo, with a label indicating the size of the logo.

Be careful as it will define the window's size.
"""
class UbFrame(Frame):
    """
    Class constructor. Takes as argument the root widget which UbFrame will
    be appended to.
    """
    def __init__(self, master = None):
        # Call base (or inherited) class constructor.
        Frame.__init__(self, master)

        # Internal properties initialization. Although not really needed, but
        # it makes easier to know which properties does have.
        # Also, the logo image is load at this point.
        self.ubLogo = PhotoImage(file = 'logoub.gif')
        self.logoCanvas = None
        self.label = None

        # Pack the frame to the root widget.
        self.pack()

        # Initialize internal components to be rendered.
        self.initializeMainWindow(master)
        self.initializeUbLogo()
        self.initializeLabel()

    """
    This method defines the size of the root widget that will contain this
    instance of UbFrame.
    """
    def initializeMainWindow(self, master):
        master.title = "UB Window"
        master.geometry("%dx%d" % (self.ubLogo.width(), self.ubLogo.height() + 42))

    """
    This method creates a canvas instance with the UB logo, and appends it to
    the root widget.
    """
    def initializeUbLogo(self):
        self.logoCanvas = Canvas(self, width = self.ubLogo.width(), height = self.ubLogo.height() - 4, bg = "black")
        self.logoCanvas.create_image(0, 0, image = self.ubLogo, anchor = NW)
        self.logoCanvas.pack()

    """
    This method creates a label instance with the text containing the UB logo
    size, and adds it to the root widget.
    """
    def initializeLabel(self):
        self.label = Label(self, text = "This image is\n %d width x %d height" % (self.ubLogo.width(), self.ubLogo.height()))
        self.label.pack()

tk = Tk()
widget = UbFrame(master = tk)

tk.mainloop()
