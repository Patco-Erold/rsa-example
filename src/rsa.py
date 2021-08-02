"""
Simple RSA implementation.
"""

import argparse

from typing import List

from utils import (_mod, _ascii, _from_ascii, _split)

_parser = argparse.ArgumentParser(description="Simple RSA Encryption Algorithm.")

_parser.add_argument(
    "N", type=int, help="The prime value of N."
)
_parser.add_argument(
    "-e", "--encrypt", action="store_true",
    help="If true the provided message will be encrypted."
)
_parser.add_argument(
    "-d", "--decrypt", action="store_true",
    help="If true the provided message will be encrypted."
)
_parser.add_argument(
    "-k", "--key", required=True, help="The encryption e or decryption key d"
)
_parser.add_argument(
    "-m", "--message", required=True,
    help="The message to be encrypted or the cipher to be decrypted."
)

_args = _parser.parse_args()


def _encrypt(_e: int, _n: int, _message: List[int]):
    """
    Encrypts the message.

    :param _e: The encryption key e.
    :param _n: The Modulo RSA value.
    :param _message: The message to be encrypted.
    :return: The message cypher.
    """
    return "-".join([str(_mod(_m ** _e, _n)) for _m in _message])


def _decrypt(_d: int, _n: int, _message: List[int]):
    """
    Decrypts the message c.

    :param _d: The decryption key d.
    :param _n: The Modulo RSA value.
    :param _message: The message cypher to be decrypted.
    :return: The plain text message.
    """
    return _from_ascii([_mod(_c ** _d, _n) for _c in _message])


def _main():
    _N = _args.N
    _key = int(_args.key)
    _message = _args.message

    if _args.encrypt:
        print(_encrypt(_key, _N, _ascii(_message)))
    elif _args.decrypt:
        print(_decrypt(_key, _N, _split(_message)))


if __name__ == '__main__':
    _main()
