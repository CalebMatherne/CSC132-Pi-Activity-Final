##################
#
# Pain
#
##################

# from tkinter import *

# class MainGui(Frame):
#     # constructor
#     def __init__(self, parent):
#         Frame.__init__(self, parent, bg="white")
#         self.setupGUI()



import time
import random
import pygame
import RPi.GPIO
import os, os.path

import tkinter as tk

Displaying = False


# GPIO pin assignments.
pin_R1 = 17
pin_G1 = 18
pin_B1 = 22
pin_R2 = 23
pin_G2 = 24
pin_B2 = 25
pin_A = 27
pin_B = 6
pin_C = 9
pin_Clock = 3 #SCL
pin_Latch = 4
pin_OE = 2

# Display properties.
RED = 0
GREEN = 1
BLUE = 2
FRAME_REPEAT = 50                                      #set from animation file?
DISPLAY_COLS = 32
DISPLAY_ROWS = 16

File = "COES Image"


# PyGame used to read image files from storage.
pygame.init()

# Configure GPIO pins.
RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(pin_R1, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_G1, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_B1, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_R2, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_G2, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_B2, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_A, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_B, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_C, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_Clock, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_Latch, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(pin_OE, RPi.GPIO.OUT, initial=1)

# Sets and Destroys frames
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        # destroys current frame and replaces it
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

### HOME PAGE ###
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        ## Directory ##
        l1= tk.Label(self, text="Choose A Group", font=('Helvetica bold',20))
        l1.grid(row=1, column=2)

        # Moves to Pictures
        b1= tk.Button(self, text="Pictures", font=('Helvetica bold', 35), command=lambda: master.switch_frame(PageOne))
        b1.grid(row=4, column=1)


        # Moves to Animations
        b2= tk.Button(self, text="Animations", font=('Helvetica bold', 35), command=lambda: master.switch_frame(PageTwo))
        b2.grid(row=4,column=3, sticky='w', pady=10)

        # Adds Space to make it look nice
        bSpacer1 = tk.Label(self, text=" ",font=('Helvetica bold', 60))
        bSpacer1.grid(row=0, column=0, columnspan=6)

        bSpacer2 = tk.Label(self, text="     ", font=('Helvetica bold', 20))
        bSpacer2.grid(row=3, column=0)


### PICTURES PAGE ###
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        l1 = tk.Label(self, text="===Pictures===", font=('Helvetica bold',20))
        l1.grid(row=0, column=2)

        # Buttons
        b1 = tk.Button(self, text="<-- Back", font=('Helvetica bold', 20), command=lambda: master.switch_frame(StartPage))
        b1.grid(row=0, column=0)

        b2 = tk.Button(self, text="Microsoft Logo", font=('Helvetica bold',20), command=lambda: ButtonPress("Microsoft Image",200))
        b2.grid(row=2, column=2, sticky='S')

        # Adds space between Buttons and Headline
        bSpacer4 = tk.Label(self, text=" ", font=('Helvetica bold',20))
        bSpacer4.grid(row=1, column= 0)

        # Adds a headline
        bSpacer2 = tk.Label(self, text="======", font=('Helvetica bold',20))
        bSpacer2.grid(row=0, column= 1)

        bSpacer3 = tk.Label(self, text="==========", font=('Helvetica bold',20))
        bSpacer3.grid(row=0, column= 3)

### ANIMATIONS PAGE ###
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        l1 = tk.Label(self, text="Animations", font=('Helvetica bold',20)) # Page Topic
        l1.grid(row=0, column=2, sticky='N', pady=10)

        # Buttons for Animation page
        b1 = tk.Button(self, text="<-- Back", font=('Helvetica bold', 20), command=lambda: BackButton(StartPage)) # returns to main screen
        b1.grid(row=0,column=0, sticky='W')

        b2 = tk.Button(self, text="Circles", font=('Helvetica bold',20),command=lambda: ButtonPress("Circles",10)) # Will show Circles
        b2.grid(row=1, column=2, sticky='S')

        b3 = tk.Button(self, text="LaTech Logo", font=('Helvetica bold',20),command=lambda: ButtonPress("LaTechLogo",200)) # Will show Latech Logo
        b3.grid(row=1, column=3, sticky='S')

        b4 = tk.Button(self, text="Mario", font=('Helvetica bold',20),command=lambda: ButtonPress("Mario",50)) # Will show Mario
        b4.grid(row=1, column=1, sticky='S')

        b5 = tk.Button(self, text="Pac-Man", font=('Helvetica bold',20),command=lambda: ButtonPress("Pac-Man",20)) # Will show Pac-Man
        b5.grid(row=3, column=2, sticky='S')

        b6 = tk.Button(self, text="Rainbow Ripple", font=('Helvetica bold',20),command=lambda: ButtonPress("RainbowRipple",10)) # Will show RainbowRipple
        b6.grid(row=3, column=3, sticky='S')

        # Adds a headline
        bSpacer2 = tk.Label(self, text="=======", font=('Helvetica bold',20))
        bSpacer2.grid(row=0, column= 1)

        bSpacer3 = tk.Label(self, text="=============", font=('Helvetica bold',20))
        bSpacer3.grid(row=0, column= 3)

        # Adds a space between buttons and Headline
        bSpacer1 = tk.Label(self, text="     ", font=('Helvetica bold',20))
        bSpacer1.grid(row=2, column=2)

def ButtonPress(Name, Speed):
    global File
    File = Name
    global FRAME_REPEAT
    FRAME_REPEAT = Speed
    global Displaying
    Displaying = True
    global Reset
    Reset = True

def BackButton(Page):
    app.switch_frame(Page)
    global Displaying
    Displaying = False

if __name__ == "__main__":
    app = SampleApp()
    app.title("Virtual Matrix")
    app.geometry('600x400')
    #app.mainloop()

    while True:
        Displaying = False
        app.update_idletasks()
        app.update()


        # Get Picture Data
        #File = "Pac-Man Eating"                                  #change from button
        path = "/home/pi/Matrix Project/Pictures/" + File
        DISPLAY_FRAMES = len(os.listdir(path))





        # Load animation image files.                            #change to look for images in right folder
        FrameImage = []
        for pict in sorted(os.listdir(path)):
            FrameImage.append(pygame.image.load(f"Pictures/{File}/{pict}"))


        # Load a display frames from images.                     #attempt to include intermediate colors
        DisplayImage = []
        for Frame in range(DISPLAY_FRAMES):
            DisplayImage.append([])
            for Row in range(DISPLAY_ROWS):
                DisplayImage[Frame].append([])
                for Col in range(DISPLAY_COLS):
                    DisplayImage[Frame][Row].append([])
                    ColourValue = FrameImage[Frame].get_at((Col, Row))
                    DisplayImage[Frame][Row][Col].append(ColourValue[0] & 0x80)
                    DisplayImage[Frame][Row][Col].append(ColourValue[1] & 0x80)
                    DisplayImage[Frame][Row][Col].append(ColourValue[2] & 0x80)

        # Loop forever.
        Frame = 0
        FrameRepeat = FRAME_REPEAT
        Reset = False
        while Displaying and not Reset:
            FrameRepeat -= 1
            if FrameRepeat < 1:
                FrameRepeat = FRAME_REPEAT
                Frame += 1
                if Frame >= DISPLAY_FRAMES:
                    Frame = 0

            # Update LED Matrix.
            for Row in range(int(DISPLAY_ROWS / 2)):
                # Select row to dispaly.
                RPi.GPIO.output(pin_A, Row & 1)
                RPi.GPIO.output(pin_B, Row & 2)
                RPi.GPIO.output(pin_C, Row & 4)

                SelRow = Row + 1
                if SelRow > (DISPLAY_ROWS / 2) - 1:
                    SelRow = 0
                for Col in range(DISPLAY_COLS):
                    # Load bits into top row set.
                    RPi.GPIO.output(pin_R1, DisplayImage[Frame][SelRow][Col][RED])
                    RPi.GPIO.output(pin_G1, DisplayImage[Frame][SelRow][Col][GREEN])
                    RPi.GPIO.output(pin_B1, DisplayImage[Frame][SelRow][Col][BLUE])

                    # Load bits into bottom row set.
                    RPi.GPIO.output(pin_R2, DisplayImage[Frame][SelRow + 8][Col][RED])
                    RPi.GPIO.output(pin_G2, DisplayImage[Frame][SelRow + 8][Col][GREEN])
                    RPi.GPIO.output(pin_B2, DisplayImage[Frame][SelRow + 8][Col][BLUE])

                    # While clocking in new bit data.
                    # Refresh existing display data on the current output row.
                    RPi.GPIO.output(pin_OE, 0)
                    RPi.GPIO.output(pin_Clock, 1)
                    RPi.GPIO.output(pin_OE, 1)
                    RPi.GPIO.output(pin_Clock, 0)

                # When a pair of rows of display bits has been loaded.
                # Latch the data into the output buffer.
                RPi.GPIO.output(pin_Latch, 1)
                RPi.GPIO.output(pin_Latch, 0)

                app.update_idletasks()
                app.update()
        






