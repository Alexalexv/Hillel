import time


class Timer:
    def __init__(self):
        self.start = 0.0
        self.end = 0.0
        self.elapsed_time = 0.0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        elapsed_time = self.end - self.start
        self.elapsed_time += elapsed_time
        return

    def reset(self):
        self.elapsed_time = 0.0
        return




with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
time.sleep(1)
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds
