import asyncio

import time

now = lambda: time.time()

async def foo(x):
    print("xxxxxxxxxx")
    await asyncio.sleep(x)
    print("~~~~~~~~~~~~~")


async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    print('Waiting: ', x)
    await asyncio.wait([foo(x)])
    return 'Done after {}s'.format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(1.5)
    coroutine3 = do_some_work(9)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    loop = asyncio.get_event_loop()
    # await loop.run_until_complete(asyncio.wait(tasks))

    done, pending = await asyncio.wait(tasks)
    for task in done:
        print('Task ret: ', task.result())

start = now()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(asyncio.wait([main(), main(), main()]))
loop.run_until_complete(task)
