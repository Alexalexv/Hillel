def call_counter(file):
    def call_counter_(func):
        def wrapper(*args):
            # next line for crating file if it not exist
            with open(f'{file}', 'a') as f:
                pass
            with open(f'{file}', 'r') as f:
                lst = list(f)
                # check for empty file
                if len(lst) == 0:
                    counter_before = 0
                else:
                    last_try: str = lst[-1]
                    last_try = last_try.replace('\n', '')
                    counter_before = int(last_try[26:-6])
            with open(f'{file}', 'a') as f:
                f.write(f"Function 'add' was called {counter_before + 1} times\n")
            return func(*args)

        return wrapper

    return call_counter_


@call_counter('data.txt')
def add(a, b):
    return a + b


