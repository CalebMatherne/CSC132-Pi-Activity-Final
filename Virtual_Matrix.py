Window_Size = [32,20]
Matrix_Size = [32,16]

from Characters import *
from tkinter import *

class MainGUI(Frame):
	# the constructor
	def __init__(self, parent):
		Frame.__init__(self, parent, bg="white")
		self.setupGUI()
    
    # sets up the GUI
	def setupGUI(self):

		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=3)

		# title
		self.title = Label(self, text="Title")
		self.title.grid(column=0, row=0, columnspan=8, rowspan=4, sticky=N)

		self.change_mode = Label(self, text="Change Mode")
		self.change_mode.grid(column=9, row=0, columnspan=8, rowspan=4, sticky=N)

		self.pack(fill=BOTH, expand=1)

		# self.columnconfigure(3,weight=3)
		# self.rowconfigure(3,weight=3)
		# for row in range(Window_Size[1]):
		# 	for column in range(Window_Size[0]):
		# 		if (row < 4):						# top portion
		# 			color = "#404040"
		# 			self.title = Label(self, width=16, height=4, bg=color, text="TITLE")
		# 			self.title.grid(column=0, row=0, columnspan=1, rowspan=4, sticky=N)
		# 		else:								# display portion
		# 			if FullFrame[row-4][column+0] == 1:
		# 				color = "#ffffff"
		# 			else:
		# 				color = "#000000"
		# 			self.l1 = Label(self, height=1, width=2, bg=color)
		# 			self.l1.grid(row = row, column = column+4, sticky = S)
		# 			self.pack(fill=BOTH, expand=1)
				




FullFrame = StringToData("testing")
for i in range(16):
	print(FullFrame[i])

# create the window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()

