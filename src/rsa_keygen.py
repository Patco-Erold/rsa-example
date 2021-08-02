"""
Simple RSA key generation.
"""

import argparse

from typing import Tuple
from utils import (_mod, _is_prime)

_parser = argparse.ArgumentParser(description="Simple RSA key generator.")

_parser.add_argument(
    "P", type=int, help="The prime value of P."
)
_parser.add_argument(
    "Q", type=int, help="The prime value of Q."
)
_parser.add_argument(
    "-e", "--key", default=2, help="The co-prime value of e."
)

_args = _parser.parse_args()


def _e_gcd(_dividend: int, _divisor: int) -> Tuple[int, int, int]:
    """
    Simple Extended Euclidean Algorithm.

    Ax + By = 1

    phi_N * x + e * y = 1

    :param _dividend: The value of the dividend.
    :param _divisor: The value of the divisor.
    :return: (gcd, decryption_key, remainder)
    """

    if _dividend == 0:
        return _divisor, 0, 1

    __gcd, _r, _d = _e_gcd(_mod(_divisor, _dividend), _dividend)

    return __gcd, _d - (_divisor // _dividend) * _r, _r


def _modulo_inv(_e: int, _phi_n: int) -> int:
    """
    Computes the value of the decryption key.

    :param _n: The N value.
    :param _e: The encryption key.
    :param _phi_n: The totient value.
    :return: The decryption key.
    """
    _, _d, _ = _e_gcd(_e, _phi_n)

    return _d + _phi_n if _d < 0 else _d


def _gcd(_e: int, _phi_n: int) -> int:
    """
    Computes the greatest common divisor of e and phi of N.

    :param _e: The encryption key.
    :param _phi_n: The value of phi N.
    :return: The gcd.
    """

    while True:
        _m = _mod(_e, _phi_n)

        if _m == 0:
            return _phi_n

        _e = _phi_n
        _phi_n = _m


def _compute_e(_e: int, _phi_n) -> int:
    """
    Computes the best value for the encryption key e.
    The encryption key e must be greater than 1 and less than phi_n,
    also must be a co-prime of phi_n.

    :param _e: The starting value of e.
    :param _phi_n: The value of phi N.
    :return: The best encryption key e.
    """

    while _e < _phi_n:
        if _gcd(_e, _phi_n) == 1:
            break

        _e += 1

    return _e


def _run():
    """
    Execute the key generation.

    :return: None
    """
    _P = _args.P
    _Q = _args.Q
    _e = int(_args.key)

    if not _is_prime(_P) or not _is_prime(_Q):
        raise ValueError("P or Q must be a prime number.")

    _N = _P * _Q
    _phi_N = (_P - 1) * (_Q - 1)
    _e = _compute_e(_e, _phi_N)
    _d = _modulo_inv(_e, _phi_N)
    print("\nGenerated Keys!")
    print(f"Phi N               : {_phi_N}")
    print(f"Public  Key, (N, e) : ({_N}, {_e})")
    print(f"Private Key, d      : {_d}\n")


if __name__ == '__main__':
    _run()
