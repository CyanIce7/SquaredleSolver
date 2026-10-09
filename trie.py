"""
Implementation of a Trie class in Python
"""


class TrieNode:
    """
    Implementation of a TrieNode class in Python
    """
    letter: str
    children: list
    is_leaf: bool

    def __init__(self, letter: str = ""):
        self.letter = letter
        self.children = [None for _ in range(26)]
        self.is_leaf = False

    def __str__(self):
        return self.str_indented(0).removesuffix('\n')

    def str_indented(self, depth: int) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        str_so_far = " " * max((depth - 1), 0) + "- " * min(depth, 1) + f'{self.letter}\n'
        for subtrie in self.children:
            if isinstance(subtrie, TrieNode):
                str_so_far += subtrie.str_indented(depth + 1)
        return str_so_far


class Trie:
    """
    Implementation of a Trie class in Python.
    """
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        return self.root.__str__()

    def insert(self, key: str):
        """
        Insert a new key (three-letter string) into this Trie.
        """
        if len(key) > 3:
            key = key[0:3]

        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode(c)  # type: ignore
            curr = curr.children[index]
        curr.is_leaf = True

    def search(self, key: str):
        """
        Return whether this key (three-letter string) exists in the Trie.
        """
        if len(key) > 3:
            key = key[0:3]

        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.is_leaf

    def is_prefix(self, prefix: str):
        """
        Return whether this prefix exists in the Trie.
        """
        if len(prefix) > 3:
            return False

        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True


my_dictionary = ["sun", "shoe", "hound", "hounds", "rone", "test"]
trie = Trie()
for word in my_dictionary:
    trie.insert(word)
print(trie)



