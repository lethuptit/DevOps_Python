def fisrtMethod():
    print("Hello world")
    #print(8*"\n")
    try:
        n=(int)(input("Enter a numer:"))
        sum=0
        for i in range(n, n+101):
            print(i)
            sum += i
        print(sum)
    except ValueError:
        print("Wrong input number.")

#20 - Write a Python program that declares an integer variable B and assign it a value. It then displays 
#a message indicating whether the value of B is positive or negative. We will consider 0 as positive.
#If for example B = 1 the output will be 1 is positive. If for example B = -1 the output will be: -1 
#is negative.
import random
def isPositive():
    b=random.randint(-100,100)
    if b>=0 :
        print("This is a positive number")
    else:
        print("This is a negative number")
    return

#21 - Make a program in Python such that given as data the enrolment and 5 grades of a student; 
#Print the enrolment, the average and the word "approved" if the student has an average greater than 
#or equal to 6, and the word "not approved" otherwise. Data: MAT, CAL1, CAL2, CAL3, CAL4, CAL5 
#Where: MAT is an integer variable that represents the student's enrolment. CAL1, CAL2, CAL3, CAL4 and 
#CAL5 are real-type variables representing the student's 5 grades.
def studentData()    :
    try:
        mat = (int)(input("Enter the enrollment:"))
        cal1=(float)(input("Enter the first grade:"))
        cal2=(float)(input("Enter the second grade:"))
        cal3=(float)(input("Enter the third grade:"))
        cal4=(float)(input("Enter the forth grade:"))
        cal5=(float)(input("Enter the fifth grade:"))

        print("The student's enrollmetn {} ".format(mat), end=-1)
        avg= (cal1+cal2+cal3+cal4+cal5)/5
        if(avg>=6):
            print("approved.")
        else:
            print("not approved.")
    except ValueError:
        print("Some wrong data. Program ends.")  

    return  

#22 - Make the program in Python such that given as a worker's salary, apply a 15% increase if your salary 
#is less than $ 1000 and 12% otherwise. Print the new salary of the worker. 
#Fact: SUE (variable of real type that represents the salary of the worker).
def realSalary(salary):
    if(salary<1000):
        salary *= 1.15
    else:
        salary *=1.2
    print("The new salary is ", salary)    


#23 - Make a program that prints the 10 multiplication tables.
def mul10Table():
    for i in range(1,11):
        print(" 10 x {} = {}".format(i,10*i))


#24 - Make a calculator.'
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def sub(x, y):
    return x - y

# This function multiplies two numbers
def mul(x, y):
    return x * y

# This function divides two numbers
def div(x, y):
    return x / y

import readchar
def calc():
    
    while True:
        list=[]
        print("Select operation.")
        print("1.Add\t2.Subtract\t3.Multiply\t4.Divide")
        c = readchar.readchar()
        print(c)
        if c in ('1', '2', '3', '4'):
            while True:
                try:
                    list.append(float(input("Enter an operand: ")))
                    if(len(list)>=2):
                        break
                except ValueError:
                    print("Invalid input. Please  try again.")
                    continue

            num1 = list[0]
            num2=list[1]
            if c == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif c == '2':
                print(num1, "-", num2, "=", sub(num1, num2))

            elif c == '3':
                print(num1, "*", num2, "=", mul(num1, num2))

            elif c == '4':
                print(num1, "/", num2, "=", div(num1, num2))
            
            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Continue? (y/n): ")
            if next_calculation == "n":
                break
        else:
            print("Wrong operator. Program ends.")    
            break

#realSalary(1000)
#mul10Table()
calc()            