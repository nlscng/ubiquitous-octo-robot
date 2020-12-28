# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain
# the following methods:
#
# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
# then it should also remove the least recently used item. get(key): gets the value at key. If no such key exists,
# return null. Each operation should run in O(1) time.


##Google
##Review

class LeastRecentlyUsedCache:
    class Node:
        def __init__(self, key):
            self.key = key
            self.prev = None
            self.next = None

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.cache = {}  # stores as key value pair in this format: key: (value, Node)
        self.head = None
        self.tail = None

    def __str__(self):
        res = []
        walker = self.head
        while walker is not None:
            res.append(str(walker.key))
            walker = walker.next
        return ",".join(res)

    def _remove_lru_node(self):
        assert len(self.cache) == self.max_size and self.tail is not None
        # remove key from cache
        del self.cache[self.tail.key]

        # remove tail from history
        if self.head == self.tail:
            self.tail = self.head = None
        else:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail

    def _move_to_head(self, key):
        # update history because this key already exist in cache, and now it is getting hit again.
        assert self.cache[key]
        node = self.cache[key][1]
        if node.next and node.prev:
            next_node = node.next
            prev_node = node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
        elif node.next is None and node.prev is None:
            self.head = self.tail = None
        elif node.next is None:
            node.prev.next = None
            self.tail = node.prev
        elif node.prev is None:
            node.next.prev = None
            self.head = node.next

        node.prev = None
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if len(self.cache) == 1:
            self.tail = node

    def _pop_tail(self):
        node = self.tail
        # clean out from cache
        del self.cache[node.key]
        # update history chain
        if node.prev is None:
            self.head = self.tail = None
        else:
            node.prev.next = None
            self.tail = node.prev

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key][1]
            self.cache[key] = (value, node)
            self._move_to_head(key)
        else:
            if len(self.cache) == self.max_size:
                self._pop_tail()
            node = LeastRecentlyUsedCache.Node(key)
            self.cache[key] = (value, node)
            node.next = self.head
            if self.head is not None:
                self.head.prev = node
            self.head = node
            if len(self.cache) == 1:
                self.tail = node

    def get(self, key):
        if key in self.cache:
            res = self.cache[key][0]
            self._move_to_head(key)
            return res
        else:
            return None


cache = LeastRecentlyUsedCache(max_size=3)
# assert not cache.get(1)
cache.set(1, 1)
assert cache.get(1) == 1, "actual: {}".format(cache.get(1))
assert cache.get(0) is None
cache.set(1, 42)
assert cache.get(1) == 42, "actual: {}".format(cache.get(1))
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
print(str(cache), "after setting 1, 2, 3")
assert cache.get(1) == 1, "actual: {}".format(cache.get(1))
print(str(cache), "after get 1")
assert cache.get(2) == 2, "actual: {}".format(cache.get(2))
print(str(cache), "after get 2")
assert cache.get(3) == 3, "actual: {}".format(cache.get(3))
print(str(cache), "after get 3")
cache.set(42, 42)
print(str(cache), "after set 42")
assert cache.get(1) is None
print(str(cache), "after get 1")
assert cache.get(42) == 42
print(str(cache), "after get 42")
assert cache.get(3) == 3
print(str(cache), "after get 3")

