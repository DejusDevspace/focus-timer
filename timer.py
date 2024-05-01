from tkinter import *
import time


FOCUS_DURATION = 25 * 60  # Number of minutes to focus per cycle (in seconds)
BREAK_DURATION = 5 * 60  # Number of minutes for break per cycle (in seconds)
SESSIONS = 4  # Chosen default number of focus sessions


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
        self.stop_button = Button(master=self.root, text='Stop', state='disabled')  # Disabled (timer is static)
        self.stop_button.grid(column=2, row=2)
        # Create the reset button
        self.reset_button = Button(master=self.root, text='Reset')
        self.reset_button.grid(column=1, row=4)

        self.active = False  # Boolean to determine if the clock is counting or not
        self.session_count = 0  # Number of completed sessions
        self.root.mainloop()  # Keep the window open (run the GUI)

    def start_timer(self):
        self.active = True
        self.start_button.config(state='disabled')  # Disable the start button because timer has started
        self.stop_button.config(state='normal')  # Enable the stop button
        self.run_sessions()

    def stop_timer(self):
        self.active = False
        self.start_button.config(state='normal')  # Enable the start button
        self.stop_button.config(state='disable')  # Disable the stop button

    def run_sessions(self):
        if self.session_count < SESSIONS:
            self.session_count += 1
            self.timer_text.config(text='Focus')
            self.countdown(FOCUS_DURATION)
            self.timer_text.config(text='Break')
            self.countdown(BREAK_DURATION)
            self.run_sessions()
        else:
            self.session_count = 0
            messagebox.showinfo("Focus Timer", "All sessions completed!")
            self.label.config(text="")
            self.stop_timer()
    def countdown(self, duration):
        pass
