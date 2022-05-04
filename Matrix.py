import time
import random
import pygame
import RPi.GPIO
import os, os.path


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
FRAME_REPEAT = 50                                        #set from animation file?
DISPLAY_FRAMES = 4                                       #will change with length of animation
DISPLAY_COLS = 32
DISPLAY_ROWS = 16


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

# Load animation image files.                            #change to look for images in right folder
FrameImage = []
FrameImage.append(pygame.image.load("LaTechLogo1.png"))
FrameImage.append(pygame.image.load("LaTechLogo2.png"))
FrameImage.append(pygame.image.load("LaTechLogo3.png"))
FrameImage.append(pygame.image.load("LaTechLogo4.png"))
FrameImage.append(pygame.image.load("LaTechLogo5.png"))

for pict in os.listdir("."):
   print(pict)

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
FrameDirection = 1
FrameRepeat = FRAME_REPEAT
while True:
   # Animate display frames.
   FrameRepeat -= 1
   if FrameRepeat < 1:
      FrameRepeat = FRAME_REPEAT
      Frame += FrameDirection
      if Frame < 1 or Frame >= DISPLAY_FRAMES - 1:
         FrameDirection *= -1

   # Update LED Matrix.
   for Row in range(int(DISPLAY_ROWS / 2)):
      # Select row to dispaly.
      RPi.GPIO.output(pin_A, Row & 1)
      RPi.GPIO.output(pin_B, Row & 2)
      RPi.GPIO.output(pin_C, Row & 4)
#      RPi.GPIO.output(HUB75E_D, Row & 8)
#      RPi.GPIO.output(HUB75E_E, Row & 16)

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
