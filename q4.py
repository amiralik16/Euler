def find_largest_palindrome_product(n_digit: int) -> int:
    """Finds the largest palindrome product of two n_digit numbers

    Args:
        n_digits (int): The number of digits

    Returns:
        int: Largest palindrom product
    """
    if n_digit < 1:
        raise ValueError("The number of digits must be and integer greater than 0")
    a = 10 ** n_digit - 1
    limit = 10 ** (n_digit - 1)
    max_product = 0
    while (a > limit):
        b = a
        while (b > limit):
            if is_int_palindrome(a * b):
                max_product = max(max_product, a* b)
            b -= 1
        a -= 1
    return max_product


def is_int_palindrome(x: input):
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(find_largest_palindrome_product(3))