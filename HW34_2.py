from datetime import datetime


class Employee:
    counter = 0

    def __init__(self, name, surname, department, date_start):
        """
        Employee card
        :param name: str
        :param surname: str
        :param department: str
        :param date_start: str %d-%m-%Y
        """
        self.name = name
        self.surname = surname
        self.department = department
        self.date_start = datetime.strptime(date_start, "%d-%m-%Y")
        Employee.counter += 1

    def days_in_company(self):
        """
        Count time in company
        :return: class datetime.timedelta
        """
        delta = datetime.now() - self.date_start
        return delta
