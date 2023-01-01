from tkinter import *
from snake import *


class Window:

    
    def __init__(self, width, height, refresh_rate=1000):
        self._root = Tk()
        self._root.title("Snake")
        self._refresh_rate = refresh_rate

        self._canvas = Canvas(self._root, width=width, height=height, bg="white")
        self._canvas.pack()

        self.snake = Snake(self._canvas, width, height)

        button_quit = Button(self._root, text="exit", command=self._root.quit)
        button_quit.pack()

        self._root.after(self._refresh_rate, self.refresh)
        self._root.mainloop()

    def refresh(self):
        print("Frame Update") # this should call something to update the snake
        self.snake.move("down")
        

        # every refresh:
            # draw all parts of the snake at their current locations
            # draw fruit at its current location
            # snake.refresh() ??
            # fruit.refresh() ??
            # but then window would need access to snake and fruit hmm
            # I can just pass snake and fruit to window i guess but 
            # window has to passed to segments ( and therefore snake)
            # for them get drawn hmmmmmmm
        self._root.after(self._refresh_rate, self.refresh)