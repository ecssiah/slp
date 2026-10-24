import random
import numpy as np
import pandas as pd
from collections import Counter
import nltk


def calculate_1gram(sents):
    sentence_list = [
        ["<s>"] + sentence + ["</s>"]
        for sentence in sents
    ]

    words = [word for sentence in sentence_list for word in sentence]
    vocab = set(words)

    vocab_count = len(vocab)
    word_count = len(words)

    words_counter = Counter(words)

    P = {}

    for word in vocab:
        P[word] = words_counter[word] / word_count

    return P


def calculate_2gram(sents):
    sentence_list = [
        ["<s>"] + sentence + ["</s>"]
        for sentence in sents
    ]

    words = [word for sentence in sentence_list for word in sentence]
    vocab = set(words)

    vocab_count = len(vocab)
    word_count = len(words)

    words_counter = Counter(words)

    bigram_list = []

    for sentence in sentence_list:
        for i in range(1, len(sentence)):
            bigram_list.append((sentence[i - 1], sentence[i]))

    bigram_list_counter = Counter(bigram_list)

    P = {}

    for bigram in bigram_list:
        P[bigram] = bigram_list_counter[bigram] / words_counter[bigram[0]]

    return P


def random_1gram_sentence(P):
    sentence = []

    while True:
        word = random.choices(list(P.keys()), weights=list(P.values()), k=1)[0]

        if word == "<s>" or word == "</s>":
            break

        sentence.append(word)

    return " ".join(sentence)


def random_2gram_sentence(P):
    P_initial = {k: v for k, v in P.items() if k[0] == "<s>"}

    sentence = [
        random.choices(list(P_initial.keys()), weights=list(P_initial.values()), k=1)[0][1]
    ]

    while True:
        bigram = random.choices(list(P.keys()), weights=list(P.values()), k=1)[0]

        if bigram[1] == "</s>":
            sentence.append(bigram[0])
            break
        else:
            sentence.append(bigram[0])
            sentence.append(bigram[1])

    return " ".join(sentence)


if __name__ == "__main__":
    print("Chapter 3\n")

    nltk.download('punkt_tab')
    nltk.download("gutenberg")

    sents = nltk.corpus.gutenberg.sents("bible-kjv.txt")

    P_1gram = calculate_1gram(sents)
    P_2gram = calculate_2gram(sents)

    random_1gram = random_1gram_sentence(P_1gram)
    random_2gram = random_2gram_sentence(P_2gram)

    print(random_1gram)
    print(random_2gram)