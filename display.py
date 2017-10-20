import time
from wrekscrape import *


from tkinter import *
class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.frame = Frame(self.tk)
        self.frame.grid()
        self.state = False
        self.tk.configure(background='white')
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.escape)

    def escape(self, event=None):
        exit()
        self.tk.destroy
        raise Exception("Exiting")




    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)

        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
font1 = ("Helvetica", "50","bold")
font2 = ("Helvetica", "50")
font3 = ("Helvetica", "10")

def pull():
    s.update()
    artistv.set(s.artist)
    titlev.set(s.title)
    albumv.set(s.album)
    print("update",s.artist,s.title,s.album)
    w.tk.after(5000,pull)

if __name__ == '__main__':
    s = Scraper()
    w = Fullscreen_Window()
    logo = PhotoImage(file="WREK_Logo.png")
    w.toggle_fullscreen()
    artistv = StringVar()
    titlev = StringVar()
    albumv = StringVar()
    s.update()
    artistv.set(s.artist)
    titlev.set(s.title)
    albumv.set(s.album)

    img = Label(w.tk, image=logo, background='white').grid(row=0,column=0, rowspan=2)

    info = Label(w.tk, text="© Gibran Essa, 2017; may not work during specialty shows" , font = font3, background='white').grid(row=0,column=1,sticky='nw')

    top = Label(w.tk, text=" Song Playing:" , font = font1, background='white').grid(row=1,column=1,columnspan=2,sticky='s')

    a = Label(w.tk, text=" Artist: ", font = font1, background='white').grid(row=2,column=1,sticky='w')

    a1 = Label(w.tk, textvariable = artistv, font = font2, background='white').grid(row=2,column=2,sticky='w')

    t = Label(w.tk, text=" Title: ", font = font1, background='white').grid(row=3,column=1,sticky='w')

    t1 = Label(w.tk, textvariable = titlev, font = font2, background='white').grid(row=3,column=2,sticky='w')

    al = Label(w.tk, text=" Album: ", font = font1, background='white').grid(row=4,column=1,sticky='w')

    al1 = Label(w.tk, textvariable = albumv, font = font2, background='white').grid(row=4,column=2,sticky='w')
    pull()
    w.tk.mainloop()
