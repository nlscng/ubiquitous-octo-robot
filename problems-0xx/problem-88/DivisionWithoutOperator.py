# This question was asked by ContextLogic.
#
# Implement division of two positive integers without using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.


def raw_division(n: int, m: int) -> int:
    if n < m:
        return raw_division(m, n)

    quot, cur_sum = 0, 0
    while cur_sum <= n:
        quot += 1
        cur_sum += m

    return quot - 1


assert raw_division(1, 1) == 1
assert raw_division(2, 1) == 2
assert raw_division(10, 3) == 3
assert raw_division(11, 7) == 1