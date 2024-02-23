class Employee:
    empCount = 0  # Class variable
    address=''
    sinNymber=''
    job=''
    dateOfBirth=''

    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable
        Employee.empCount += 1

    def display_count(self):
        print(f'Total Employees: {Employee.empCount}')

    def display_employee(self):
        print('Name: {}, Salary: {}'.format(self.name, self.salary))

    def increaseSalary(self, num):
        self.salary += num

    
emp1 = Employee('Mike', 10000)
emp2 = Employee('Doug', 5000)
emp1.display_employee()
emp2.display_employee()
emp1.display_count()