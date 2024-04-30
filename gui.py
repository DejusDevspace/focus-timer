from tkinter import *
# from PIL import Image, ImageTk


class Clock:
    def __init__(self):
        self.root = Tk()  # Initialize the tkinter window
        self.root.title('Focus Timer')  # Create the title of the window
        self.root.config(padx=50, pady=50, bg='#F7F6BB')
        clock_image = PhotoImage(file='./images/clock-image.png')  # Load the clock image in directory
        # Create a canvas and place the image on the canvas
        self.canvas = Canvas(master=self.root, width=200, height=230, bg='#F7F6BB', highlightthickness=0)
        self.canvas.create_image(100, 115, image=clock_image)
        # Create the text above the clock image
        self.timer_text = Label(text='Timer', bg='#F7F6BB', fg='#87A922', font=('Courier', 30, "bold"))
        self.timer_text.grid(column=1, row=0)
        # Create the time text (minutes:seconds)
        self.time_text = self.canvas.create_text(100, 130, text='00:00', fill='#114232', font=('Courier', 20, "bold"))
        self.canvas.grid(column=1, row=1)
        # Create the start button
        self.start_button = Button(master=self.root, text='Start')
        self.start_button.grid(column=0, row=2)
        # Create the stop button
        self.stop_button = Button(master=self.root, text='Stop')
        self.stop_button.grid(column=2, row=2)
        # Create the reset button
        self.reset_button = Button(master=self.root, text='Reset')
        self.reset_button.grid(column=1, row=4)

        self.root.mainloop()  # Keep the window open (run the GUI)
