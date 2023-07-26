from threading import Thread
from time import time, perf_counter_ns
import random
import os

NS = 1000_000_000


def file_generator(directory, number_of_files, size):
    i = 0
    while i < number_of_files:
        a = 0
        random_string = ''
        random_size = random.randrange(int(size / 2), size)
        while a < random_size:
            punctuation = [33, 34, 39, 40, 41, 44, 10, 45, 46, 58, 59]
            random_lst = (
                [random.randrange(48, 58), random.randrange(65, 91), random.randrange(97, 123),
                 random.choice(punctuation)])
            random_val = random.choice(random_lst)
            random_char = chr(random_val)
            random_string += random_char
            a += 1
        with open(directory + str(int(time())) + str(i), 'a') as f:
            f.write(random_string)
        i += 1


def count_letters_in_file(file_path, letter_to_find):
    with open(file_path, 'r') as f:
        string = f.read()
        return string.count(letter_to_find)


def count_letters_in_files(dir_, file_names, letter_to_find, counter_res: list):
    counter = 0
    for i in file_names:
        sub_counter = count_letters_in_file(dir_ + i, letter_to_find)
        counter += sub_counter
    counter_res.append(counter)
    return counter


def letter_counter_in_one_thread(directory, letter_to_find):
    files = os.listdir(directory)
    counter = 0
    for i in files:
        counter += count_letters_in_file(directory + i, letter_to_find)
    return counter


def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    files = os.listdir(directory)
    avg_chunk_size = len(files) // number_of_threads
    remainder = len(files) % number_of_threads
    splitted_files = []
    start = 0
    for i in range(number_of_threads):
        end = start + avg_chunk_size + (1 if i < remainder else 0)
        splitted_files.append(files[start:end])
        start = end
    counter = []
    threads = []
    for i in splitted_files:
        thread = Thread(target=count_letters_in_files, args=(directory, i, letter_to_find, counter))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return sum(counter)


file_generator('dir/', 200, 100000)

start_time = perf_counter_ns()
multi = letter_counter_in_n_threads('dir/', 'b', 100)
end_time = perf_counter_ns()
print(f"multi thread io: {(end_time - start_time) / NS}, result = {multi}")

start_time = perf_counter_ns()
one = letter_counter_in_one_thread('dir/', 'b')
end_time = perf_counter_ns()
print(f"one thread io: {(end_time - start_time) / NS}, result = {one}")




