from typing import Set

def get_multiples(base: int, maximum: int) -> Set[int]:
    """Gets multiples of base up to and including maximum

    Args:
        base (int): [description]
        maximum (int): Maximum number allowed

    Returns:
        Set[int]: Set of multiples of base that are less than maximum
    """
    if base < 0:
        raise ValueError('base should be a positive integer')
    if maximum < 1:
        raise ValueError('maximum should be a positive integer greater than 1')
    res: Set[int] = set()
    num = 1
    while (num * base < maximum):
        res.add(num * base)
        num += 1
    return res


def sum_series_upto(number: int) -> int:
    return number * (number + 1) / 2


def set_solution():
    maximum = 1000
    mult_3 = get_multiples(3, maximum)
    mult_5 = get_multiples(5, maximum)
    return sum(mult_3.union(mult_5))


def efficient_solution():
    maximum = 1000
    mult_3_sum = sum_series_upto(maximum//3)
    mult_5_sum = sum_series_upto(maximum//5)
    mult_15_sum = sum_series_upto(maximum//15)
    return mult_3_sum + mult_5_sum - mult_15_sum

if __name__ == '__main__':
    print(efficient_solution())