class Snake:

    def __init__(self):


class Segment:

    _SIZE = 5
    _COLOUR = "black"

    def __init__(self, x, y, canvas): # x and y position of top left corner
        self._x = x
        self._y = y
        self._rect_graphic = canvas.create_rectangle(self._x, self._y, self._x + _SIZE, self._y - _SIZE, fill = _COLOUR)
        self._canvas = canvas

    """ 
    moves the segment in the currect direction and updates its x and y
        
    """
    def move(self, direction):
        new_x = self._x
        new_y = self._y

        if direction == "up":
            new_y = self._y + _SIZE
        elif direction == "down":
            new_y = self._y - _SIZE
        elif direction == "left":
            new_x = self._x - _SIZE
        elif direction == "right":
            new_x = self._x + _SIZE

        self._canvas.move(self._rect_graphic, new_x, new_y)
        self._x = new_x
        self._y = new_y


