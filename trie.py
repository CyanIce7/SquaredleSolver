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

            # Catch invalid index
            if index < 0 or index >= 26:
                print(key, index)
                return

            if curr.children[index] is None:
                curr.children[index] = TrieNode(c)  # type: ignore
            curr = curr.children[index]
        curr.is_end_word = True

    def search(self, key: str):
        """
        Return whether this key exists in the Trie.
        """
        curr = self.root
        letter_index = 0
        key = key.lower()
        for c in key:
            if c == "?":
                potential_letters = []
                for child in curr.children:
                    if child is not None:
                        potential_letters.append(child)
                return any(self.search(key[:letter_index] + child.letter + key[(letter_index + 1):]) for child in potential_letters)
            else:
                index = ord(c) - ord('a')
                if curr.children[index] is None:
                    return False
                curr = curr.children[index]
            letter_index += 1
        return curr.is_end_word

    def is_prefix(self, prefix: str):
        """
        Return whether this prefix exists in the Trie.
        """
        curr = self.root
        letter_index = 0
        for c in prefix:
            if c == "?":
                potential_letters = []
                for child in curr.children:
                    if child is not None:
                        potential_letters.append(child)
                return len(potential_letters) > 0
            else:
                index = ord(c) - ord('a')
                if curr.children[index] is None:
                    return False
                curr = curr.children[index]
            letter_index += 1
        return True


if __name__ == "__main__":
    my_dictionary = ["sun", "shoe", "hound", "hounds", "shin", "honey", "hungover"]
    trie = Trie()
    for word in my_dictionary:
        trie.insert(word)
    print(trie)
    print(trie.search("hound"))
    print(trie.search("hound?"))
    print(trie.search("h?ney"))
    print(trie.search("h?ngover"))
    print(trie.search("su?"))
    print(trie.search("s?d"))
    print(trie.search("?un"))
    print(trie.is_prefix("?"))



