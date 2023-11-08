import tkinter as tk
import math
import time

clear = 'systemTransparent'
centerx, centery = (275 + 25) / 2, (50 + 300)/2
radius = (300 - 50) / 2
lenSec = 80
lenMin = 110
lenHour = 50


class app:
    window = None
    canvas = None
    secondsHand = None
    minutesHand = None
    hoursHand = None
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CSCI 371 Clock Project")
        self.window.geometry('300x400+0+0')
        self.window.resizable(False, False)
    def createApp(self):
        self.createBase()
        self.createHands()
    def createBase(self):
        self.canvas = tk.Canvas(width = 300, height = 500, bg = "white")
        self.canvas.pack(padx = 0, pady = 0)
        self.canvas.create_oval(25, 50, 275, 300, width=4, fill="#B6B6B6")
        # Create Numbers on Clock
        for i in range(1, 13):
            x, y = centerx + (radius - 20) * (math.cos(math.radians(270 + ((360/12) * i)))), centery  + (radius - 20) * (math.sin(math.radians((270 + (360/12) * i))))
            self.canvas.create_text(x, y, text=str(i), font='tkDefaultFont 24')
    def createHands(self):
        self.secondsHand = self.canvas.create_line(centerx, centery, centerx, centery - lenSec, width=2, fill="red")
        self.minutesHand = self.canvas.create_line(centerx, centery, centerx, centery + lenMin, width=2, fill="black")
        self.hoursHand = self.canvas.create_line(centerx, centery, centerx, centery + lenMin, width=4, fill="black")
        self.canvas.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, width=0, fill="black")
        self.animate()
    def updateHands(self):
        timeStruct = time.localtime()
        seconds = timeStruct.tm_sec
        minutes = timeStruct.tm_min
        hour = timeStruct.tm_hour
        hour = hour % 12
        seconds = seconds % 60

        #Create temp variables
        secondsx, secondsy = centerx + lenSec * (math.cos(math.radians(270 + ((360/60) * seconds)))), centery  + lenSec * (math.sin(math.radians((270 + (360/60) * seconds))))
        minx, miny = centerx + lenMin * (math.cos(math.radians(270 + ((360/60) * minutes)))), centery  + lenMin * (math.sin(math.radians((270 + (360/60) * minutes))))
        hourx, houry = centerx + lenHour * (math.cos(math.radians(270 + ((360/12) * hour)))), centery  + lenHour * (math.sin(math.radians((270 + (360/12) * hour))))
        
        #Update Coords
        self.canvas.coords(self.secondsHand, centerx, centery, secondsx, secondsy)
        self.canvas.coords(self.minutesHand, centerx, centery, minx, miny)
        self.canvas.coords(self.hoursHand, centerx, centery, hourx, houry)
    def animate(self):
        self.updateHands()
        self.window.after(500, self.animate)
if __name__ == "__main__":
    a = app()
    a.createApp()
    a.window.mainloop()