#1)	What are the differences and similarities between an identifier and a reserved word.

#-->Identifiers are the name used to identify a variable/function, constant, object, class… 
#-->that are able to be used by the user and the scope where they are defined 
#-->while reserved Word is predefined in a specific programming language with its meanings and functions 
#that all users can use.


#2)	Create an algorithm to determine the largest of 3 numbers.
def findMaxNumber():
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        third_number = int(input("Enter the second number: "))
    except ValueError:
        print("User input is not an integer")

    print("The biggest is :", str(max(first_number,second_number,third_number)))
    return

#3)	Create an algorithm to determine the largest of a series of numbers that are read from the keyboard. 
#The user ends by entering -1.
def findMaxNumber():
    n=0
    list=[]
    while(n!=-1):
        try:
            n = int(input("Enter a number: "))
            if n!=-1:
                list.append(n)     
            else:
                break 
        except ValueError:
            print("User input is not an integer")


    print("The biggest is :", str(max(list)))
    return

#4)Write an algorithm to determine the least of a series of numbers that are read from the keyboard. 
#The user ends by entering -1. What differences do you find with respect to the previous algorithm? 
#--> Just differ only the function
def findMinNumber():
    n=0
    list=[]
    while(n!=-1):
        try:
            n = int(input("Enter a number: "))
            if n!=-1:
                list.append(n)
            else:
                break
        except ValueError:
            print("User input is not an integer")

    print("The smallest is :", str(min(list)))
    return

#5)	Write an algorithm to print and count the multiples of 3 from 1 to a number that we enter by keyboard.
def countMulOf3():
    n=0
    count=0
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("User input is not an integer")

    for i in range(1,n+1):
        count = count+3*i
        
    print("The count of multiple of 3 from 1 to {} is {}".format(n,count))
    return

#6)	Write an algorithm that reads a series of real numbers and adds them, printing the result. 
#The series ends when the user enters the number zero.
def findSumOfNumbers():
    n=-1
    list=[]
    while(n!=0):
        try:
            n = int(input("Enter a number: "))
            if n!=0:
                list.append(n)
            else:
                break
        except ValueError:
            print("User input is not an integer")

    print("The sum is :", str(sum(list)))
    return


#7)	Write an algorithm to find the average of a series of numbers that are read from the keyboard. 
#Compare this exercise with the previous one. What are the differences and similarities?
def findAvgOfNumbers():
    n=-1
    num=0
    list=[]
    while(n!=0):
        try:
            n = float(input("Enter a number: "))
            if n!=0:
                list.append(n)
                num+=1
            else:
                break
        except ValueError:
            print("User input is not an integer")

    print("The average is :", str(sum(list)/num))
    return

#8)	Given a series of real numbers that are being read from the keyboard, 
#determine the maximum value and the position of it.
def findPosOfMaxNum():
    n=-1
    num=0
    list=[]
    while(n!=0):
        try:
            n = float(input("Enter a number: "))
            list.append(n)
        except ValueError:
            break

    print("The max is :{} and its position is {}".format(max(list), list.index(max(list))))
    return

#9)	Write an algorithm that requests the reading of a series of individual characters and count how many times 
#the letter "a" is entered. The user ends by entering the "$" symbol. 
import readchar

def findTimesOfa():
    c=' '
    count=0
    list=[]
    while(c!='$'):
        print("Enter a character: ",end='')
        c = readchar.readchar()
        print(c)
        if c=='a':
            count +=1


    print("The number of 'a' is :{}".format(count))
    return



#10)Develop an algorithm to count the number of students whose weight is between 50 and 60, 
#between 61 and 80 and between 81 and 100. The weights are entered by keyboard and report 
#the number of students in each category of weight. How does the algorithm change 
#if I want to accumulate weight totals for each category?
def groupWeights():
    n=-1
    list50_60=[]
    list61_80=[]
    list81_100=[]

    while(n!=0):
        try:
            n = float(input("Enter a weight: "))
            if n==0:
                break
            elif n>=50.0 and n<=60.0 :
                list50_60.append(n)
            elif n>=61 and n<=80 :
                list61_80.append(n)    
            elif n>=81 and n<=100 :
                list81_100.append(n)  
        except ValueError:
            print("User input is not an integer")

    print("There is {} student in 50-60 kilogram with weight total is {}:".format(len(list50_60), sum(list50_60)))
    print("There is {} student in 61-80 kilogram with weight total is {}".format(len(list61_80), sum(list61_80)))
    print("There is {} student in 81-100 kilogram with weight total is {}".format(len(list81_100), sum(list81_100)))
    return

#11)	Write an algorithm to determine if a number read by keyboard is prime.
def isPrime():
    num = int(input("Enter a number: "))
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

        # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")

#12)Write an algorithm to print and count numbers that are multiples of 2 or 3 that are between 1 and 100.
def findMultiple2_3():
    list2=[]
    list3=[]
    for i in range(1, 101):
        if (i % 2) == 0:
            list2.append(i)
        elif i%3==0:
            list3.append(i)

    print("Multiple of 2 has {} number including:\n{}".format(len(list2), list2))
    print("Multiple of 3 has {} number including:\n{}".format(len(list3), list3))


#13)Develop an algorithm to determine if a series of numbers that the user is entering is in increasing 
#     order or not.
import sys
def isIncreasingList():
    m=-sys.float_info.max
    print(m)
    while(1):
        try:
            n=(float)(input("Enter a number: "))
            if(n<m):
                print("This is not an increasing order.")
                return
            else:
                m=n
        except ValueError:
            break;

    print("This is an increasing order.")
    

#time_in_day1()
#findMaxNumber()
#findMinNumber()
#countMulOf3()
#findSumOfNumbers()
#findAvgOfNumbers()
#findPosOfMaxNum()
#findTimesOfa()
#groupWeights()
#findMultiple2_3()
isIncreasingList()
