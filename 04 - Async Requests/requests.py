import asyncio

import httpx


async def get_from_httpbin(
        async_client: httpx.AsyncClient,
        semaphore: asyncio.Semaphore,
        incremental_id: int,
) -> httpx.Response:
    async with semaphore:
        print(f'Sending {incremental_id}...')
        return await async_client.get('https://httpbin.org/get', params={'incremental_id': incremental_id})


async def main():
    semaphore = asyncio.Semaphore(3)

    async with httpx.AsyncClient() as async_client:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(get_from_httpbin(async_client, semaphore, p)) for p in range(20)]

    exceptions = sum(1 for t in tasks if t.exception())
    cancellations = sum(1 for t in tasks if t.cancelled())
    print(f'Exceptions: {exceptions} Cancellations: {cancellations} Tasks: {len(tasks)}')

    sum_of_first_20_numbers = sum([int(t.result().json()['args']['incremental_id']) for t in tasks])
    print(f'Sum of first {len(tasks)} numbers: {sum_of_first_20_numbers}')


if __name__ == '__main__':
    asyncio.run(main())
