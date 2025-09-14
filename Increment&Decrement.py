import tkinter as tk
from tkinter import font

class FancyCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Fancy Counter ✨")
        self.root.geometry("400x300")
        self.root.config(bg="#1f1f2e")

        self.count = 0

        # Custom font
        self.custom_font = font.Font(family="Helvetica", size=48, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=14, weight="bold")

        # Counter label
        self.label = tk.Label(
            root,
            text=str(self.count),
            font=self.custom_font,
            fg="#00FFAB",
            bg="#1f1f2e"
        )
        self.label.pack(pady=50)

        # Buttons
        btn_frame = tk.Frame(root, bg="#1f1f2e")
        btn_frame.pack()

        self.decrement_btn = tk.Button(
            btn_frame,
            text="-",
            font=self.button_font,
            width=5,
            bg="#ff6b6b",
            fg="white",
            activebackground="#ff4b4b",
            command=self.decrement
        )
        self.decrement_btn.pack(side="left", padx=20)

        self.increment_btn = tk.Button(
            btn_frame,
            text="+",
            font=self.button_font,
            width=5,
            bg="#4ecdc4",
            fg="white",
            activebackground="#3cc4b2",
            command=self.increment
        )
        self.increment_btn.pack(side="right", padx=20)

        # Glow effect
        self.animate_label()

    def increment(self):
        self.count += 1
        self.update_ui()

    def decrement(self):
        self.count -= 1
        self.update_ui()

    def update_ui(self):
        self.label.config(text=str(self.count))
        self.label.config(fg="#FFD93D" if self.count % 2 == 0 else "#6BCB77")
        self.update_background()

    def update_background(self):
        if self.count < 0:
            bg_color = "#8B0000"  # dark red
        elif self.count > 0:
            bg_color = "#006400"  # dark green
        else:
            bg_color = "#1f1f2e"  # neutral

        # Update background color
        self.root.config(bg=bg_color)
        self.label.config(bg=bg_color)
        # Update button frame and button backgrounds to match
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.config(bg=bg_color)

    def animate_label(self):
        def pulse():
            current_color = self.label.cget("fg")
            new_color = "#FF6B6B" if current_color == "#00FFAB" else "#00FFAB"
            self.label.config(fg=new_color)
            self.root.after(1000, pulse)
        pulse()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FancyCounterApp(root)
    root.mainloop()
