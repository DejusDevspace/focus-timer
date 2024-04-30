from tkinter import *
# from PIL import Image, ImageTk


class Clock:
    def __init__(self):
        self.root = Tk()  # Initialize the tkinter window
        self.root.title('Focus Timer')  # Create the title of the window
        self.root.config(padx=50, pady=50, bg='black')
        clock_image = PhotoImage(file='./images/clock-image.png')
        self.canvas = Canvas(master=self.root, width=200, height=230, bg='black', highlightthickness=0)
        self.canvas.create_image(100, 115, image=clock_image)

        self.time_text = self.canvas.create_text(100, 130, text="00:00", fill="black", font=('Courier', 20, "bold"))
        self.canvas.grid(column=1, row=1)

        self.timer_text = Label(text="Timer", bg='black', fg='white', font=('Courier', 30, "bold"))
        self.timer_text.grid(column=1, row=0)

        self.root.mainloop()  # Keep the window open (run the GUI)
