import tkinter.messagebox
from tkinter import *
import time


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
        self.timer_heading = Label(text='Timer', bg='#F7F6BB', fg='#87A922', font=('Courier', 30, "bold"))
        self.timer_heading.grid(column=1, row=0)
        # Create the time text (minutes:seconds)
        self.time_text = self.canvas.create_text(100, 130, text='00:00', fill='#114232', font=('Courier', 20, "bold"))
        self.canvas.grid(column=1, row=1)
        # Create the start button
        self.start_button = Button(master=self.root, text='Start', command=self.start_timer)
        self.start_button.grid(column=0, row=2)
        # Create the stop button
        # Initialize in disabled state (timer is static)
        self.stop_button = Button(master=self.root, text='Stop', state='disabled', command=self.stop_timer)
        self.stop_button.grid(column=2, row=2)
        # Create the reset button
        self.reset_button = Button(master=self.root, text='Reset', command=self.reset_timer)
        self.reset_button.grid(column=1, row=4)

        self.active = False  # Boolean to determine if the clock is counting or not
        self.session_count = 0  # Number of completed sessions
        self.FOCUS_DURATION = 25 * 60  # Number of minutes to focus per cycle (in seconds)
        self.BREAK_DURATION = 5 * 60  # Number of minutes for break per cycle (in seconds)
        self.SESSIONS = 4  # Chosen default number of focus sessions
        self.root.mainloop()  # Keep the window open (run the GUI)

    def start_timer(self):
        """Starts the timer"""
        self.active = True
        self.start_button.config(state='disabled')  # Disable the start button because timer has started
        self.stop_button.config(state='normal')  # Enable the stop button
        self.run_sessions()

    def stop_timer(self):
        """Stops the timer from counting"""
        self.active = False
        self.start_button.config(state='normal')  # Enable the start button
        self.stop_button.config(state='disable')  # Disable the stop button

    def run_sessions(self):
        """Runs the focus and rest sessions of the timer"""
        if self.session_count < self.SESSIONS:
            self.session_count += 1  # Increase number of completed sessions by 1
            self.timer_heading.config(text='Focus')  # Change the timer heading to display 'focus'
            self.countdown(self.FOCUS_DURATION)
            self.timer_heading.config(text='Break')  # Change the timer heading to display 'break'
            self.countdown(self.BREAK_DURATION)
            self.run_sessions()  # Run the next session
        else:
            self.session_count = 0
            tkinter.messagebox.showinfo(title='Focus Timer', message='All sessions completed')
            self.timer_heading.config(text='Timer')  # Return timer heading to display 'timer'
            self.stop_timer()  # Stop the timer

    def countdown(self, duration):
        """Initializes the countdown functionality for a specified duration"""
        while duration > 0 and self.active:
            minutes, seconds = divmod(duration, 60)  # Get the number of minutes and seconds
            time_string = "{:02d}:{:02d}".format(minutes, seconds)  # The string for the countdown
            self.canvas.itemconfig(self.time_text, text=time_string)
            self.root.update()  # Update the window to show countdown sequence
            time.sleep(1)  # Wait for a second
            duration -= 1  # Reduce the duration by a second after every second

    def reset_timer(self):
        self.stop_timer()
        self.FOCUS_DURATION = 25 * 60
        self.canvas.itemconfig(self.time_text, text='00:00')
        self.timer_heading.config(text='Timer')
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
