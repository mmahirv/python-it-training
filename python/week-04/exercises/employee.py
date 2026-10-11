class Employee:
    def __init__(self, name, surname, salary):
        self.name = name 
        self.surname = surname 
        self.salary = salary
        
    def __str__(self):
        return f'{self.name} {self.surname} earn every month: {self.salary}'
    
    def hello(self):
        print(f'Hello I am Empoyeee {self.name}')
    
class Developers(Employee):
    def __init__(self, name, surname, salary, department):
        super().__init__(name, surname, salary)
        self.department = department
        
    def __str__(self):
        return (super().__str__() + f' in this departmenr: {self.department}')
    
class Intern(Employee):
    salary = 2000
    
    def __init__(self, name, surname, department):
       super().__init__(name, surname, self.salary)
       self.department = department

mahir = Intern('Mahir', 'Varli', 'product')

print(f'{mahir.name} {mahir.surname} {mahir.salary} {mahir.department}')

mahir.hello()

dila = Employee('Dila', 'Abla',5000)

dila.hello()