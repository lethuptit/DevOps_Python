#15)For our brave ones: translate a time expressed in seconds to a time expressed 
# in days, hours, minutes and seconds.
def time_in_day1():
    secs = int(input("Enter the number of seconds: "))
    days = secs//86400
    hours = (secs - days*86400)//3600
    minutes = (secs - days*86400 - hours*3600)//60
    seconds = secs - days*86400 - hours*3600 - minutes*60
    print(("{} days, ".format(days) if days else "") + 
          ("{} hours, ".format(hours) if hours else "") + 
            ("{} minutes, ".format(minutes) if minutes else "") + 
            ("{} seconds ".format(seconds) if seconds else ""))
    return

import math
#11. Given the radius of a circle, make an algorithm to calculate the value of the area.
def circle_area(radius):
    #radius = first_number
    area = math.pi*radius*radius
    print("Area of the circle is:", area)
    return

#12)Write an algorithm that determines if an "N" number is divisible by another "M".
def is_divisible(N, M):
    r=N/M
    if(N==M*r):
        print(str(N) + "is devisible by " + str(M))
    else:
        print(str(N) + "is not devisible by " + str(M))
    return


#13)Write an algorithm to translate a time expressed in days, hours, minutes and seconds
# to time expressed in seconds.
def time_in_seconds( d,  h,  m,  s):
    total_secs = d*8400 + h*3600 + m*60+s
    print('The total second is {f}'.format(total_secs))
    return total_secs

#14)We are being informed of three environmental temperature values, and we are asked
# to develop an algorithm to calculate and report the sum and average of these values.
def sum_avg(val1, val2,val3):
    sum= val1+val2+val3
    avg=sum/3
    print("Sum is " + str(sum))
    print("Average is " + str(avg))
    return


# Practice
def sum_product(val1, val2):
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
    except ValueError:
        print("User input is not an integer")

    sum = first_number + second_number
    product = first_number * second_number

    print("Sum:", str(sum))
    print("Product:", str(product))
    return

time_in_day1()


