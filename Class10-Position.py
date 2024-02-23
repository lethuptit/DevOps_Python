#1 - Implement the class Position that represents a coordinate (x, y). 
#Each position is defined by two integer values ​​x and y. Available operations are:
#   · Default constructor, corresponds to the position (0,0). 
#   · Constructor with initial values ​​of X and Y 
#   · Methods for modifying and querying (set / get) the attributes of the class. 
#   · Methods for increasing and decreasing the values ​​of each of the position
# coordinates (incX, incY, decX, decY). 
#   · A method for setting coordinate values ​​(setXY).

class Position:

    def __init__(self, a=0, b=0) -> None:
        self._x=a
        self._y=b
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,a):
        self._x=a

    @property
    def y(self):
        return self._y
    
    @x.setter
    def y(self,a):
        self._y=a

    def incX(self):
        self.x +=1
        return self.x
    
    def decX(self):
        self.x -=1
        return self.x
    
    def incY(self):
        self.y +=1
        return self.y
    
    def decY(self):
        self.y -=1
        return self.y
    
    def setXY(self,X,Y):
        self.x=X
        self.y=Y

