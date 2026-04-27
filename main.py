import tkinter as tk
from tkinter import ttk

from clock_tab import AnalogClockTab
from stopwatch_tab import StopwatchTab
from timer_tab import TimerTab
from alarm_tab import AlarmTab


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Clock Workshop")
        self.root.geometry("470x560")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root, padx=12, pady=12)
        self.main_frame.pack(expand=True, fill="both")

        self.header_label = tk.Label(
            self.main_frame,
            text="Clock App with Python Frontend",
            font=("Helvetica", 16, "bold"),
        )
        self.header_label.pack(pady=(0, 4))

        self.subtitle_label = tk.Label(
            self.main_frame,
            text="Main clock plus stopwatch, timer and alarm tools.",
            font=("Helvetica", 10),
            fg="#444444",
        )
        self.subtitle_label.pack(pady=(0, 10))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(in_=self.main_frame, expand=True, fill="both")

        self.clock_app = AnalogClockTab(self.notebook)
        self.stopwatch_app = StopwatchTab(self.notebook)
        self.timer_app = TimerTab(self.notebook)
        self.alarm_app = AlarmTab(self.notebook)

        self.notebook.add(self.clock_app.frame, text="Clock")
        self.notebook.add(self.stopwatch_app.frame, text="Stopwatch")
        self.notebook.add(self.timer_app.frame, text="Timer")
        self.notebook.add(self.alarm_app.frame, text="Alarm")

        self.run_app_loop()

    def run_app_loop(self):
        self.clock_app.update_clock()
        self.stopwatch_app.update_logic()
        self.timer_app.update_logic()
        self.alarm_app.update_logic()

        self.root.after(100, self.run_app_loop)


if __name__ == "__main__":
    app_window = tk.Tk()
    MainApplication(app_window)
    app_window.mainloop()
