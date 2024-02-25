class Employee:
    no_of_leaves=8

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        #self.email=f"{name}.{role}@gmail.com"

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def set_leaves(cls,no_of_leaves):
        cls.no_of_leaves=no_of_leaves
    @property
    def email(self):
        return f"{self.name}.{self.role}@gmail.com"

ajay=Employee("Ajay","22","Operator")

print(ajay.email)

ajay.name="python"

print(ajay.email)
