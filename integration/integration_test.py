# test_operations.py

import pytest
from my_numbers import find_minimum, find_maximum, calculate_sum, calculate_average, square_each_element


# Test find_minimum function
def test_find_minimum():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    assert find_minimum(numbers) == 1


def test_find_minimum_empty_list():
    with pytest.raises(ValueError, match="List is empty, cannot find minimum"):
        find_minimum([])


# Test find_maximum function
def test_find_maximum():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    assert find_maximum(numbers) == 9


def test_find_maximum_empty_list():
    with pytest.raises(ValueError, match="List is empty, cannot find maximum"):
        find_maximum([])


# Test calculate_sum function
def test_calculate_sum():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    assert calculate_sum(numbers) == 25


# Test calculate_average function
def test_calculate_average():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    assert calculate_average(numbers) == 25 / 7


def test_calculate_average_empty_list():
    with pytest.raises(ValueError, match="List is empty, cannot calculate average"):
        calculate_average([])


# Test square_each_element function
def test_square_each_element():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    assert square_each_element(numbers) == [9, 1, 16, 1, 25, 81, 4]
