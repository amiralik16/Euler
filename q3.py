# The solution here is probably not the most efficient solution. In the 
# find_smallest_divisible_number, we can skip checking things that are multiples
# of things that we have already checked. e.g. when you check 2 and 3, then skip checking 4, 6 and 9

def find_largest_prime_factor(number: int) -> int:
    """Finds the largest prime factor

    Args:
        number (int): Number to find the largest prime factor for

    Returns:
        int: Largest prime factor
    """
    print(number)
    if number <= 0:
        raise ValueError("Number should be a positive integer")
    if number ==1:
        return number
    factor = find_smallest_divisible_number(number)

    if factor < number:
        return find_largest_prime_factor(number//factor)
    
    return number


def find_smallest_divisible_number(number: int) -> int:
    for i in range(2, number + 1):
        if not number % i:
            return i

if __name__ == '__main__':
    number = 600851475143
    print(find_largest_prime_factor(number))

