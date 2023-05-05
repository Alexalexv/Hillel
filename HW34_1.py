import time
import random


class Company:
    version = '1.01'

    def __init__(self, name, site, description='Nothing here', count_employee='Nothing here'):
        self.company_name = name
        self.emploee_count = count_employee
        self.site = site
        self.description = description

    def add_employee_count(self, min_count: int, max_count: int):
        """
        Returns True if get valid data, else - false. Set in format "{min_count}...{max_count} specialists"
        :param min_count: int
        :param max_count: int
        :return: bool
        """
        if isinstance(min_count, int) is False or isinstance(max_count, int) is False:
            return False
        elif min_count > max_count:
            return False
        else:
            self.emploee_count = f'{min_count}...{max_count} specialists'
            return True

    def get_dict(self):
        """
        Dict with company information will be returned
        :return: dict
        """
        dict_ = {"company_name": f"{self.company_name}", "emploee_count": f"{self.emploee_count}",
                 "site": f"{self.site}", "description": f"{self.description}"}
        return dict_

    @staticmethod
    def generate_identifier(additional_length=5):
        """
        Static method for generation random identifier for using
        :param additional_length: int
        :return: str
        """
        i = 0
        result = ''
        while i < additional_length:
            random_lst = ([random.randrange(48, 57), random.randrange(65, 90), random.randrange(97, 122)])
            random_val = random.choice(random_lst)
            random_char = chr(random_val)
            result += random_char
            i += 1
        timestamp = int(time.time())
        identifier = f'{timestamp}_{result}'
        return identifier



