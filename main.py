"""
Squaredle solver
"""

import networkx as nx
from trie import Trie
import timeit
import pickle
import os

word_list = []


class SquaredleGraph(nx.Graph):
    """
    Squaredle graph lol
    """
    coords_to_letters: dict[tuple, str]
    trie: Trie
    valid_words: list
    recursive_searches: int

    def __init__(self, grid):
        super().__init__()
        self.coords_to_letters = {}
        self.valid_words = []
        self.recursive_searches = 0

        self.build_graph(grid)

    def build_graph(self, grid: list[list[str]]) -> None:
        """
        Add nodes and edges to the graph.
        Mutating method.
        """
        row_num = len(grid)
        col_num = len(grid[0])

        for row in range(row_num):
            for col in range(col_num):
                node = (row, col)
                self.add_node(node)
                self.coords_to_letters[node] = grid[row][col]

                for x, y in DIRECTIONS:
                    new_row, new_col = x + row, y + col

                    if 0 <= new_row < row_num and 0 <= new_col < col_num:
                        adjacent_node = (new_row, new_col)
                        if adjacent_node not in self.coords_to_letters:
                            self.add_edge(node, adjacent_node)

    def add_trie(self, trie: Trie) -> None:
        """
        Add the word trie into this class.
        Mutating method.
        """
        self.trie = trie

    def _find_words_starting_with_letter(self, node: tuple, curr_string="", visited=None) -> None:
        """
        Find valid words in the grid starting with self.coords_to_letters[node] using depth-first search.
        Mutating method.
        """
        if visited is None:
            visited = set()

        visited.add(node)
        curr_string += self.coords_to_letters[node]
        # print(curr_string, [self.coords_to_letters[i] for i in visited])
        self.recursive_searches += 1

        if len(curr_string) >= 4:
            if self.trie.search(curr_string):
                self.valid_words.append(curr_string)

        if self.trie.is_prefix(curr_string):
            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    self._find_words_starting_with_letter(neighbor, curr_string, visited)
            visited.remove(node)
        else:
            visited.remove(node)

    def find_words(self, sort: bool = True) -> list[str]:
        """
        Find all words in this squaredle.
        """
        for k in self.coords_to_letters:
            self._find_words_starting_with_letter(k)
        self.valid_words = list(set(self.valid_words))

        if sort:
            self.valid_words.sort()

        return self.valid_words


def generate_trie():
    """
    Load the word list and create a Trie with it.
    """
    global word_list

    with open("word_list.txt", 'r') as word_list_file:
        word_list = [str(i)[:-1] for i in word_list_file]

    trie = Trie()
    for word in word_list:
        if 4 <= len(word) <= 16:
            trie.insert(word)

    return trie


SQUAREDLE_GRID = [["u", "t", "s"],
                  ["d", "h", "e"],
                  ["r", "o", "n"]]

SQUAREDLE_GRID_2 = [["a", "m", "y", "u", "m"],
                    ["e", "l", "b", "f", "o"],
                    ["n", "c", "i", "r", "y"],
                    ["t", "h", "c", "b", "r"],
                    ["e", "d", "i", "m", "e"]]

SQUAREDLE_GRID_MASSIVE = grid = [
    ['s', 't', 'r', 'e', 'a', 'm', 'l', 'i', 'n', 'e', 'd', 'w', 'o', 'r', 'k'],
    ['a', 'p', 'p', 'l', 'i', 'c', 'a', 't', 'i', 'o', 'n', 'b', 'a', 's', 'e'],
    ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r', 's', 'c', 'i', 'e', 'n', 'c', 'e'],
    ['d', 'e', 'v', 'e', 'l', 'o', 'p', 'm', 'e', 'n', 't', 't', 'e', 'a', 'm'],
    ['e', 'n', 'v', 'i', 'r', 'o', 'n', 'm', 'e', 'n', 't', 'a', 'l', 'l', 'y'],
    ['f', 'u', 'n', 'd', 'a', 'm', 'e', 'n', 't', 'a', 'l', 'i', 's', 't', 's'],
    ['g', 'e', 'o', 'g', 'r', 'a', 'p', 'h', 'i', 'c', 'a', 'l', 'l', 'y', 'x'],
    ['h', 'e', 'l', 'i', 'c', 'o', 'p', 't', 'e', 'r', 'p', 'i', 'l', 'o', 't'],
    ['i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'a', 'l', 'l', 'y'],
    ['j', 'u', 's', 't', 'i', 'f', 'i', 'c', 'a', 't', 'i', 'o', 'n', 's', 'z'],
    ['k', 'n', 'o', 'w', 'l', 'e', 'd', 'g', 'e', 'b', 'a', 's', 'e', 'd', 'q'],
    ['l', 'e', 'x', 'i', 'c', 'o', 'g', 'r', 'a', 'p', 'h', 'e', 'r', 's', 'w'],
    ['m', 'a', 'c', 'r', 'o', 'e', 'c', 'o', 'n', 'o', 'm', 'i', 'c', 's', 'v'],
    ['n', 'e', 'u', 'r', 'o', 's', 'c', 'i', 'e', 'n', 't', 'i', 's', 't', 's'],
    ['o', 'r', 'g', 'a', 'n', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'a', 'l', 'y']
]

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

t1 = timeit.default_timer()
squaredle_graph = SquaredleGraph(SQUAREDLE_GRID_MASSIVE)
trie = generate_trie()
squaredle_graph.add_trie(trie)
squaredle_graph.find_words()
t2 = timeit.default_timer()

print(squaredle_graph.valid_words)
print(len(squaredle_graph.valid_words))
print(t2 - t1)
print(squaredle_graph.recursive_searches)

