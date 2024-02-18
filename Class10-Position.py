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

#2 - Create a Person class, with attributes name, surname and phone. Check that
# the phone only accepts 9 digits. Create an Account class, with accountNumber,
# balance and owner attributes. The owner is a Person. 
#Create a constructor with parameters and another without parameters, access methods
# and toString for these classes.
# Check that the balance of the account must not be less than 0. Create a method
# called transaction that enters as parameters quantity and transactionType;
# Transaction type is "withdrawal" or "deposit". If it is a withdrawal, the amount
# is subtracted from the balance, and if it is deposit the amount is increased to
# the balance. The transaction method must print the transaction type and the new
# balance. Create in a class called Main, two accounts belonging to two different
# people and make a deposit and a withdrawal in each account. Print the values ​​of
# people, owners and transactions.