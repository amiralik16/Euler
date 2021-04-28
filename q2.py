
from typing import Generator

def fib_generator() -> Generator[int, None, None]:
    """Generats fibounacci numbers

    Returns:
        int: Next fibbounacci number in sequence
    """
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def sum_even_fib(maximum: int) -> int:
    """Sums even fibounacci numbers up to the maximum

    Args:
        maximum (int): Limit of the fibounacci number

    Returns:
        int: Sum
    """
    fib_gen = fib_generator()
    res = 0
    fib = next(fib_gen)
    while fib < maximum:
        if fib % 2:
            res += fib
        fib = next(fib_gen)
    
    return res


if __name__ == '__main__':
    maximum = 4e6
    print(sum_even_fib(maximum))