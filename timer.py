import tkinter.messagebox
from tkinter import *
import time
import pygame

NO_OF_SESSIONS = 4
FOCUS_DURATION = 25  # In minutes
BREAK_DURATION = 5


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
        # Create the reset button
        self.reset_button = Button(master=self.root, text='Reset', command=self.reset_timer, state='disabled')
        self.reset_button.grid(column=2, row=2)
        # Create text to show the current session
        self.current_session = Label(master=self.root, text='Session: 0', bg='#F7F6BB', fg='#114232',
                                     font=('Courier', 13, 'bold'))
        self.current_session.grid(column=1, row=3)
        # -------------------- CLOCK PARAMETERS -------------------- #
        self.active = None  # Boolean to determine if the clock is counting or not
        self.session_count = None  # Number of completed sessions
        self.FOCUS_DURATION = FOCUS_DURATION * 60  # Number of minutes to focus per cycle (in seconds)
        self.BREAK_DURATION = BREAK_DURATION * 60  # Number of minutes for break per cycle (in seconds)
        self.SESSIONS = NO_OF_SESSIONS  # Chosen default number of focus sessions
        self.mixer = pygame.mixer  # Create the mixer from pygame
        self.mixer.init()  # Initialize the mixer
        self.transition_sound = pygame.mixer.Sound('./sounds/clock_trans_sound.mp3')  # Path to the transition sound

        self.root.mainloop()  # Keep the window open (run the GUI)

    def start_timer(self):
        """Starts the timer"""
        self.active = True
        self.session_count = 0
        self.start_button.config(state='disabled')  # Disable the start button because timer has started
        self.reset_button.config(state='normal')  # Enable the stop button
        self.run_sessions()  # Call the run sessions function

    def run_sessions(self):
        """Runs the focus and rest sessions of the timer"""
        if self.active:
            if self.session_count < self.SESSIONS:
                self.session_count += 1  # Increase number of completed sessions by 1
                # Update the session number in the gui
                self.current_session.config(text='Session: {}/{}'.format(self.session_count, self.SESSIONS))
                if self.session_count == self.SESSIONS:  # Final session
                    self.timer_heading.config(text='Focus')  # Change the timer heading to display 'focus'
                    self.countdown(self.FOCUS_DURATION)  # No break at the final session
                    tkinter.messagebox.showinfo(title='Focus Timer', message='All sessions completed')
                    self.reset_timer()  # Reset the timer
                self.timer_heading.config(text='Focus')  # Change the timer heading to display 'focus'
                self.countdown(self.FOCUS_DURATION)
                self.timer_heading.config(text='Break')  # Change the timer heading to display 'break'
                self.countdown(self.BREAK_DURATION)
                self.run_sessions()  # Run the next session
        else:
            self.reset_timer()

    def countdown(self, duration):
        """Initializes the countdown functionality for a specified duration"""
        while duration > 0 and self.active:
            minutes, seconds = divmod(duration, 60)  # Get the number of minutes and seconds
            time_string = "{:02d}:{:02d}".format(int(minutes), int(seconds))  # The string for the countdown
            self.canvas.itemconfig(self.time_text, text=time_string)
            self.root.update()  # Update the window to show countdown sequence
            time.sleep(1)  # Wait for a second
            duration -= 1  # Reduce the duration by a second after every second
            if minutes == 0 and seconds == 1:
                channel = pygame.mixer.Channel(0)  # Create a channel for playing the sound
                channel.play(self.transition_sound)  # Play the transition sound through the channel
                time.sleep(3)  # Play the sound for three seconds

    def stop_countdown(self):
        self.active = False  # Stop the clock from counting
        self.timer_heading.config(text='Timer')  # Reset the heading of the clock
        self.canvas.itemconfig(self.time_text, text='00:00')  # Replace time text with 00:00
        self.current_session.config(text='Session: 0')  # Reset the number of sessions text

    def reset_timer(self):
        """Resets the timer and returns all setting to initial state"""
        self.stop_countdown()  # Call the stop countdown function
        self.start_button.config(state='normal')
        self.reset_button.config(state='disabled')  # Disable the reset button
