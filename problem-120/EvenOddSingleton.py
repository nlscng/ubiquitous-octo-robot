# This problem was asked by Microsoft.
#
# Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in
# every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the
# second instance.


"""
So instead of singleton on the object, this is really a singleton on a counter maybe?

"""


class EvenOddSingleton:
    even = "Even"
    odd = "Odd"
    # GG: apparently python static variables are just variables initialized in the class but outside
    #  of method, like these

    def __init__(self):
        self.__counter = 0  # I could use a boolean to model the switching, instead of an int

    def get_instance(self):
        if self.__counter % 2 == 0:
            self.__counter += 1
            return EvenOddSingleton.odd
        else:
            self.__counter += 1
            return EvenOddSingleton.even


even_odd = EvenOddSingleton()
assert even_odd.get_instance() == 'Odd'
assert even_odd.get_instance() == 'Even'
assert even_odd.get_instance() == 'Odd'
assert even_odd.get_instance() == 'Even'
assert even_odd.get_instance() == 'Odd'
assert even_odd.get_instance() == 'Even'
