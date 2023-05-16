class AttributePrinterMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        str_ = f'{class_name}: {{\n'
        for k, v in self.__dict__.items():
            k = k.replace('_A__', '')
            if k[0] == '_':
                k = k[1:]
            str_ = str_ + f'\t{k}: ' + f'{v}\n'
        str_ = str_ + '}'
        return str_


class A(AttributePrinterMixin):
    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]


a = A()
print(a)
