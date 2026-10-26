"""
Testing file for Tries, espeically for datasets with lots of words
"""
import trie

with open("word_list.txt", 'r') as word_list_file:
    word_list = [str(i)[:-1] for i in word_list_file]

trie = trie.Trie()
for word in word_list:
    trie.insert(word)

print("a")
