from wrekscrape import *


from tkinter import *
class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.configure(background='white')
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)


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

if __name__ == '__main__':
    w = Fullscreen_Window()
    logo = PhotoImage(file="WREK_Logo.png")
    w.toggle_fullscreen()
    img = Label(w.tk, image=logo, anchor = 'nw', background='white')
    img.pack(fill='both' ,side = 'left')
    a = Label(w.tk, text="Artist: ", font = font1, anchor = 'nw', background='white')
    a.pack(side = 'left')
    a1 = Label(w.tk, text = artist(), font = font2, background='white',  anchor = 'nw')
    a1.pack(side = 'left')

    w.tk.mainloop()
