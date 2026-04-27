import tkinter as tk
import math
import time


class AnalogClockTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, padx=10, pady=10)

        self.title_label = tk.Label(
            self.frame,
            text="Analog Clock",
            font=("Helvetica", 14, "bold"),
        )
        self.title_label.pack(pady=(0, 6))

        self.canvas_size = 400
        self.clock_canvas = tk.Canvas(self.frame, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.clock_canvas.pack(pady=20)

        self.center_x = self.canvas_size // 2
        self.center_y = self.canvas_size // 2
        self.clock_radius = 150

        self.digital_time_label = tk.Label(self.frame, text="", font=("Helvetica", 18, "bold"))
        self.digital_time_label.pack()

    def update_clock(self):
        self.clock_canvas.delete("all")

        self.clock_canvas.create_oval(
            self.center_x - self.clock_radius, self.center_y - self.clock_radius,
            self.center_x + self.clock_radius, self.center_y + self.clock_radius,
            width=4, outline="#333"
        )

        for i in range(60):
            angle = math.radians(i * 6 - 90)
            if i % 5 == 0:
                tick_length = 15
                tick_width = 3
            else:
                tick_length = 8
                tick_width = 1

            outer_x = self.center_x + self.clock_radius * math.cos(angle)
            outer_y = self.center_y + self.clock_radius * math.sin(angle)
            inner_x = self.center_x + (self.clock_radius - tick_length) * math.cos(angle)
            inner_y = self.center_y + (self.clock_radius - tick_length) * math.sin(angle)

            self.clock_canvas.create_line(inner_x, inner_y, outer_x, outer_y, width=tick_width, fill="#333")

        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            num_x = self.center_x + (self.clock_radius - 35) * math.cos(angle)
            num_y = self.center_y + (self.clock_radius - 35) * math.sin(angle)
            self.clock_canvas.create_text(num_x, num_y, text=str(i), font=("Arial", 14, "bold"))

        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        self.draw_hand(hours * 30 + (minutes / 2), self.clock_radius - 60, 6, "black")
        self.draw_hand(minutes * 6 + (seconds / 10), self.clock_radius - 40, 4, "blue")
        self.draw_hand(seconds * 6, self.clock_radius - 15, 2, "red")

        self.clock_canvas.create_oval(
            self.center_x - 6, self.center_y - 6,
            self.center_x + 6, self.center_y + 6,
            fill="black"
        )

        self.digital_time_label.config(text=time.strftime('%H:%M:%S'))

    def draw_hand(self, angle_degrees, length, width, color):
        angle_radians = math.radians(angle_degrees - 90)
        end_x = self.center_x + length * math.cos(angle_radians)
        end_y = self.center_y + length * math.sin(angle_radians)
        self.clock_canvas.create_line(
            self.center_x, self.center_y, end_x, end_y,
            width=width, fill=color, capstyle=tk.ROUND
        )
