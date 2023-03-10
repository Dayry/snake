from tkinter import *
from snake import *
from fruit import Fruit


class Window:

    
    def __init__(self, width, height, refresh_rate=1000):
        self._root = Tk()
        self._root.title("Snake")
        self._refresh_rate = refresh_rate
        self.canvas = Canvas(self._root, width=width, height=height, bg="white")
        self.width = width
        self.height = height
        self.size = 20
        self.score = 0

        # Label
        self.score_label_var = StringVar()
        self.score_label_var.set(f"Score: {self.score}")
        self.score_label = Label(self._root, textvariable = self.score_label_var)
        self.score_label.pack()

        self.canvas.pack(pady=20, padx=20)

        # Make the snake and spawn first fruit
        self.snake = Snake(self.canvas, self.width, self.height, self.size, "black")
        self.fruit = Fruit(self.canvas, self.size, "blue", self.width, self.height, self.snake)

        # Buttons
        button_new_game = Button(self._root, text="New Game", command=self.reset)
        button_new_game.pack()
        button_quit = Button(self._root, text="exit", command=self._root.quit)
        button_quit.pack()

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
        if self.fruit.did_snake_hit():
            self.score += 10
            self.score_label_var.set(f"Score: {self.score}")
        if self.snake.check_self_collision():
            self.reset()
            self.score = 0
            self.score_label_var.set(f"Score: {self.score}")
        
        # Recurive loop to load next frame
        self._root.after(self._refresh_rate, self.refresh)

    """
    Delete current graphical represention of snake and fruit, then reassign the
    variables of each.
    """
    def reset(self):
        # Clear the canvas, spawn new fruit and snake
        self.canvas.delete("all")

        self.snake = Snake(self.canvas, self.width, self.height, self.size, "black")
        self.fruit = Fruit(self.canvas, self.size, "blue", self.width, self.height, self.snake)
