#3 - (Poll.py) A survey was carried out to 15 students in a University 
#where the following information was requested: Photo ID #, SEX, SALARY, JOB.
#• PHOTO ID # (It's an integer)
#• SEX (1 - Male 2 - Female)
#• JOB (1 - If you work 2 - Do not work)
#• SALARY (An integer value)
#Write the algorithm that allows reading and storing the requested data in vectors, 
#then calculate and print:
#• Percentage of men in the university
#• Percentage of women in the university
#• Percentage of men who work and average salary
#• Percentage of working women and average salary
class Student:
    def __init__(self, photo_id, sex, sal, job):
        self.PhotoID = photo_id
        self.Sex = sex
        self.Salary = sal
        self.Job = job
import pandas     
class University:
    def __init__(self, list):
        self.Students = list

    #def menPortion(self):
    #    return sum (self.Students.Sex==1)/ len(self.Students)
    
    def womenPortion(self):
        return sum(self.Students.Sex==2)/len(self.Students)

    def avgSalWorkingMenPortion(self):
        s = sum(self.Students.Sex==1 and self.Students.Job==1)/len(self.Students)
    
    def avgSalWorkingWomenPortion(self):
        return sum(self.Students.Sex==2 and self.Students.Job==1)/len(self.Students)
    
def readStudentData(file):
    
    students=[]
    try:
        df = pandas.read_excel(file)
        
        # Iterate the loop to read the cell values
        for row in range(0, df.shape[0]):
            id = df.iloc[row,1]
            sex= df.iloc[row,2]
            job = df.iloc[row,3]
            sal= df.iloc[row,4]

            s = Student(id, sex, job,sal)
            students.append(s)

        total = (df.shape[0])
        menPortion = sum(df["Sex"]==1)*100/total
        womenPortion = sum(df["Sex"]==2)*100/total
        df1 = df[(df["Sex"]==1) & (df["Job"]==1)]
        if(df1.empty):
            workingMenProtion =0
            avgMenSalary =0
        else:
            workingMenProtion= df1.shape[0]/total
            avgMenSalary = 1

        #workingWomenProtion= sum(df["Sex"]==2 & df["Job"]==1)/total
        print(workingMenProtion)
        return students

    except FileNotFoundError:
        print(f"Error: File '{file}' not found. Please provide the correct file path.")
        exit()
    except pandas.errors.EmptyDataError:
        print(f"Error: File '{file}' is empty. Please make sure it contains data.")
        exit()


readStudentData("StudentData.xlsx")