class Employee:
    no_of_leaves=8

    def __init__(self, name, role, salary):
        self.name=name
        self.role=role
        self.salary=salary

    def __add__(self, other):
        return self.salary+other.salary
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def set_leaves(cls,no_of_leaves):
        cls.no_of_leaves=no_of_leaves
    
#https://docs.python.org/3/library/operator.html#mapping-operators-to-functions

emp1 = Employee("ajay", "Developer", 300)
emp2 = Employee("Chaku", "master chef", 600)

print(emp1+emp2)

