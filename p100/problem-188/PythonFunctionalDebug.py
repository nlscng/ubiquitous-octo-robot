# This problem was asked by Google.
#
# What will this code print out?
#
# def make_functions():
#     flist = []
#
#     for i in [1, 2, 3]:
#         def print_i():
#             print(i)
#         flist.append(print_i)
#
#     return flist
#
# functions = make_functions()
# for f in functions:
#     f()
# How can we make it print out what we apparently want?

##GOOGLE


# Very interesting problem, worthy of the google sticker, although in the end it's so simple

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(statement):
            # Remember none of the func body is executed in declaration
            print(statement)

        flist.append((print_i, i))

    return flist


functions = make_functions()
for f, a in functions:
    f(a)
