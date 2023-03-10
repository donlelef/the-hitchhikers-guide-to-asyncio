from typing import Generator


def jumping_range(up_to: int) -> Generator[int, int, None]:
    index, jump = 0, 0
    while index < up_to:
        print(f'{index=} {jump=}')
        jump = yield index
        if jump is None:
            jump = 1
        index += jump


if __name__ == '__main__':
    iterator = jumping_range(5)
    print(next(iterator))  # 0
    print(iterator.send(2))  # 2
    print(next(iterator))  # 3
    print(iterator.send(-1))  # 2
