#2 - Create a Person class, with attributes name, surname and phone. Check that
# the phone only accepts 9 digits.
# Create an Account class, with accountNumber, balance and owner attributes. 
# The owner is a Person. 
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
import re
class Person:

    def __init__(self, name='', sur='', phone='') -> None:
        self._name=name
        self._surname=sur
        
        self._phone=phone

    def isValidPhone(self):
        pattern = re.compile(r'\d{9}')
        return re.match(self._phone)
    
    def toString(self):
        return (f"{self._name} {self._surname} (Phone:{self._phone})")
    
from enum import Enum    
class TransactionType(Enum):
    WITHDRAW =1
    DEPOSIT=2

class Account:
    def __init__(self,accN, p,b) -> None:
        self._accountNumber  = accN
        self._onwer = p
        self._balance = b

    @property
    def accountNumber(self):
        return self._accountNumber
    
    @accountNumber.setter
    def accountNumber(self, acc):
        self._accountNumber = acc

    @property
    def owner(self):
        return self._onwer
    
    @owner.setter
    def owner(self, o):
        self._onwer = o

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, b):
        self._balance = b

    def isValidBalance(self):
        if self.balance >= 0:
            return True
        return False
    
    def transaction(self, type, number):
        if(type==TransactionType.WITHDRAW):
            self.balance -= number
        elif type== TransactionType.DEPOSIT :
            self.balance += number

    def toString(self):
        return f"{self.owner.toString()}, {self.balance}"
    
class Main:
    def __init__(self) -> None:
        p1=Person("Jenny", "Nguyen", "123456789")
        acc1 = Account(1,p1, 123456,)
        acc1.transaction(1,5000)
        p2=Person("Timmy", "Phan", "987654321")
        acc2 = Account(2,p2, 20000)
        acc2.transaction(2,5000)

        print(acc1.toString())
        print(acc2.toString())

m = Main()