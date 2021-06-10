from tkinter import*
from PIL import Image, ImageTk, ImageDraw #pip install pillow
from datetime import*
import time
from math import*

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Analog Clock")
        self.root.geometry("700x500")
        self.root.config(bg="#2f4f4f")

        title= Label(self.root, text="Analog_Clock", font=("times new roman", 50, "bold"), bg=("white")).place(x=0,y=30, relwidth=1)

        self.lbl=Label(self.root, bg="white")
        self.lbl.place(x=450, y=150, height=400, width=400)

        self.working()
      
    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400,400), (255,255,255))
        draw = ImageDraw.Draw(clock)
        #====For Clock Image====
        bg = Image.open('cl.jfif')
        bg = bg.resize((300,300), Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        #====Hour Line Image====
        origin = 200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))), fill="black", width = 4)
         #====Minute Line Image====
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))), fill="red", width = 4)
         #====Second Line Image====
        draw.line((origin,200+80*sin(radians(sec_)),200-100*cos(radians(sec_))), fill="green", width = 4)
               
        clock.save("clock_new.png")
    
    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360
        # print(h,m,s)
        # print(hr, min_, sec_)

        self.clock_image(hr,min_,sec_)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

     
root = Tk()
obj = Clock(root)
root.mainloop()