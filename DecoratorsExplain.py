import time
import functools


def operatsiooniaeg(funktsioon):
    def wrapper(*args, **kwargs):
        algus = time.perf_counter()
        funktsioon(*args, **kwargs)
        print('aeg :', time.perf_counter() - algus)

    return wrapper


@operatsiooniaeg
def minu_funktsioon(a):
    sum_result = 0
    for i in range(a):
        sum_result += i
        # print(i)
    print(sum_result)


@functools.cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    start = time.perf_counter()
    print(str(fibonacci(150)/fibonacci(149)))
    print('aeg: ', time.perf_counter() - start)
    minu_funktsioon(100000)
