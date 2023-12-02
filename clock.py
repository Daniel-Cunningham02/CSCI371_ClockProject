import tkinter as tk
from tkinter import ttk
import math
import time


class app:
    centerx, centery = 0, 0 
    radius = (300 - 50) / 2
    lenSec = 80
    lenMin = 110
    lenHour = 50
    diffx = 0
    diffy = 0
    coordinatesText = None
    coordinatesEntry = None

    seconds = None
    minutes = None
    hour = None
    inpSeconds = 0
    inpMinutes = 0
    inpHours = 0
    test = False
    window = None
    canvas = None
    secondsHand = None
    minutesHand = None
    hoursHand = None
    testButton = None
    hourInp = None
    minInp = None
    secInp = None
    def __init__(self):
        self.numbers = []
        self.window = tk.Tk()
        self.window.title("CSCI 371 Clock Project")
        self.window.geometry('300x450+0+0')
        self.window.resizable(False, False)
        self.inpSeconds = tk.IntVar()
        self.inpMinutes = tk.IntVar()
        self.inpHours = tk.IntVar()
        self.coordinatesText = tk.StringVar()
        self.diffx = tk.IntVar()
        self.diffy = tk.IntVar()
        self.centerx, self.centery = (275 + (25) + self.diffx.get()) / 2, ((50) + (300) + self.diffy.get())/2

    def createApp(self):
        self.createBase()
        self.createHands()

    def createBase(self):
        self.canvas = tk.Canvas(width = 300, height = 300, bg = "white")
        self.canvas.pack(padx = 0, pady = 0)
        self.border = self.canvas.create_oval(25 + self.diffx.get()/2, 50 + self.diffy.get()/2, 275 + self.diffx.get()/2, 300 + self.diffy.get()/2, width=3, fill="#ffffff")
        self.testButton = ttk.Button(self.window, text="Test!", command=self.switchModes)
        self.testButton.pack()
        self.test = False
        self.createOptions()
        
        # Create Numbers on Clock
        for i in range(1, 13):
            x, y = self.centerx + (self.radius - 20) * (math.cos(math.radians(270 + ((360/12) * i)))), self.centery  + (self.radius - 20) * (math.sin(math.radians((270 + (360/12) * i))))
            text = self.canvas.create_text(x, y, text=str(i), font='tkDefaultFont 24')
            self.numbers.append(text)

    def createHands(self):
        self.minutesHand = self.canvas.create_line(self.centerx, self.centery, self.centerx, self.centery + self.lenMin, width=2, fill="black")
        self.secondsHand = self.canvas.create_line(self.centerx, self.centery, self.centerx, self.centery - self.lenSec, width=2, fill="red")
        self.hoursHand = self.canvas.create_line(self.centerx, self.centery, self.centerx, self.centery + self.lenMin, width=4, fill="black")
        self.point = self.canvas.create_oval(self.centerx - 5, self.centery - 5, self.centerx + 5, self.centery + 5, width=0, fill="black")
        self.animate()

    def updateHands(self):
        try:
            self.centerx, self.centery = (275 + (25) + self.diffx.get()) / 2, ((50) + (300) + self.diffy.get())/2
            self.canvas.coords(self.point, self.centerx - 5, self.centery - 5, self.centerx + 5, self.centery + 5 )
            for i in range(len(self.numbers)):
                x, y = self.centerx + (self.radius - 20) * (math.cos(math.radians(270 + ((360/12) * i+1)))), self.centery  + (self.radius - 20) * (math.sin(math.radians((270 + (360/12) * i+1))))
                self.canvas.coords(self.numbers[i], x, y)
        except:
            pass
        if not self.test:
            timeStruct = time.localtime()
            self.seconds = timeStruct.tm_sec
            self.minutes = timeStruct.tm_min
            self.hour = timeStruct.tm_hour
            self.hour = self.hour % 12
            self.seconds = self.seconds % 60
            #Create temp variables
        else:
            try:
                self.seconds = int(self.secInp.get()) % 60
                self.hour = int(self.hourInp.get()) % 12
                self.minutes = int(self.minInp.get()) % 60
            except:
                print("Error occured parsing test") 

        secondsx, secondsy = self.centerx + self.lenSec * (math.cos(math.radians(270 + ((360/60) * self.seconds)))), self.centery  + self.lenSec * (math.sin(math.radians((270 + (360/60) * self.seconds))))
        minx, miny = self.centerx + self.lenMin * (math.cos(math.radians(270 + ((360/60) * (self.minutes + self.seconds/60))))), self.centery  + self.lenMin * (math.sin(math.radians((270 + (360/60) * (self.minutes + self.seconds/60)))))
        hourx, houry = self.centerx + self.lenHour * (math.cos(math.radians(270 + ((360/12) * (self.hour + self.minutes/60))))), self.centery  + self.lenHour * (math.sin(math.radians((270 + (360/12) * (self.hour + self.minutes/60)))))
        
        #Update Coords
        self.canvas.coords(self.secondsHand, self.centerx, self.centery, secondsx, secondsy)
        self.canvas.coords(self.minutesHand, self.centerx, self.centery, minx, miny)
        self.canvas.coords(self.hoursHand, self.centerx, self.centery, hourx, houry)
        try:
            self.canvas.coords(self.border, 25 + self.diffx.get()/2, 50 + self.diffy.get()/2, 275 + self.diffx.get()/2, 300 + self.diffy.get()/2)
            newMinLength = self.sizeSlider.get()
            
            self.lenHour = findRatio(self.lenHour, self.lenMin, newMinLength)
            self.lenSec = findRatio(self.lenSec, self.lenMin, newMinLength)
            self.lenMin = newMinLength
            print(self.lenHour, self.lenSec, self.lenMin)
        except:
            self.lenHour = self.lenHour
            self.lenSec = self.lenSec
            self.lenMin = self.lenMin
            print(self.lenHour, self.lenSec, self.lenMin)

            
    def createOptions(self):
        self.sizeSliderVar = 110
        self.sliderFrame = tk.Frame(self.window)
        self.sliderFrame.pack()
        self.sizeLabel = ttk.Label(self.sliderFrame, text="Size:")
        self.sizeLabel.pack(side="left")
        self.sizeSlider = ttk.Scale(self.sliderFrame, value=110, from_=50, to=110, variable=self.sizeSliderVar)
        self.sizeSlider.pack(side="left")
        self.generateButton = ttk.Button(self.sliderFrame, text="Generate", command=self.generateCoordinates)
        self.generateButton.pack(side="left")

        # Create New Frame
        self.changeCenterFrame = tk.Frame(self.window)
        self.changeCenterFrame.pack()
        self.diffxLabel = ttk.Label(self.changeCenterFrame, text="Translate X:")
        self.diffxLabel.pack(side="left")
        self.diffxInp = tk.Entry(self.changeCenterFrame, width=5, textvariable=self.diffx)
        self.diffxInp.pack(side="left")
        self.diffxLabel = ttk.Label(self.changeCenterFrame, text="Translate Y:")
        self.diffxLabel.pack(side="left")
        self.diffyInp = tk.Entry(self.changeCenterFrame,width=5, textvariable=self.diffy)
        self.diffyInp.pack(side="left")

    def switchModes(self):
        if self.test:
            self.test = False
            self.hourLabel.destroy()
            self.hourInp.destroy()
            self.minLabel.destroy()
            self.minInp.destroy()
            self.secLabel.destroy()
            self.secInp.destroy()
            self.testFrame.destroy()
        else:
            self.test = True
            #Hour
            self.testFrame = tk.Frame(self.window)
            self.testFrame.pack()
            self.hourLabel = ttk.Label(self.testFrame,text="Hour:", width=10)
            self.hourLabel.pack(side="left", expand=True)
            self.hourInp = tk.Entry(self.testFrame, width=5, textvariable=self.inpHours)
            self.hourInp.pack(side="left")

            #Minutes
            self.minLabel = ttk.Label(self.testFrame,text="Minutes:", width=10)
            self.minLabel.pack(side="left")
            self.minInp = tk.Entry(self.testFrame,width=5, textvariable=self.inpMinutes)
            self.minInp.pack(side="left")

            #Seconds
            self.secLabel = ttk.Label(self.testFrame,text="Seconds:", width=10, padding=0)
            self.secLabel.pack(side="left")
            self.secInp = tk.Entry(self.testFrame,width=5, textvariable=self.inpSeconds)
            self.secInp.pack( side="left")

    def generateCoordinates(self):
        if(self.coordinatesEntry == None):
            self.coordinateFrame= tk.Frame(self.window)
            self.coordinateFrame.pack(fill="x")
            self.coordinatesEntry = tk.Entry(self.coordinateFrame, textvariable=self.coordinatesText)
            self.coordinatesEntry.pack(fill="x")
        temp = str("{:.2f}".format(self.centerx)) + ', ' + str("{:.2f}".format(self.centery)) + "  "
        temp += str("{:.2f}".format(self.canvas.coords(self.hoursHand)[2])) + ', ' + str("{:.2f}".format(self.canvas.coords(self.hoursHand)[3])) + "  "
        temp += str("{:.2f}".format(self.canvas.coords(self.minutesHand)[2])) + ', ' + str("{:.2f}".format(self.canvas.coords(self.minutesHand)[3])) + "  "
        temp += str("{:.2f}".format(self.canvas.coords(self.secondsHand)[2])) + ', ' + str("{:.2f}".format(self.canvas.coords(self.secondsHand)[3]))
        self.coordinatesText.set(temp)
    def animate(self):
        self.updateHands()
        self.window.after(500, self.animate)


# Finds ratio to find new size of the hands
def findRatio(oldX, oldLenMin, NewLenMin):
    temp = (NewLenMin * oldX) / oldLenMin
    if temp > 0:
        return temp
    else:
        return oldX 

if __name__ == "__main__":
    a = app()
    a.createApp()
    a.window.mainloop()