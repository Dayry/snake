class Snake:

    def __init__(self):
        pass


class Segment:

    _SIZE = 20
    _COLOUR = "black"

    def __init__(self, x, y, canvas, max_x, max_y): # x and y position of top left corner
        self._x = x
        self._y = y
        self._canvas = canvas
        self._max_x = max_x
        self._max_y = max_y

        self._rect_graphic = self._canvas.create_rectangle(
            self._x, self._y, 
            self._x + Segment._SIZE, self._y - Segment._SIZE, 
            fill = Segment._COLOUR)

    """ 
    moves the segment in the currect direction and updates its x and y
        
    """
    def move(self, direction):
        if direction == "up":
            self._y -= Segment._SIZE
        elif direction == "down":
            self._y += Segment._SIZE
        elif direction == "left":
            self._x -= Segment._SIZE
        elif direction == "right":
            self._x += Segment._SIZE

        self._check_boundary()

        self._canvas.delete(self._rect_graphic)
        self._rect_graphic = self._canvas.create_rectangle(
            self._x, self._y, 
            self._x + Segment._SIZE, self._y - Segment._SIZE, 
            fill = Segment._COLOUR)

    def _check_boundary(self):
        if self._x >= self._max_x:
            self._x = 0
        if self._x < 0:
            self._x = self._max_x

        if self._y >= self._max_y:
            self._y = 0
        if self._y < 0:
            self._y = self._max_y


