class Snake:

    def __init__(self, canvas, max_x, max_y):
        self._canvas = canvas
        self._head = None
        self._tail = None
        self._body = []

        self.size = 20
        for i in range(5):
            self._body.append(Segment(300, 100+self.size, self._canvas, max_x, max_y))
            self.size += 20

    def move(self, direction):
        for seg in self._body:
            seg.move(direction)


class Segment:

    _SIZE = 20
    _COLOUR = "black"

    def __init__(self, x, y, canvas, max_x, max_y): # x and y position of top left corner
        self._x = x
        self._y = y
        self._canvas = canvas
        self._max_x = max_x
        self._max_y = max_y

        # make create rec method
        self._rect_graphic = self._canvas.create_rectangle(
            self._x, self._y, 
            self._x + Segment._SIZE, self._y + Segment._SIZE, 
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

        self._check_boundary(direction)

        self._canvas.delete(self._rect_graphic)
        self._rect_graphic = self._canvas.create_rectangle(
            self._x, self._y, 
            self._x + Segment._SIZE, self._y + Segment._SIZE, 
            fill = Segment._COLOUR)

    def _check_boundary(self, direction):
        if direction == "up":
            if self._y < 0:
                self._y = self._max_y - Segment._SIZE
        elif direction == "down":
            if self._y > self._max_y - Segment._SIZE:
                self._y = 0
        
        elif direction == "left":
            if self._x < 0:
                self._x = self._max_x - Segment._SIZE
        elif direction == "right":
            if self._x > self._max_x - Segment._SIZE:
                self._x = 0


        if self._x >= self._max_x:
            self._x = 0
        if self._x < 0:
            self._x = self._max_x

        


