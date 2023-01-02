class Fruit:

    def __init__(self, x, y, canvas, size, colour):
        self.x = x
        self.y = y
        self._size = size
        self._canvas = canvas
        self._colour = colour

        self._rect_graphic = self._canvas.create_rectangle(
            self.x, self.y, 
            self.x + self._size, self.y + self._size, 
            fill = self._colour)

    def spawn(self, x, y):
        self._x = x
        self._y = y

        self._canvas.delete(self._rect_graphic)
        self._rect_graphic = self._canvas.create_rectangle(
            self.x, self.y, 
            self.x + self._size, self.y + self._size, 
            fill = self._colour)
