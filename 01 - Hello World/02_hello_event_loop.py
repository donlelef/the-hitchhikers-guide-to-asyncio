import asyncio


async def main():
    print('Hello...')
    await asyncio.sleep(1)
    print('...World!')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
