class Employee:
    salary = 120000
    name = "Rohit"
    def getDetails(self):
        print("Name -> ",self.name)
        print("Salary -> ",self.salary)
emp1 = Employee()
emp1.getDetails()