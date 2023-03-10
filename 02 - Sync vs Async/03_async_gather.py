import asyncio
import time


async def send_crow(i: int) -> int:
    print(f'Sending crow {i}')
    await asyncio.sleep(1)
    print(f'Crow {i} returned')
    return i


async def main():
    start = time.perf_counter()
    results = await asyncio.gather(send_crow(1), send_crow(2), send_crow(3))
    elapsed = time.perf_counter() - start
    print(f'Elapsed: {elapsed} s')
    print(f'Results: {results}')


if __name__ == '__main__':
    asyncio.run(main())
