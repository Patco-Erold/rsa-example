"""
Simple Utilities.
"""


def _mod(_dividend: int, _divisor: int) -> int:
    """
    Computes the modulo of the given values.

    _dividend % _divisor

    :param _dividend: The value of the dividend.
    :param _divisor: The value of the divisor.
    :return: The Modulo.
    """
    _q = (_dividend // _divisor)
    _d = _q * _divisor

    return _dividend - _d


def _is_prime(_number: int) -> bool:
    """
    Checks if a given number is a prime number.

    :param _number: The value to be tested.
    :return: True if the given number is prime number, False otherwise.
    """

    if _number < 2:
        return False

    for _x in range(2, _number):
        if _mod(_number, _x) == 0:
            return False

    return True


def _ascii(_message: str) -> list:
    """
    Computes and returns the ascii list of of given the given string.

    :param _message: The string whose ascii values are needed.
    :return: The list of ascii values.
    """
    return [ord(__c) for __c in _message]


def _from_ascii(_message: list) -> str:
    """
    Computes and returns the characters of the given ascii values.

    :param _message: A list of ascii values.
    :return: The string message
    """
    return "".join(chr(__i) for __i in _message)


def _split(_message: str) -> list:
    """
    Splits the given string.

    :param _message: The string to be split.
    :return: The list of values.
    """
    if _message.find('-') > 0:
        _m = _message.split('-')
        _m = [int(__i) for __i in _m]
    else:
        _m = [int(_message)]

    return _m
