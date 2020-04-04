# This problem was asked by Google.
#
# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or
# ancestors are not locked.
#
# Design a binary tree node class with the following methods:
#
# is_locked, which returns whether the node is locked lock, which attempts to lock the node. If it cannot be locked,
# then it should return false. Otherwise, it should lock it and return true. unlock, which unlocks the node. If it
# cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true. You may augment
# the node to add parent pointers or any other property you would like. You may assume the class is used in a
# single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h),
# where h is the height of the tree.

class LockingBSTNode:
    def __init__(self, value, parent=None, is_locked=False):
        self.value = value
        self.parent = parent
        self.locked = is_locked
        self.locked_descendent_count = 0

    def is_locked(self):
        return self.locked

    def lock(self):
        # check along parents for locked nodes,
        # if parents have no locked node, and self has no locked descendent,
        # increment parents' "locked_descendent_count" by 1, then lock self
        parents = self._collect_parents()
        has_locked_parents = any([p.is_locked() for p in parents])
        if not has_locked_parents and self.locked_descendent_count == 0:
            self.locked = True
            for p in parents:
                p.locked_descendent_count += 1
            return True
        else:
            return False

    def unlock(self):
        # unlockable: self has no locked descendent, and no parent is locked
        # after unlocking, decrease parent's locked descendent by 1
        parents = self._collect_parents()
        has_locked_parents = any([p.is_locked() for p in parents])
        if not has_locked_parents and self.locked_descendent_count == 0:
            self.locked = False
            for p in parents:
                p.locked_descendent_count -= 1
                assert p.locked_descendent_count >= 0, "This node has negative locked descendent count: {}".format(
                    str(p))
            return True
        else:
            return False

    def _collect_parents(self):
        parents = []
        walker = self.parent
        while walker is not None:
            parents.append(walker)
            walker = walker.parent
        return parents

    def __str__(self):
        return "value: {}, is_locked: {}, locked_descendent_count: {}" \
            .format(self.value,
                    self.locked,
                    self.locked_descendent_count
                    )

# test cases copied from https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_024.py
a = LockingBSTNode("a")
b = LockingBSTNode("b", a)
c = LockingBSTNode("c", a)
d = LockingBSTNode("d", b)
e = LockingBSTNode("e", b)
f = LockingBSTNode("f", c)
g = LockingBSTNode("g", c)

assert b.lock()
assert b.is_locked()
assert c.lock()
assert b.unlock()
assert not b.is_locked()
assert d.lock()

assert not g.lock()
assert c.unlock()
assert g.lock()

assert f.lock()
assert e.lock()
assert a.locked_descendent_count == 4
assert b.locked_descendent_count == 2
assert c.locked_descendent_count == 2
