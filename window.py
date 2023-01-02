from tkinter import *
from snake import *


class Window:

    
    def __init__(self, width, height, refresh_rate=1000):
        self._root = Tk()
        self._root.title("Snake")
        self._refresh_rate = refresh_rate
        self._canvas = Canvas(self._root, width=width, height=height, bg="white")
        self._canvas.pack(pady=20, padx=20)

        # Make the snake
        self.snake = Snake(self._canvas, width, height)

        # Buttons
        button_quit = Button(self._root, text="exit", command=self._root.quit)
        button_quit.pack()
        button_test_grow = Button(self._root, text="GROW", command=self._test_grow)
        button_test_grow.pack()

        # Key bindings for input (has caps too just in case)
        # Up
        self._root.bind("<Key-Up>", self.direction_input)
        self._root.bind("<Key-w>", self.direction_input)
        self._root.bind("<Key-W>", self.direction_input)
        # Down
        self._root.bind("<Key-Down>", self.direction_input)
        self._root.bind("<Key-s>", self.direction_input)
        self._root.bind("<Key-S>", self.direction_input)
        # Left
        self._root.bind("<Key-Left>", self.direction_input)
        self._root.bind("<Key-a>", self.direction_input)
        self._root.bind("<Key-A>", self.direction_input)
        # Right
        self._root.bind("<Key-Right>", self.direction_input)
        self._root.bind("<Key-d>", self.direction_input)
        self._root.bind("<Key-D>", self.direction_input)

        # Frame loop and mainloop
        self._root.after(self._refresh_rate, self.refresh)
        self._root.mainloop()

    def _test_grow(self):
        self.snake.grow()

    def direction_input(self, event):
        direction = event.keysym

        if direction == "w" or direction == 'W':
            direction = "Up"
        elif direction == "s" or direction == 'S':
            direction = "Down"
        elif direction == "a" or direction == "A":
            direction = "Left"
        elif direction == "d" or direction == "D":
            direction = "Right"

        self.snake.change_direction(direction)

    """
    Snake moves in its current direction every frame
    """
    def refresh(self):
        print("Frame Update")
        self.snake.move() 
        
        # Recurive loop to load next frame
        self._root.after(self._refresh_rate, self.refresh)