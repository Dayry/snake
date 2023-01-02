import random

class Fruit:

    def __init__(self, canvas, size, colour, width, height, snake):
        self._size = size
        self._canvas = canvas
        self._colour = colour
        self._snake = snake
        self._width = width
        self._height = height
        self._rect_graphic = None

        self.x = 0
        self.y = 0
        self.spawn()

    def spawn(self):
        self.x, self.y = self._rand_x_y()
        print(self.x, self.y)

        if self._rect_graphic is not None:
            self._canvas.delete(self._rect_graphic)
        self._rect_graphic = self._canvas.create_rectangle(
            self.x, self.y, 
            self.x + self._size, self.y + self._size, 
            fill = self._colour)
    
    def _rand_x_y(self):
        x = 0
        y = 0
        overlap = True

        while overlap:
            x = random.randint(0, self._width - self._size)
            y = random.randint(0, self._height - self._size)

            # Check the fruit won't overlap the snake
            for seg in self._snake._body:
                if seg._x == x and seg._y == y:
                    continue
            overlap = False
        
        return x, y