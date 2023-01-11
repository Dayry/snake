class Snake:

    def __init__(self, canvas, max_x, max_y, size=20, colour="black"):
        self._canvas = canvas
        self.body = []
        self.head = None
        self.direction = "Up"       
        self.size = size
        self.colour = colour
        self.max_x = max_x
        self.max_y = max_y
        self._starting_segments = 5

        # Create the snake
        self._spawn()

    """
    Creates the segments of the snake and adds them to the body property.
    """
    def _spawn(self):
        start_x = self.max_x // 2
        start_y = self.max_y // 2
        for i in range(self._starting_segments):
            seg = Segment(start_x, start_y,
                self._canvas, self.max_x, self.max_y,
                self.size, self.colour)
            start_y += self.size
            self.body.append(seg)

        self.head = self.body[0]

    """
        Moves head in current direction, all other segments move to the position the
        segment in front was in
    """
    def move(self):
        self.head.movehead(self.direction)
        for seg_index in range(1, len(self.body)):
            new_x = self.body[seg_index-1].old_x
            new_y = self.body[seg_index-1].old_y

            self.body[seg_index].move(self.direction, new_x, new_y)

    """
    Changes the current direction so the next frame will move that way
    moves in the last (allowed) direction entered
    """
    def change_direction(self, newdirection):
        if newdirection == "Down" and self.direction == "Up":
            return
        elif newdirection == "Up" and self.direction == "Down":
            return
        elif newdirection == "Left" and self.direction == "Right":
            return
        elif newdirection == "Right" and self.direction == "Left":
            return

        self.direction = newdirection

    def grow(self):
        x = self.body[-1].old_x
        y = self.body[-1].old_y

        seg = Segment(x, y,
                self._canvas, self.max_x, self.max_y,
                self.size, self.colour)
        self.body.append(seg)

    def check_self_collision(self):
        head_x = self.head._x
        head_y = self.head._y
        for seg_index in range(1, len(self.body)):
            seg = self.body[seg_index]
            if head_x == seg._x and head_y == seg._y:
                return True
        return False


class Segment:

    def __init__(self, x, y, canvas, max_x, max_y, size, colour): # x and y position of top left corner
        # x and y is the top left corner of the segment (square)
        self._x = x
        self._y = y
        self._canvas = canvas
        self._max_x = max_x
        self._max_y = max_y

        self.old_x = x
        self.old_y = y
        self.size = size
        self.colour = colour

        self._rect_graphic = None

        self._draw()

    """ 
    Special method just for moving the head segment
    Deletes the graphical representation of the segment on the canvas and
    redraws it in the new position   
    """
    def movehead(self, direction):
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

        self._check_boundary(direction)
        self._draw()
        

    def _draw(self):
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
        self._draw()

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



        


