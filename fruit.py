class Fruit:

    def __init__(self, canvas, size, colour, snake):
        self.x = 0
        self.y = 0
        self._size = size
        self._canvas = canvas
        self._colour = colour
        self._snake = snake

        self._rect_graphic = None
        self.spawn()

    def spawn(self):
        self._x, self._y = self._rand_x_y()

        if self._rect_graphic is not None:
            self._canvas.delete(self._rect_graphic)
        self._rect_graphic = self._canvas.create_rectangle(
            self.x, self.y, 
            self.x + self._size, self.y + self._size, 
            fill = self._colour)
    
    def _rand_x_y(self):
        x = 0
        y = 0

        # generate x and y and make sure the snake isnt on it
        
        return x, y