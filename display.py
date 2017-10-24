import time
from wrekscrape import *


from tkinter import *
class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
 #       self.tk.attributes('-zoomed', True)
        self.frame = Frame(self.tk)
        self.frame.grid()
        self.state = False
        self.logo = PhotoImage(file="WREK_Logo.png")
        self.logoi = PhotoImage(file="WREK_Logo_inv.png")
        self.tk.configure(background='white')
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.escape)
        self.artistv = StringVar()
        self.titlev = StringVar()
        self.albumv = StringVar()
        self.specialtyshowv = StringVar()

        self.img = Label(self.tk, image=self.logo, background='white')
        self.img.grid(row=0,column=0, rowspan=2)
        self.info = Label(self.tk, text="© Gibran Essa, Jack Thomson 2017; may not show correct songs during specialty shows" , font = font3,
                          background='white')
        self.info.grid(row=0,column=1,sticky='nw')
        self.show = Label(self.tk, textvariable = self.specialtyshowv , font = font1, background='white')
        self.show.grid(row=1,column=1,columnspan=2,sticky='s')
        self.top = Label(self.tk, text=" Now Playing:" , font = font1, background='white')
        self.top.grid(row=2,column=1,columnspan=2,sticky='s')
        self.a = Label(self.tk, text=" Artist: ", font = font1, background='white')
        self.a.grid(row=3,column=1,sticky='w')
        self.a1 = Label(self.tk, textvariable = self.artistv, font = font2, background='white')
        self.a1.grid(row=3,column=2,sticky='w')
        self.t = Label(self.tk, text=" Title: ", font = font1, background='white')
        self.t.grid(row=4,column=1,sticky='w')
        self.t1 = Label(self.tk, textvariable = self.titlev, font = font2, background='white')
        self.t1.grid(row=4,column=2,sticky='w')
        self.al = Label(self.tk, text=" Album: ", font = font1, background='white')
        self.al.grid(row=5,column=1,sticky='w')
        self.al1 = Label(self.tk, textvariable = self.albumv, font = font2, background='white')
        self.al1.grid(row=5,column=2,sticky='w')

        self.s = Scraper()


    def escape(self, event=None):
        exit()
        self.tk.destroy
        raise Exception("Exiting")

    def clean(self):
        self.tk.configure(background='black')
        self.img.config(fg='white', bg='black',
                        image=self.logoi)
        self.info.config(fg='white', bg='black')
        self.show.config(fg='white', bg='black')
        self.top.config(fg='white', bg='black')
        self.a.config(fg='white', bg='black')
        self.a1.config(fg='white', bg='black')
        self.t.config(fg='white', bg='black')
        self.t1.config(fg='white', bg='black')
        self.al.config(fg='white', bg='black')
        self.al1.config(fg='white', bg='black')
        self.tk.after(1000,self.clean2)


    def clean2(self):
        self.tk.configure(background='white')
        self.img.config(bg='white', fg='black',
                        image=self.logo)
        self.info.config(bg='white', fg='black')
        self.show.config(bg='white', fg='black')
        self.top.config(bg='white', fg='black')
        self.a.config(bg='white', fg='black')
        self.a1.config(bg='white', fg='black')
        self.t.config(bg='white', fg='black')
        self.t1.config(bg='white', fg='black')
        self.al.config(bg='white', fg='black')
        self.al1.config(bg='white', fg='black')

        self.tk.after(1800000,self.clean)






    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)

        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def pull(self):
        self.s.update()
        self.artistv.set(self.s.artist)
        self.titlev.set(self.s.title)
        self.albumv.set(self.s.album)
        self.specialtyshowv.set(self.s.show)
        print(self.s.show)
        print("update",self.s.artist,self.s.title,self.s.album, self.show)
        self.tk.after(5000,self.pull)

font1 = ("Helvetica", "50","bold")
font2 = ("Helvetica", "50")
font3 = ("Helvetica", "10")


if __name__ == '__main__':

    w = Fullscreen_Window()

    w.toggle_fullscreen()
    w.pull()
    w.clean()

    w.tk.mainloop()
