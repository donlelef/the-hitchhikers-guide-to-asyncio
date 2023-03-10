import asyncio
import time


async def send_crow(i: int) -> int:
    print(f'Sending crow {i}')
    await asyncio.sleep(i)
    print(f'Crow {i} returned')
    return i


async def main():
    start = time.perf_counter()
    done, pending = await asyncio.wait([
        asyncio.create_task(send_crow(1)),
        asyncio.create_task(send_crow(2)),
        asyncio.create_task(send_crow(3))
    ],
        timeout=10,
        return_when=asyncio.FIRST_COMPLETED
    )
    elapsed = time.perf_counter() - start
    print(f'Elapsed: {elapsed} s')
    print(f'Done: {done}')
    print(f'Pending: {pending}')


if __name__ == '__main__':
    asyncio.run(main())
