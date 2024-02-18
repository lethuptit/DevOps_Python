#1Create a program print the average height of 10 student and Who are above or below the avrage
class Student:
    Name=""
    Height=0

    def __init__(self, name, height):
        self.Name = name
        self.Height = height
    
    def __str__(self):
        return f"{self.Name}({self.Height} cm)"
    def __repr__(self) :
        #str(self)
        return f"{self.Name}({self.Height} cm)"
#*ehuewhrue
# ewihfqwefh
#!ewjhrewjrhekwj
#?
#//jhasdjgs

class ClassRoom:
    Students =[]
    AvgHeight=0
    belowAvgStudents=[]
    aboveAvgStudents=[]

    def calAvgHeight(self):
        sum=0;
        for student in self.Students:
            sum += student.Height

        avg = sum/len(self.Students)

        for student in self.Students:
            if(student.Height >= avg):
                self.aboveAvgStudents.append(student)
            else:
                self.belowAvgStudents.append(student)
        
        return avg    

def calAvgHeightinClass(n):
    room = ClassRoom()
    for i in range(0,n):
        s = input("{}. Enter student's name and height(cm):".format(i+1))
        try:        
            l = s.rsplit(" ",1)
            student = Student(l[0],int(l[-1]))
            room.Students.append(student)
            avg = room.calAvgHeight()

        except ValueError:
            print("Invalid date type. Program ends.")

    print("The average of height is ", avg)
    print("Students above average height are: ", room.aboveAvgStudents)
    print("Students below average height are: ", room.belowAvgStudents)



    
calAvgHeightinClass(2)