#1)	What are the advantages and disadvantages of modular programming. 
#Explain in words how to model with modules a problem where you have to read from the keyboard a series 
#of numbers (which can be stored in a list) and display the 3 major numbers and 3 minor ones.
#--> Advantages:
#   + Reusable & reduce time for re-writting code
#   + Clear & Easy to understand
#   + Can be maintained easily and developed for large scaling
#--> Disadvantages:
#   + Sometimes they look a little messy by transfering parameters and return value.
#   + need to be generalizaion for almost situation so Some operation are repeated when calling modules
#   +
#--> The first routine to determine 3 major numbers and 5 minor ones from a input list and return 2 list of 
# output, one for major and one for minor
#--> The another funcion allows users to input a series of number and put them to a list then call the first 
#    routine to get back two output list, then print out these lists to the console


#2)	Count the number of words, separated by one or more spaces, from a telegram ending in point. 
#   It can be assumed that the user enters character by character the telegram or the complete sequence, 
#   which is more comfortable to propose a solution. 

#3)	Given the following algorithms:

#algorithm a1
#	var Number : x
#	x <-- 10                        x=10
#	print (x * 5)                   printed 20
#	x <-- a2(x*2)                   x = a2(20) --> x =10
#	x <-- x * 2                     x = 20
#	a2(x)                           a2(20) --> after this, x = 20
#end algorithm

#algorithm a2(Number : x) : Number          if x=20  as am input
#print (x)                                  printed 20
#x <-- x / 2                                x = 10
#print (x)                                  printed 10
#return x                                   return x = 10
#end algorithm

#Identify the scopes of each variable. Track the execution of a1 indicating what is displayed by console. 
#Iden for the execution (independently) of the algorithm a2.


#4)	Develop an algorithm for a dice game. The player must bet on a number between 1 and 6 (keyboard reading), 
#   then you must simulate the roll of a dice and finally inform the player if he has won or lost 
#   (print on screen).
import random
def diceGame():
    try:
        n=int(input("Enter a your number:"))
        m=random.randing(1,6)
        if(m==n):
            print("You win.")
        else:
            print("You lose.")
    except ValueError:
        return;


#5)	Write an algorithm to invert a string of characters. 
def invert(s):
    return s[::-1]

#6)	Explain what the following algorithm performs

#algorithm toInt (String : cad)
#   var Number : long,i <-- 0,pot <-- 1,res <-- 0
#   var String : c
#   long <-- length (cad)
#   while (i < long) do
#       c <-- charIn(cad,long - i - 1)          get the last character of the input String and conver to number format
#       res <-- res + ord(c) * pot              count the the numberic level of this char and the prevuous
#       pot <-- pot * 10                        go to the next numberic level
#       i <-- i + 1                             get the next left char of the input string
#   end while
#   return res
#en algorithm

#Where ord is a function that receives a character and returns its value in numeric format. 
#This way it is compatible to work with arithmetic operations.


#7)	Propose a modular solution to the problem of determining if a number is prime.
#algorithm IsPrime(int: n)
#   for each i in (0, n-1)
#       if n mod i ==0
#            return false
#       
#   return true


#8)	Write a sub-algorithm that has a parameter of type number that represents a year and determines 
#whether the year is leap year or not.
#algorithm isLeapYear(int: year)
#   if year mod 4 ==0
#       return true
#   else    
#       return true
#end


#9)	Write a sub-algorithm to determine the number of days of a month of a year, the latter two parameters 
#of the sub-algorithm.
#algorithm getDays(int: month, int: year) return int
#   switch (month)
#       case 1,3,5,7,8,10,12: return 31     break
#       case 4,6,9,11: return 30 break
#       case 2:
#            if(isLeap(year))    
#                return 29
#           else return 28
#           break
#end


#10)	A meteorological station collects rain data for a month and year of a determined locality. 
#An algorithm must be written asking the user to enter a month and a year, and allow for each day of that 
#month in that year, enter the millimeters of water that were recorded 
#(in case of not having registered a rain one day is entered 0) . 
#The amount of total millimeters of water precipitated in that month must be shown, the maximum precipitation 
#recorded for a day and on what day it was given, and finally if it rained two days in a row.


