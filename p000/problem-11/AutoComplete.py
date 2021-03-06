# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
#
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal]. Implement an
# autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in
# the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
#
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


class MyTrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26  # assuming we only handle lower case english characters
        self.is_end_of_word = False


def index(char):
    return ord(char) - ord('a')


class MyTrie:
    def __init__(self):
        self.trie = MyTrieNode('')

    def insert_words(self, word_bank: list):
        for word in word_bank:
            self.insert_word(word)

    def insert_word(self, word: str):
        node = self.trie
        for char in word.lower():
            idx = index(char)
            if node.children[idx] is None:
                child_node = MyTrieNode(char)
                node.children[idx] = child_node
                node = child_node
            else:
                node = node.children[idx]

        node.is_end_of_word = True

    def search(self, char):
        return

    def suggest(self, query):
        if not query:
            return []

        suggestions = []
        word = ""
        node = self.trie
        for char in query:
            idx = index(char)
            if node.children[idx] is None:
                # we are out of the trie before the characters in query are all looked up.
                return suggestions
            else:
                node = node.children[idx]

        # we've confirmed that the query so far exist in our trie
        # continue from here on and find all the words left in trie
        # TODO dfs from this node and return all complete words in trie
        return self.__find_all_complete_words(node, prefix=query)

    def __find_all_complete_words(self, node: MyTrieNode, prefix: str):
        # DFS from the given node, pull out complete words whenever we see one
        def is_not_none_list(array: list):
            return list(filter(lambda x: x is not None, array))

        def traverse(n: MyTrieNode, buffer: str):
            if n.is_end_of_word:
                found_words.append(buffer)
            children = is_not_none_list(n.children)
            for child in children:
                traverse(child, buffer + child.val)

        found_words = []
        traverse(node, buffer=prefix)

        return found_words

# set up
test_trie = MyTrie()
test_bank = ["do", "dog", "deer", "deal"]
test_trie.insert_words(test_bank)

assert test_trie.suggest("ab") == []
assert test_trie.suggest("dc") == []
assert test_trie.suggest("do") == ["do", "dog"]
assert test_trie.suggest("de") == ["deal", "deer"]
assert test_trie.suggest("d") == ["deal", "deer", "do", "dog"]
