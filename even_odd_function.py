def even_numbers_to_nth(numbers, n):
    return " ".join(str(num) for num in numbers[:n] if num % 2 == 0)

def odd_numbers_to_nth(numbers, n):
    return " ".join(str(num) for num in numbers[:n] if num % 2 != 0)