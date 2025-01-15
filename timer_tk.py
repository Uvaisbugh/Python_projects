import tkinter as tk
import time

class TimerApp:
    def __init__(self, root):

        """
        Initialize the TimerApp instance with a root tkinter window.

        This sets up the UI elements for the timer, including a time label, start button, pause button, resume button, and reset button.

        Parameters
        ----------
        root : tkinter.Tk
            The root window for the timer app.

        """
        self.root = root
        self.root.title("Timer")
        
        self.time_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
        self.time_label.pack()
        
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT)
        
        self.resume_button = tk.Button(root, text="Resume", command=self.resume_timer)
        self.resume_button.pack(side=tk.LEFT)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT)
        
        self.running = False
        self.paused = False
        self.start_time = 0
        self.elapsed_time = 0
        
    def update_timer(self):
        """
        Update the time label with the elapsed time if the timer is running and not paused.

        Updates the time label with the elapsed time in the format MM:SS. If the timer is
        running and not paused, it calls itself after 1000 milliseconds to update the time
        label again.
        """
        if self.running and not self.paused:
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(self.elapsed_time), 60)
            self.time_label.config(text=f"{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_timer)

    def start_timer(self):
        """
        Start the timer if it is not running.

        If the timer is not running, start the timer by setting the running flag to
        True and calling the update_timer method to update the time label.
        """
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_timer()

    def pause_timer(self):
        """
        Pause the timer if it is running.

        If the timer is running and not paused, pause the timer by setting the
        paused flag to True.
        """
        if self.running and not self.paused:
            self.paused = True

    def resume_timer(self):
        """
        Resume the timer if it is paused.

        If the timer is running and paused, resume the timer by setting the
        paused flag to False and calling the update_timer method to
        continue the timer.
        """
        if self.running and self.paused:
            self.paused = False
            self.update_timer()

    def reset_timer(self):

        """
        Reset the timer to its initial state.

        Reset the timer by setting the running flag to False, the paused flag
        to False, and the elapsed time to 0. Set the time label to "00:00".
        """
        self.running = False
        self.paused = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
