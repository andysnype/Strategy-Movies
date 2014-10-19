import GenSched
from tkinter import *
print("hi")

class Manager:
	def __init__(self, box):
		buttons = {
			"Reserve": self.onclickReserve
			"Quit": self.onclickQuit
		}

		frame1 = Frame(box)
		frame1.pack()

		lblName = label(frame1, text="Type Name")


if __name__ == "__main__":
	window = Tk()
	Manager(window)
	window.mainloop()
