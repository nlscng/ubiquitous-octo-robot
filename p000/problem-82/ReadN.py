# This problem was asked Microsoft.
#
# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
#
# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.


def read_7(data: str) -> str:
    return data[:7] if len(data) > 7 else data


def read_n(data: str, n: int) -> list:
    # TBC
    if not data or n == 0:
        return []

    read = 0
    res = []
    while read < n:
        buff = read_7(data)

