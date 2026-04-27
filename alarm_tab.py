import tkinter as tk
from tkinter import messagebox
import time
import winsound


class AlarmTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, padx=16, pady=16)

        self.active = False
        self.time_set = None
        self.sound_repetitions = 4

        self.title_label = tk.Label(
            self.frame,
            text="Alarm",
            font=("Helvetica", 14, "bold"),
        )
        self.title_label.pack(pady=(10, 6))

        instruction = tk.Label(self.frame, text="Set an alarm using 24-hour format (HH:MM):", font=("Arial", 12))
        instruction.pack(pady=20)

        self.entry = tk.Entry(self.frame, font=("Arial", 18), justify='center', width=10)
        self.entry.pack()

        self.status_label = tk.Label(self.frame, text="No alarm scheduled.", fg="gray", font=("Arial", 12))
        self.status_label.pack(pady=20)

        self.btn_set = tk.Button(self.frame, text="Set Alarm", command=self.set_alarm)
        self.btn_set.pack()

    def set_alarm(self):
        alarm_input = self.entry.get().strip()
        if self.is_valid_time(alarm_input):
            self.time_set = alarm_input
            self.active = True
            self.status_label.config(text=f"Alarm scheduled for {self.time_set}.", fg="green")
            return

        messagebox.showwarning("Format Error", "Use HH:MM format in 24-hour time, for example 14:30.")

    def update_logic(self):
        if self.active and self.time_set:
            current_time_str = time.strftime("%H:%M")
            if current_time_str == self.time_set:
                self.active = False
                self.status_label.config(text="No alarm scheduled.", fg="gray")
                self.entry.delete(0, tk.END)
                self.play_alarm_sound()
                messagebox.showinfo("Alarm", "The scheduled alarm time has been reached.")

    @staticmethod
    def is_valid_time(value):
        parts = value.split(":")
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            return False

        hour, minute = (int(part) for part in parts)
        return 0 <= hour <= 23 and 0 <= minute <= 59

    def play_alarm_sound(self):
        for _ in range(self.sound_repetitions):
            try:
                winsound.Beep(1000, 350)
                time.sleep(0.1)
            except RuntimeError:
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
