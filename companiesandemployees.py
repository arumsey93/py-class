import datetime

class Employee:

    def __init__(self, name, title):
        self.name = name
        self.job_title = title
        self.employment_start_date = None

    def hired(self):
        self.employment_start_date = datetime.datetime.now()

class Company:

    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry = industry
        self.employees = list()

    def employee_list(self, employee):
        self.employees.append(employee)

    def company_print(self):
        print(f'{self.name} is in the {self.industry} and has the following employees')
        self.emp()

    def emp(self):
        for employees in self.employees:
            print(f'*   {employees.name}')

MatthewLLC = Company("Matthew LLC", "666 Satans Way", "Homewrecking")
TylerInc = Company("Tyler Inc", "123 CoolGuy Ave", "Wet Tshirt contests")

Matthew = Employee("Matthew", "Tshirt Provider")
Tyler = Employee("Tyler", "Home DESTROYER")
Drew = Employee("Drew", "Cameraman")
Danny = Employee("Danny", "Janitor")
Alex = Employee("Alex", "CEO")

TylerInc.employee_list(Matthew)
TylerInc.employee_list(Drew)
MatthewLLC.employee_list(Tyler)
MatthewLLC.employee_list(Danny)
MatthewLLC.employee_list(Alex)
TylerInc.company_print()
MatthewLLC.company_print()

