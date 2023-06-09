import re


class AttributePrinterMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        str_ = f'{class_name}: {{\n'
        for k, v in self.__dict__.items():
            k = re.sub('^_\w+__', '', k)
            if k[0] == '_':
                k = k[1:]
            str_ = str_ + f'\t{k}: ' + f'{v}\n'
        str_ = str_ + '}'
        return str_


class B_b_123:
    def __init__(self):
        self.__private_in_B = 'private_in_B'


class A(B_b_123, AttributePrinterMixin):
    pass


a = A()
print(a)
