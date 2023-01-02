class Snake:

    def __init__(self, canvas, max_x, max_y, size=20, colour="black"):
        self._canvas = canvas
        self._body = []
        self._head = None
        self._tail = None # does it need a tail??
        self._direction = "Down"
        self.size = size
        self.colour = colour

        # Create the snake
        next_seg = 0
        for i in range(5):
            self._body.append(Segment(300, 100+next_seg, self._canvas, max_x, max_y, i, self.size, self.colour))
            next_seg += 20

        self._head = self._body[0]

    """
        Moves head in current direction, all other segments move to the position the
        segment in front was in
    """
    def move(self):
        self._head.move_head(self._direction)
        for seg_index in range(1, len(self._body)):
            new_x = self._body[seg_index-1].old_x
            new_y = self._body[seg_index-1].old_y

            self._body[seg_index].move(self._direction, new_x, new_y)


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

    def __init__(self, x, y, canvas, max_x, max_y, index, size, colour): # x and y position of top left corner
        # x and y is the top left corner of the segment (square)
        self._x = x
        self._y = y
        self._canvas = canvas
        self._max_x = max_x
        self._max_y = max_y

        self.index = index
        self.old_x = x
        self.old_y = y
        self.size = size
        self.colour = colour

        # Include this in the move refactor
        self._rect_graphic = self._canvas.create_rectangle(
            self._x, self._y, 
            self._x + self.size, self._y + self.size, 
            fill = self.colour)

    """ 
    Special method just for moving the head segment
    Deletes the graphical representation of the segment on the canvas and
    redraws it in the new position   
    """
    def move_head(self, direction):
        self.old_x = self._x
        self.old_y = self._y

        if direction == "Up":
            self._y -= self.size
        elif direction == "Down":
            self._y += self.size
        elif direction == "Left":
            self._x -= self.size
        elif direction == "Right":
            self._x += self.size

        # This stuff will be done by all segments to refactor
        # in seg.move() too
        self._check_boundary(direction)

        self._canvas.delete(self._rect_graphic)
        self._rect_graphic = self._canvas.create_rectangle(
            self._x, self._y, 
            self._x + self.size, self._y + self.size, 
            fill = self.colour)

    """

    Deletes the graphical representation of the segment on the canvas and
    redraws it in the new position   
    """
    def move(self, direction, x, y):
        self.old_x = self._x
        self.old_y = self._y

        self._x = x
        self._y = y

        self._check_boundary(direction)

        self._canvas.delete(self._rect_graphic)
        self._rect_graphic = self._canvas.create_rectangle(
            self._x, self._y, 
            self._x + self.size, self._y + self.size, 
            fill = self.colour)



    """
    Makes the canvas wrap left right up down
    """
    def _check_boundary(self, direction):
        if direction == "Up":
            if self._y < 0:
                self._y = self._max_y - self.size
        elif direction == "Down":
            if self._y > self._max_y - self.size:
                self._y = 0
        
        elif direction == "Left":
            if self._x < 0:
                self._x = self._max_x - self.size
        elif direction == "Right":
            if self._x > self._max_x - self.size:
                self._x = 0


        


