from HW34_1 import Company
from HW34_2 import Employee

some_company = Company("Rusalka", "rusalka.com")
print(some_company.company_name, some_company.site)
print(some_company.add_employee_count(1, 2))
print(some_company.get_dict())


some_employee = Employee("Ivan", "Dorn", "Music", "17-10-1988")
print(some_employee.days_in_company())