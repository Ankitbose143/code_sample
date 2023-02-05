import asyncio
from random import randint
import time
import threading
import random
print("rng",random.randrange(5,100,2))

def print_i(i):
   number = 0
   if (number % 2) == 0: #check for even number
       pass
      # time.sleep(1)
   while number != 5:
      number = randint(0,100)
   print("id-", i)
st = time.time()
for i in range (0,100):
   print_i(i)
print("time", time.time()-st)
async def print_i(i):
   number = 0
   if (number % 2) == 0: #check for even number
       pass
      # time.sleep(1)
   while number != 5:
      number = randint(0,100)
   print("id-", i)
st1 = time.time()
for i in range (0,100):
   asyncio.run(print_i(i))
print("time2", time.time() - st)


async def square_number(n):
    for i in range(1, n+1):
        print("Square of ", i, "is ", i**2)
        # await asyncio.sleep(0.001)


async def main():
    async with asyncio.TaskGroup() as task_group:
        # Calling square number function
        task_group.create_task(square_number(5))
        task_group.create_task(square_number(10))


# calling main function
asyncio.run(main())