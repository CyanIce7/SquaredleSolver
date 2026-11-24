from nltk import bigrams, trigrams
from collections import Counter

def open_word_list():
    with open("word_list.txt", 'r') as word_list_file:
        word_list = [str(i)[:-1] for i in word_list_file]

    return word_list

def count_bigrams(word_list, sort_by_letter = True):
    bigram_counts = Counter()

    for word in word_list:
        bigram_counts.update(bigrams(word))

    if sort_by_letter:
        bigram_counts = sorted(bigram_counts.items(), key=lambda x: (x[0][0], x[0][1]))
    
    return bigram_counts

def count_trigrams(word_list, sort_by_letter = True):
    trigram_counts = Counter()

    for word in word_list:
        trigram_counts.update(trigrams(word))

    if sort_by_letter:
        trigram_counts = sorted(trigram_counts.items(), key=lambda x: (x[0][0], x[0][1]))
    
    return trigram_counts

if __name__ == "__main__":
    word_list = open_word_list()
    bigram_counts = count_bigrams(word_list)
    trigram_counts = count_trigrams(word_list)
    print(bigram_counts)
    print(trigram_counts)