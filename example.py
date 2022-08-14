from datetime import date
class employee:
    salary = 10000
    no_of_emp = 0
    def __init__(self, name, empno, dob, city):
        self.name = name
        self.empno = empno
        self.dob = dob
        self.city = city
        employee.no_of_emp = employee.no_of_emp + 1

    def address(self):
        addr = f"Name : {self.name}\nEmpno : {self.empno}\nDOB : {self.dob}\nCity : {self.city}"
        return addr
    
    def age(self):
        current_year = date.today().year
        return current_year - self.dob
    
    def total_salary(self,bonus):
        self.salary = self.salary+bonus
        
emp1 = employee('kowsi',2,2003,'Vellore')
emp2 = employee('reshma',3,2001,'Ranipet')

emp1.total_salary(2000)

print(employee.no_of_emp)
print("EMPLOYEE 1")
print('NAME:',emp1.name)
print('SALARY:',emp1.salary)
print("EMPLOYEE 2")
print('NAME:',emp2.name)
print('SALARY:',emp2.salary)

OUTPUT:

2
EMPLOYEE 1
NAME: kowsi
SALARY: 12000
EMPLOYEE 2
NAME: reshma
SALARY: 10000

