class Employee:
    no_of_leaves=8

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def set_leaves(cls,no_of_leaves):
        cls.no_of_leaves=no_of_leaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    

    @staticmethod
    def printgood(string):
        print(f"{string} is awesome")
        
    

#ajay=Employee("Ajay","22","Operator")

# chaku=Employee.from_str("chaku-480-team member")


# print(chaku.role)
        
Employee.printgood("Ajay")


#print(ajay.printdetails())