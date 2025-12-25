from tkinter import *

myWindow = Tk()
myWindow.title("Main window")
myWindow.geometry("300x200")

def open_new_window():
    new_window = Toplevel(myWindow)
    new_window.title("New window")
    new_window.geometry("250x150")

    btn = Button(
        new_window,
        text="Hi!Click.",
        command=lambda: print("clicked.")
    )
    btn.pack(pady=20)

main_button = Button(
    myWindow,
    text="Open new window",
    command=open_new_window
)
main_button.pack(pady=50)

myWindow.mainloop()
