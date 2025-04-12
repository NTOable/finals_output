class Employee :
    checkin_number = 0
    def __init__(self, name : str, code : int, department : str, age : int) :
        self.name = name
        self.code = code
        self.age = age
        self.department = department
        self.employee = []
        Employee.checkin_number += 1

    def add_employee(self, employee) :
        self.employee.append(employee)

    #defining constructor for dict alternative
    @classmethod
    def info_dict(cls, employee_dict : dict) :
        return cls(
            employee_dict['name'],
            employee_dict['code'],
            employee_dict['department'],
            employee_dict['age']
                   )

    #defining extra class method for OOP checklist
    @classmethod
    def get_checkin_number(cls) :
        return f"Number of employees that checked-in today: {cls.checkin_number}"

    #getters
    def get_code(self) :
        return f"Code: {self.code}"
    def get_name(self) :
        return f"Name: {self.name}"
    def get_age(self) :
        return f"Age:  {self.age}"
    def get_dept(self) :
        return f"Department: {self.department}"

#instances
employee1 = Employee("Jay", 823905, "Logistics", 28)
employee2 = Employee("Blake", 824005, "Marketing", 24)
employee3 = Employee("Cody", 824105, "IT", 25)

#alternative instance 1 (using dict)
employee4 = Employee.info_dict({
    "name" : "Emily", "code" : 824205,
    "department" : "Finance", "age" : 32
})

#classmethod output (outputs total amount of created instances of Employee)
print(Employee.get_checkin_number() + "\n")

for employee in [employee1, employee2, employee3, employee4] :
    print(employee.get_name())
    print(employee.get_code())
    print(employee.get_age())
    print(employee.get_dept() + "\n")
