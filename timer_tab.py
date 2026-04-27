import tkinter as tk
from tkinter import messagebox
import time


class TimerTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, padx=16, pady=16)

        self.running = False
        self.seconds_left = 0
        self.last_tick = time.time()

        self.title_label = tk.Label(
            self.frame,
            text="Countdown Timer",
            font=("Helvetica", 14, "bold"),
        )
        self.title_label.pack(pady=(10, 6))

        instruction = tk.Label(self.frame, text="Enter minutes to count down:", font=("Arial", 12))
        instruction.pack(pady=20)

        self.entry = tk.Entry(self.frame, font=("Arial", 18), justify='center', width=10)
        self.entry.insert(0, "1")
        self.entry.pack()

        self.time_label = tk.Label(self.frame, text="00:00", font=("Helvetica", 40))
        self.time_label.pack(pady=30)

        self.btn_start = tk.Button(self.frame, text="Start Timer", command=self.start)
        self.btn_start.pack()

    def start(self):
        try:
            minutes = float(self.entry.get())
            if minutes <= 0:
                raise ValueError
            self.seconds_left = int(minutes * 60)
            self.running = True
            self.time_label.config(text=self.format_time(self.seconds_left))
            self.entry.config(state="disabled")
            self.btn_start.config(state="disabled")
            self.last_tick = time.time()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number greater than zero.")

    def update_logic(self):
        if self.running:
            if time.time() - self.last_tick >= 1.0:
                self.seconds_left -= 1
                self.last_tick = time.time()

                if self.seconds_left > 0:
                    self.time_label.config(text=self.format_time(self.seconds_left))
                else:
                    self.running = False
                    self.time_label.config(text="00:00")
                    self.entry.config(state="normal")
                    self.btn_start.config(state="normal")
                    messagebox.showinfo("Timer", "Time is up.")

    @staticmethod
    def format_time(total_seconds):
        mins, secs = divmod(total_seconds, 60)
        return f"{mins:02}:{secs:02}"
