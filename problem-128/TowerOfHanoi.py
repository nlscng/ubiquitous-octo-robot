# The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.
#
# All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom
# and the smallest one at the top.
#
# The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:
#
# You can only move one disk at a time. A move consists of taking the uppermost disk from one of the stacks and
# placing it on top of another stack. You cannot place a larger disk on top of a smaller disk. Write a function that
# prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered,
# with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.
#
# For example, with n = 3, we can do this in 7 moves:
#
# Move 1 to 3
# Move 1 to 2
# Move 3 to 2
# Move 1 to 3
# Move 2 to 1
# Move 2 to 3
# Move 1 to 3

"""
Text book recursion problem, this should be a nice practice after all this time...

if I only have one disk
1 -> 3

two disks:
1 -> 2
1 -> 3
2 -> 3

three disks

1 -> 3
1 -> 2
3 -> 2
1 -> 3
2 -> 1
2 -> 3
1 -> 3

Let's mark the poles src, aux, tgt. Moving m disk from src to tgt is the same as moving m - 1 top disk to aux


a; 2, 1
b:
c:

a; 1
c:
b:

"""


# GG: surprisingly difficult for me to get it right, I think the critical piece is the decrementing counter of m disk
#  being moved and passed in as an argument in the recur calls


def hanoi(k: int):
    assert k > 0

    def move(n: int, s: str, a: str, t: str):
        if n > 0:
            move(n - 1, s, t, a)
            print("Moving #{} disk from {} to {}.".format(str(n), s, t))
            move(n - 1, a, s, t)

    move(k, "A", "B", "C")


# hanoi(3)


class Pole:
    def __init__(self, name, n: int = 0):
        self.name = name
        self.stack = [n for n in range(n, 0, -1)]

    def visualize(self):
        print("{}: {}".format(self.name, self.stack))


print(hanoi(4))


def hanoi_with_visual(k: int):
    assert k > 0
    a = Pole("A", k)
    b = Pole("B")
    c = Pole("C")
    poles = [a, b, c]

    def move(m: int, src: Pole, aux: Pole, tgt: Pole):
        if m > 0:
            move(m - 1, src, tgt, aux)
            print("Moving {} disk from {} to {}".format(str(m), src.name, tgt.name))
            disk = src.stack.pop()
            tgt.stack.append(disk)
            for p in poles:
                p.visualize()
            move(m - 1, aux, src, tgt)

    move(k, a, b, c)


hanoi_with_visual(4)
