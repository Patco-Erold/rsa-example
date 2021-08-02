import argparse

_parser = argparse.ArgumentParser(
    description="Generation of prime numbers"
)

_parser.add_argument(
    "L", type=int, help="Provide the Limit"
)

_args = _parser.parse_args()


def _is_prime(_number):
    if _number < 2:
        return False

    for _x in range(2, _number):
        if _number % _x == 0:
            return False
    else:
        return True


if __name__ == '__main__':

    print(list(filter(_is_prime, range(1, int(_args.L)))))
