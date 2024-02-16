def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty, cannot find minimum")
    return min(numbers)


def find_maximum(numbers):
    if not numbers:
        raise ValueError("List is empty, cannot find maximum")
    return max(numbers)


def calculate_sum(numbers):
    return sum(numbers)


def calculate_average(numbers):
    if not numbers:
        raise ValueError("List is empty, cannot calculate average")
    return sum(numbers) / len(numbers)


def square_each_element(numbers):
    return [num ** 2 for num in numbers]
