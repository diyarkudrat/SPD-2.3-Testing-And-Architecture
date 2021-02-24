import pytest


def calculate_kinetic_energy(mass, velocity):
    """Returns kinetic energy of mass [kg] with velocity level."""
    return 0.5 * mass * velocity ** 2


def get_average(li):
    if len(li) < 1:
        return None

    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean


def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')

    return word == word[::-1]


def test_palindrome():
    with pytest.raises(TypeError):
        palindrome(24)


def test_get_average():
    li = []
    assert get_average(li) == None


def test_calculate_kinetic_energy():
    mass = 10  # [kg]
    velocity = 4  # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80
