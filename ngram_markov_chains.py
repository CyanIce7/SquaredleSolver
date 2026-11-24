from ngram_analysis import open_word_list, count_bigrams
import numpy as np
from collections import Counter

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
LETTER_INDEX = {c: i for i, c in enumerate(ALPHABET)}
N = 26

def matrix_from_counter(counts_counter):
    transition_matrix = np.zeros((N, N))
    for (letter_1, letter_2), count in counts_counter.items():
        if letter_1 in LETTER_INDEX and letter_2 in LETTER_INDEX:
            transition_matrix[LETTER_INDEX[letter_1], LETTER_INDEX[letter_2]] += count

    for row in transition_matrix:
        row_sum = np.sum(row)
        np.log(row + 1) + row_sum
        row_sum = np.sum(row)
        row / row_sum
        
    return transition_matrix

P = matrix_from_counter(count_bigrams(open_word_list()))
print(P)