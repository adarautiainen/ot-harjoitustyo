from tkinter import Tk
from user_interface.ui import UI

def main():
    window = Tk()
    window.title("Budget application")
    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()