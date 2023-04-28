import tkinter as tk
from tkinter import ttk
from user_interface.ui import UI


def main(window):
    container = ttk.Frame(window)
    container.grid(column=0, row=0, sticky="NSEW")

    canvas = tk.Canvas(container, highlightthickness=0)
    canvas.grid(column=0, row=0, sticky="NSEW")

    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.grid(column=1, row=0, sticky="NS")

    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def configure_scroll_region(_):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", configure_scroll_region)

    canvas.configure(yscrollcommand=scrollbar.set)

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    ui_view = UI(scrollable_frame)
    ui_view.start()


def initialize():
    window = tk.Tk()
    window.title("Budget application")
    window.geometry("500x700")

    main(window)

    window.mainloop()


if __name__ == "__main__":
    initialize()
