import asyncio


class CatError(BaseException):
    pass


async def raise_error():
    raise CatError('Miao!')


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(raise_error())
            t2 = tg.create_task(raise_error())
    except* CatError as eg:
        print(eg)
    except* Exception as ex:
        print(ex)

    print(t1)
    print(t2)


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
