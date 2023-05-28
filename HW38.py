class ClassCache:
    def __init__(self, func):
        self.func = func
        self.func_dict = {}

    def __call__(self, *args, **kwargs):
        key_dict = str(args)
        key_kwargs = sorted(kwargs)
        key_dict = key_dict + str(key_kwargs)
        if key_dict in self.func_dict.keys():
            result = self.func_dict[key_dict]
        else:
            result = self.func(*args, **kwargs)
            self.func_dict[key_dict] = result
        return result
