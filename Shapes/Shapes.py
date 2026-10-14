class Shapes:
    def __init__(self, colour):
        self._colour =  colour

    def get_area(self):
        ...

class Rectangle(Shapes):
    def __init__(self, colour, length, breath):
        super().__init__(colour)
        self._length = length
        self._breath = breath

    def get_area(self):
        return self._length * self._breath