#Create a class called Password with the following conditions:
#It has the length and password attributes. By default, the length will be 8. 
#The constructors will be as follows: A default constructor. A constructor with the
# length that we send as parameter. 
#Generate a random password with that length. 
#The methods you implement will be: 
#   -isStrong (): return a boolean if it is strong or not, to be strong you must 
#have more than 2 uppercase, more than 1 lower case and more than 5 numbers. 
#   - GeneratePassword (): Generates the password of the object with the defined 
#length. 
#   -Get method for password and length. 
#   -Set method for length. 

import string
import random

class Password:
    def __init__(self, l=0) -> None:
        self._password=''
        self._length=l
        if(l>0):
            self.generatePassword(l)

    def generatePassword(self, length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        self.password = ''.join(random.choice(letters) for i in range(length))
        #print("Random string of length", length, "is:", result_str)
        return self.password
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,s):
        self._password = s

    @property
    def length(self):
        return self.length
    
    @length.setter
    def length(self,l):
        self.length=l

    def isStrong(self):
        num=0
        upper=0
        lower  =0
        for c in self.password:
            if(c.isdigit):
                num+=1
            elif c.isupper():
                upper+=1
            elif c.islower:
                lower+=1
        
        if(num>=5 & upper>=2 & lower>=1):
            return True
        return False
    
    def __str__(self) -> str:
        s=''
        if self.isStrong()==True:
            s="Strong"
        else:
            s="Weak"
        return f"{self.password}: {s}"
    
    def __repr__(self) -> str:
        s=''
        if self.isStrong()==True:
            s="Strong"
        else:
            s="Weak"
        return f"{self.password}: {s}" 

#Now let's create an executable class:
#Create an array of Passwords with the size that you indicate by keyboard. 
#Create a loop that creates an object for each position in the array. It also
# indicates by keyboard the length of the Passwords (before loop).     
#Create another array of booleans where we store if the password of the password
# array is strong or not (use the previous loop).     
#At the end, we show the password and whether or not it is strong (use the previous
# loop). Use this simple format: password1 boolean_value1, #password2 boolean_value2

passwords = []
isStrongPass=[]
n=(int)(input("Input the number of passwords:")    )
for i in range(1,n+1):
    l=(int)(input("Input the length of password {} :".format(i))    )
    if(l<=0):
        i-=1
        continue
    p = Password(l)
    #isStrongPass.append("Strong" if p.isStrong()==True else "Weak")
    passwords.append(p)

print(passwords)

#1 - Implement the class Position that represents a coordinate (x, y). Each position is defined by two integer values ​​x and y. Available operations are:
#· Default constructor, corresponds to the position (0,0). 
#· Constructor with initial values ​​of X and Y 
#· Methods for modifying and querying (set / get) the attributes of the class. 
#· Methods for increasing and decreasing the values ​​of each of the position coordinates (incX, incY, decX, decY). 
#· A method for setting coordinate values ​​(setXY).

#2 - Create a Person class, with attributes name, surname and phone. Check that the
# phone only accepts 9 digits. Create an Account class, with accountNumber, balance
# and owner attributes. The owner is a Person. Create a constructor with parameters
# and another without parameters, access methods and toString for these classes.
# Check that the balance of the account must not be less than 0. Create a method
# called transaction that enters as parameters quantity and transactionType;
# Transaction type is "withdrawal" or "deposit". If it is a withdrawal, the amount
# is subtracted from the balance, and if it is deposit the amount is increased to
# the balance. The transaction method must print the transaction type and the new
# balance. Create in a class called Main, two accounts belonging to two different
# people and make a deposit and a withdrawal in each account. Print the values ​​of
# people, owners and transactions.