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

import tkinter as tk

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
        l1= tk.Label(self, text="Choose A Group", font=('Helvetica bold',35))
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

        l1 = tk.Label(self, text="Pictures", font=('Helvetica bold',40))
        l1.grid(row=0, column=2)

        # Buttons
        b1 = tk.Button(self, text="<-- Back", font=('Helvetica bold', 20), command=lambda: master.switch_frame(StartPage))
        b1.grid(row=0, column=0)

        b2 = tk.Button(self, text="Microsoft Logo", font=('Helvetica bold',20))
        b2.grid(row=2, column=2, sticky='S')

        # Adds space between Buttons and Headline
        bSpacer4 = tk.Label(self, text=" ", font=('Helvetica bold',20))
        bSpacer4.grid(row=1, column= 0)

        # Adds a headline
        bSpacer2 = tk.Label(self, text="===============", font=('Helvetica bold',20))
        bSpacer2.grid(row=0, column= 1)

        bSpacer3 = tk.Label(self, text="===================", font=('Helvetica bold',20))
        bSpacer3.grid(row=0, column= 3)

### ANIMATIONS PAGE ###
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        l1 = tk.Label(self, text="Animations", font=('Helvetica bold',40)) # Page Topic
        l1.grid(row=0, column=2, sticky='N', pady=10)

        # Buttons for Animation page
        b1 = tk.Button(self, text="<-- Back", font=('Helvetica bold', 20), command=lambda: master.switch_frame(StartPage)) # returns to main screen
        b1.grid(row=0,column=0, sticky='W')

        b2 = tk.Button(self, text="Circles", font=('Helvetica bold',20)) # Will show Circles
        b2.grid(row=1, column=2, sticky='S')

        b3 = tk.Button(self, text="LaTech Logo", font=('Helvetica bold',20)) # Will show Latech Logo
        b3.grid(row=1, column=3, sticky='S')

        b4 = tk.Button(self, text="Mario", font=('Helvetica bold',20)) # Will show Mario
        b4.grid(row=1, column=1, sticky='S')

        b5 = tk.Button(self, text="Pac-Man", font=('Helvetica bold',20)) # Will show Pac-Man
        b5.grid(row=3, column=2, sticky='S')

        b6 = tk.Button(self, text="Rainbow Ripple", font=('Helvetica bold',20)) # Will show RainbowRipple
        b6.grid(row=3, column=3, sticky='S')

        # Adds a headline
        bSpacer2 = tk.Label(self, text="=============", font=('Helvetica bold',20))
        bSpacer2.grid(row=0, column= 1)

        bSpacer3 = tk.Label(self, text="=================", font=('Helvetica bold',20))
        bSpacer3.grid(row=0, column= 3)

        # Adds a space between buttons and Headline
        bSpacer1 = tk.Label(self, text="     ", font=('Helvetica bold',20))
        bSpacer1.grid(row=2, column=2)

if __name__ == "__main__":
    app = SampleApp()
    app.title("Virtual Matrix")
    app.geometry('900x420')
    app.mainloop()