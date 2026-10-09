"""
Squaredle solver
"""

import networkx as nx
import matplotlib.pyplot as plt
import typing
from trie import Trie

word_list = []


class SquaredleGraph(nx.Graph):
    """
    Squaredle graph lol
    """
    coords_to_letters: dict

    def __init__(self, grid):
        super().__init__()
        self.coords_to_letters = {}

        self.build_graph(grid)

    def build_graph(self, grid: list[list[str]]) -> None:
        """
        Add nodes and edges to the graph.
        """
        row_num = len(SQUAREDLE_GRID)
        col_num = len(SQUAREDLE_GRID[0])

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


def load_trie():
    """
    Create a trie with the word list.
    """
    global word_list

    with open("word_list.txt", 'r') as word_list_file:
        word_list = [str(i)[:-1] for i in word_list_file]

    trie = Trie()
    for word in word_list:
        trie.insert(word)

    return trie


SQUAREDLE_GRID = [["u", "t", "s"],
                  ["d", "h", "e"],
                  ["r", "o", "n"]]

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

squaredle_graph = SquaredleGraph(SQUAREDLE_GRID)

print(squaredle_graph.coords_to_letters)
trie = load_trie()
print(trie)
print(word_list)

# blah blah
# bees
