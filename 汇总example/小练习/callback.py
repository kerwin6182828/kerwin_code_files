import time
import asyncio
import functools

now = lambda : time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(t, future):
    print('Callback:', t, future.result())


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(functools.partial(callback, 2))
loop.run_until_complete(task)

print('TIME: ', now() - start)
