import asyncio
import time
import multiprocessing.dummy

flatten = lambda t: [item for sublist in t for item in sublist]

numbers = flatten([[(x, y) for x in range(2000)] for y in range(2000)])

def add_them(x, y):
  return x + y

def async_loop(arguments_list, iterating_function):
    async def async_function(*args):
        iterating_function(*args)
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(async_function(*arguments)) for arguments in arguments_list]
    loop.run_until_complete(asyncio.gather(*tasks))

def thread_loop(arguments_list, iterating_function, pool_size):
    def list_function(arguments_list):
      iterating_function(*arguments_list)
    pool = multiprocessing.dummy.Pool(pool_size)
    pool.map(list_function, arguments_list)
    pool.close()
    pool.join()


# tests!

start = time.perf_counter()
for nums in numbers:
  x, y = nums
  add_them(x, y)
end = time.perf_counter()
print('for loop takes {}'.format(end-start))
'''
start = time.perf_counter()
async_loop(numbers, add_them)
end = time.perf_counter()
print('async takes {}'.format(end-start))
'''
start = time.perf_counter()
thread_loop(numbers, add_them, 2)
end = time.perf_counter()
print('multiprocessing takes {}'.format(end-start))

start = time.perf_counter()
[add_them(x, y) for x, y in numbers]
end = time.perf_counter()
print('list comprehension takes {}'.format(end-start))
