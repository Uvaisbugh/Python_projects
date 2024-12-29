'''def fibonacci_gen():
    a,b = 0,1
    while True:
        yield a
        a,b= b, a+b
        
fib=fibonacci_gen()
for _ in range(10):
    print(next(fib))
'''

import tkinter as tk
import time

class TimerApp:
    def __init__(self, root):
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
        if self.running and not self.paused:
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(self.elapsed_time), 60)
            self.time_label.config(text=f"{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_timer()

    def pause_timer(self):
        if self.running and not self.paused:
            self.paused = True

    def resume_timer(self):
        if self.running and self.paused:
            self.paused = False
            self.update_timer()

    def reset_timer(self):
        self.running = False
        self.paused = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
