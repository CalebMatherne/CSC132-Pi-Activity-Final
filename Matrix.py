import time
import random
import pygame
import RPi.GPIO


# GPIO pin assignments.
HUB75E_R1 = 17 # was 14
HUB75E_G1 = 18 # was 15
HUB75E_B1 = 22 # was 18
HUB75E_R2 = 23
HUB75E_G2 = 24
HUB75E_B2 = 25
# HUB75E_E = 8
HUB75E_A = 27 # was 7
HUB75E_B = 6 # was 12
HUB75E_C = 9 # was 16
#HUB75E_D = 20
HUB75E_CLK = 3 # was 21
HUB75E_LAT = 4 # was 26
HUB75E_OE = 2 # was 19

# Display properties.
RED = 0
GREEN = 1
BLUE = 2
FRAME_REPEAT = 50
DISPLAY_FRAMES = 4
DISPLAY_COLS = 32
DISPLAY_ROWS = 16


# PyGame used to read image files from storage.
pygame.init()

# Configure GPIO pins.
RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(HUB75E_R1, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_G1, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_B1, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_R2, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_G2, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_B2, RPi.GPIO.OUT, initial=0)
# RPi.GPIO.setup(HUB75E_E, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_A, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_B, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_C, RPi.GPIO.OUT, initial=0)
#RPi.GPIO.setup(HUB75E_D, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_CLK, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_LAT, RPi.GPIO.OUT, initial=0)
RPi.GPIO.setup(HUB75E_OE, RPi.GPIO.OUT, initial=1)

# Load animation image files.
FrameImage = []
FrameImage.append(pygame.image.load("LaTechLogo1.png"))
FrameImage.append(pygame.image.load("LaTechLogo2.png"))
FrameImage.append(pygame.image.load("LaTechLogo3.png"))
FrameImage.append(pygame.image.load("LaTechLogo4.png"))
FrameImage.append(pygame.image.load("LaTechLogo5.png"))

# Load a display frames from images.
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
      RPi.GPIO.output(HUB75E_A, Row & 1)
      RPi.GPIO.output(HUB75E_B, Row & 2)
      RPi.GPIO.output(HUB75E_C, Row & 4)
#      RPi.GPIO.output(HUB75E_D, Row & 8)
#      RPi.GPIO.output(HUB75E_E, Row & 16)

      SelRow = Row + 1
      if SelRow > (DISPLAY_ROWS / 2) - 1:
         SelRow = 0
      for Col in range(DISPLAY_COLS):
         # Load bits into top row set.
         RPi.GPIO.output(HUB75E_R1, DisplayImage[Frame][SelRow][Col][RED])
         RPi.GPIO.output(HUB75E_G1, DisplayImage[Frame][SelRow][Col][GREEN])
         RPi.GPIO.output(HUB75E_B1, DisplayImage[Frame][SelRow][Col][BLUE])

         # Load bits into bottom row set.
         RPi.GPIO.output(HUB75E_R2, DisplayImage[Frame][SelRow + 8][Col][RED])
         RPi.GPIO.output(HUB75E_G2, DisplayImage[Frame][SelRow + 8][Col][GREEN])
         RPi.GPIO.output(HUB75E_B2, DisplayImage[Frame][SelRow + 8][Col][BLUE])

         # While clocking in new bit data.
         # Refresh existing display data on the current output row.
         RPi.GPIO.output(HUB75E_OE, 0)
         RPi.GPIO.output(HUB75E_CLK, 1)
         RPi.GPIO.output(HUB75E_OE, 1)
         RPi.GPIO.output(HUB75E_CLK, 0)

      # When a pair of rows of display bits has been loaded.
      # Latch the data into the output buffer.
      RPi.GPIO.output(HUB75E_LAT, 1)
      RPi.GPIO.output(HUB75E_LAT, 0)
