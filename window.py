from tkinter import *


class Window:

    
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Snake")

        self._canvas = Canvas(self._root, width=width, height=height, bg="white")
        self._canvas.pack()

        button_quit = Button(self._root, text="exit", command=self._root.quit)
        button_quit.pack()

        self._canvas.after(5000, self._root.quit)
        # replace quit with update_frame() i.e move in curr direction, remove tail etc

        self._root.mainloop()