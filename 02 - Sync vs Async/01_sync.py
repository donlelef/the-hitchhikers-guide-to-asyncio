import time


def send_crow(i: int):
    print(f'Sending crow {i}')
    time.sleep(1)
    print(f'Crow {i} returned')


def main():
    start = time.perf_counter()
    for crow in range(1, 4):
        send_crow(crow)
    elapsed = time.perf_counter() - start
    print(f'Elapsed: {elapsed} s')


if __name__ == '__main__':
    main()
