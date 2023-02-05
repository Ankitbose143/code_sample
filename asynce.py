import asyncio

list_1 = 'hi i am cool'.split()


async def hello(a):
    await asyncio.sleep(2)
    print(a)
    return a


async def run_tasks():
    tasks = [hello(word) for word in list_1]
    await asyncio.wait(tasks)


# def main():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(run_tasks())
#     loop.close()
#
#
# main()

# def main2():
asyncio.run(run_tasks())

# main2()