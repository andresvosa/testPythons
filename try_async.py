"""Piece of code for understanding
    asyncio
Returns:
    [type]: [description]
"""
import asyncio
#import concurrent.futures
import time

async def main():
    await ord_wrp(10)
    task = asyncio.create_task(other_function())
    print('A')
    await asyncio.sleep(1)
    print('B')
    return_value = await task
    print(return_value)

async def other_function():
    print(10)
    await asyncio.sleep(2)
    print(20)
    return 42

async def ordinary_function(delay):
    print(1)
    time.sleep(delay)
    print(2)
    return 3

async def ord_wrp(time_delay):
    loop = asyncio.get_running_loop()
    reslt = await loop.run_in_executor(None, ordinary_function, time_delay)
    return reslt

asyncio.run(main())
