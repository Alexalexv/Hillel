def call_counter(file):
    def call_counter_(func):
        def wrapper(*args):
            func_name = func.__name__
            func_name_len = len(func_name)

            # next line for creating file if it not exists
            with open(f'{file}', 'a') as f:
                pass

            # I need to get last counter of func
            lst = []
            with open(f'{file}', 'r') as f:
                for i in f:
                    if f"'{func_name}'" in i:
                        lst.append(i)

            # check case, when func run first time
            if len(lst) == 0:
                counter_before = 0
            # get last counter for function
            else:
                last_try: str = lst[-1]
                last_try = last_try.replace('\n', '')
                counter_before = int(last_try[10 + func_name_len + 13:-6])
            with open(f'{file}', 'a') as f:
                f.write(f"Function '{func_name}' was called {counter_before + 1} times\n")
            return func(*args)

        return wrapper

    return call_counter_


@call_counter('data.txt')
def add(a, b):
    return a + b


