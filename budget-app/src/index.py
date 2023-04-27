import tkinter as tk
from user_interface.ui import UI


def main():
    window = tk.Tk()
    window.title("Budget application")

    window.geometry("500x700")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
