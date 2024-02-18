#1. Create a list of any object you design using any creation method you decide. 
#Have a for loop iterate over this list and do some form of operations on it and 
#print the results.

#2. Create a class called Book that stores the information for each of the books in 
#a library. The class should keep the title of the book, author, number of copies 
# of the book and number of lend copies. The class will contain the following 
# methods: 
#   -Default constructor. 
#   -Constructor with parameters. 
#   -Setters / getters. 
#Method Loan that increases the corresponding attribute each time a loan is made 
#from the book. No books may be borrowed if no copies are available to lend. 
#Returns true if the operation was successful and false otherwise. 

#Returns method that decrements the corresponding attribute when a book is returned.
#No books can be returned that have not been lend. Returns true if the operation was
#successful and false otherwise. 
#Write a method to display data from books. 
#Write a program to test the operation of the Book class.
class Book:
    def __init__(self, t='', aa='',c=0) -> None:
        self.__title = t
        self.__author = aa
        self.__availableCopies = c
        self.__lendCopies=0

    @property
    def lendCopies(self):
        return self.__lendCopies

    @lendCopies.setter
    def lendCopies(self, var):
        self.__lendCopies = var
        
    def __str__(self) -> str:
        return f"({self.__title, self.Author, self.Copies, self.__lendCopies})"
    
    @property
    def Title(self):
        return self.__title
    
    @Title.setter
    def Title(self, t):
        self.__title = t

    @property
    def Author(self):
        return self.__author
    
    @Author.setter
    def Author(self, t):
        self.__author = t
    
    @property
    def Copies(self):
        return self.__availableCopies
    
    @Copies.setter
    def Copies(self, t):
        self.__availableCopies = t
    
      
    def Loan(self):
        if(self.Copies>self.lendCopies):
            self.lendCopies += 1
            return True
        return False
    
    def Return(self):
        if(self.lendCopies>0):
            self.lendCopies -=1
            return True
        return False

    def Info(self):
        print (self)

b = Book('bb', 'a',2)    
b.Loan()
b.Loan()
b.Loan()
b.Info()
b.Return()
print(b)