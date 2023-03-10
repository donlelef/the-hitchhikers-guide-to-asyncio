import asyncio
import time


async def send_crow(i: int) -> int:
    print(f'Sending crow {i}')
    await asyncio.sleep(1)
    print(f'Crow {i} returned')
    return i


async def main():
    start = time.perf_counter()

    # new in python 3.11!
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(send_crow(crow)) for crow in range(1, 4)]

    res = [t.result() for t in tasks]

    elapsed = time.perf_counter() - start
    print(f'Elapsed: {elapsed} s')
    print(f'Results: {res}')


if __name__ == '__main__':
    asyncio.run(main())
