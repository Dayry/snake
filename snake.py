class Snake:

    def __init__(self, canvas, max_x, max_y):
        self._canvas = canvas
        self._body = []
        self._head = None
        self._tail = None # does it need a tail??
        self._direction = "Down"

        # Create the snake
        next_seg = 0
        for i in range(1):
            self._body.append(Segment(300, 100+next_seg, self._canvas, max_x, max_y))
            next_seg += 20

        self._head = self._body[0]

    def move(self):
        self._head.move(self._direction)
        # move_body     

    def move_body_r(self, direction):
        pass
        # move each segment into the position the segment in front was in
    """
    Changes the current direction so the next frame will move that way
    moves in the last (allowed) direction entered
    """
    def change_direction(self, direction):
        # if current direction is up, can't move down vv
        # if current direction is left, can't move right vv
        self._direction = direction


class Segment:

    _SIZE = 20
    _COLOUR = "black"

    def __init__(self, x, y, canvas, max_x, max_y): # x and y position of top left corner
        # x and y is the top left corner of the segment (square)
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
    Deletes the graphical representation of the segment on the canvas and
    redraws it in the new position   
    """
    def move(self, direction):
        if direction == "Up":
            self._y -= Segment._SIZE
        elif direction == "Down":
            self._y += Segment._SIZE
        elif direction == "Left":
            self._x -= Segment._SIZE
        elif direction == "Right":
            self._x += Segment._SIZE

        self._check_boundary(direction)

        self._canvas.delete(self._rect_graphic)
        self._rect_graphic = self._canvas.create_rectangle(
            self._x, self._y, 
            self._x + Segment._SIZE, self._y + Segment._SIZE, 
            fill = Segment._COLOUR)

    """
    Makes the canvas wrap left right up down
    """
    def _check_boundary(self, direction):
        if direction == "Up":
            if self._y < 0:
                self._y = self._max_y - Segment._SIZE
        elif direction == "Down":
            if self._y > self._max_y - Segment._SIZE:
                self._y = 0
        
        elif direction == "Left":
            if self._x < 0:
                self._x = self._max_x - Segment._SIZE
        elif direction == "Right":
            if self._x > self._max_x - Segment._SIZE:
                self._x = 0


        


