# This problem was asked by Stripe.
#
# Write a function to flatten a nested dictionary. Namespace the keys with a period.
#
# For example, given the following dictionary:
#
# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
# it should become:
#
# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }
# You can assume keys do not contain dots in them, i.e. no clobbering will occur.

"""
This is identical to pramp 25. Although I am going to make some assumption to make this easier.
So there's no dots in names, and I am assuming there's no empty name allowed.
"""


def flatten_dictionary(lex: dict) -> dict:
    assert lex
    res = dict()

    def recur(l: dict, prefix: str):
        if prefix:
            prefix = prefix + '.'
        for k, v in l.items():
            if isinstance(v, dict):
                recur(v, prefix + str(k))
            else:
                res[prefix + str(k)] = v

    recur(lex, '')
    return res


test = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

out = {
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
assert flatten_dictionary(test) == out
