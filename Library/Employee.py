from Person import Person


class Employee(Person):
    def __init__(self, name, contact, salary, job):
        super().__init__(name, contact)
        self.__salary = salary
        self.job = job

    @property
    def employee_info(self):
        return f'name: {self.name}, contact: {self.contact}, job: {self.job}, salary: {self.__salary}'


