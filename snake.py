class Snake:

    def __init__(self, canvas, max_x, max_y):
        self._canvas = canvas
        self._body = []
        self._head = None
        self._tail = None # does it need a tail??
        self._direction = "Down"

        # Create the snake
        next_seg = 0
        for i in range(2):
            self._body.append(Segment(300, 100+next_seg, self._canvas, max_x, max_y, i))
            next_seg += 20

        self._head = self._body[0]

    def move(self):
        self._head.move(self._direction)


    def move_body(self, direction):
        pass
        # move each segment into the position the segment in front was in
    """
    Changes the current direction so the next frame will move that way
    moves in the last (allowed) direction entered
    """
    def change_direction(self, new_direction):
        if new_direction == "Down" and self._direction == "Up":
            return
        elif new_direction == "Up" and self._direction == "Down":
            return
        elif new_direction == "Left" and self._direction == "Right":
            return
        elif new_direction == "Right" and self._direction == "Left":
            return

        self._direction = new_direction


class Segment:

    _SIZE = 20
    _COLOUR = "black"

    def __init__(self, x, y, canvas, max_x, max_y, index): # x and y position of top left corner
        # x and y is the top left corner of the segment (square)
        self._x = x
        self._y = y
        self._canvas = canvas
        self._max_x = max_x
        self._max_y = max_y

        self.index = index
        self.old_x = x
        self.old_y = y

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


        


