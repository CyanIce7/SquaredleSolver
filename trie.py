"""
Implementation of a Trie class in Python
"""


class TrieNode:
    """
    Implementation of a TrieNode class in Python
    """
    letter: str
    children: list
    is_end_word: bool

    def __init__(self, letter: str = ""):
        self.letter = letter
        self.children = [None for _ in range(26)]
        self.is_end_word = False

    def __str__(self):
        return self.str_indented(0).removesuffix('\n')

    def str_indented(self, depth: int) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_end_word:
            str_so_far = " " * max((depth - 1), 0) + "- " * min(depth, 1) + f'{self.letter}.\n'
        else:
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
        Insert a new key into this Trie.
        """
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode(c)  # type: ignore
            curr = curr.children[index]
        curr.is_end_word = True

    def search(self, key: str):
        """
        Return whether this key exists in the Trie.
        """
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.is_end_word

    def is_prefix(self, prefix: str):
        """
        Return whether this prefix exists in the Trie.
        """
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True


if __name__ == "__main__":
    my_dictionary = ["sun", "shoe", "hound", "hounds", "shin", "honey"]
    trie = Trie()
    for word in my_dictionary:
        trie.insert(word)
    print(trie)
    print(trie.search("hound"))
    print(trie.search("hounds"))
    print(trie.search("hone"))
    print(trie.search("sheet"))
    print(trie.is_prefix("hone"))



