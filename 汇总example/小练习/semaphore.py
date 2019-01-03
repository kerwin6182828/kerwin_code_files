import asyncio
async def my_worker(semaphore):
    l = object()
    print("object id: ", id(l))
    semaphore.acquire()
    print("成功获得了信号量: ", id(l))
    asyncio.sleep(3)
    print("释放信号量: ", id(l))
    semaphore.release()
async def main():
    my_semaphore = asyncio.Semaphore(value=2)
    # await asyncio.wait([my_worker(my_semaphore), my_worker(my_semaphore), my_worker(my_semaphore), my_worker(my_semaphore)])
    await asyncio.wait([my_worker(my_semaphore) for _ in range(10)])
    print("Main 协程")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("所有 Workers 完成")
loop.close()
