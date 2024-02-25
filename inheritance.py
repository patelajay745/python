from staticmethod import Employee

class Programmer(Employee):
    @classmethod
    def fav_lang(cls,string):
        
        return f"{string} has no of {cls.no_of_leaves}"
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}"
    


ajay=Programmer("ajay","programmer","300")        
print(ajay.printdetails())