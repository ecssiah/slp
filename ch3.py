from collections import defaultdict, Counter
import nltk
import numpy as np
import random
import re
import pandas as pd


def calculate_1gram(text):
    sentence_list = [
        ["<s>"] + sentence.split(" ") + ["</s>"]
        for sentence in text
    ]

    words = [word for sentence in sentence_list for word in sentence]
    vocab = set(words)

    word_count = len(words)
    words_counter = Counter(words)

    P = {word : words_counter[word] / word_count for word in vocab}

    return P


def random_1gram_sentence(P):
    sentence = []

    while True:
        word = random.choices(list(P.keys()), weights=list(P.values()), k=1)[0]

        if word == "<s>" or word == "</s>":
            break

        sentence.append(word)

    return " ".join(sentence)


def calculate_2gram(text):
    sentence_list = [
        ["<s>"] + sentence.split(" ") + ["</s>"]
        for sentence in text
    ]

    words = [word for sentence in sentence_list for word in sentence]
    words_counter = Counter(words)

    bigram_list = []

    for sentence in sentence_list:
        for i in range(1, len(sentence)):
            bigram_list.append((sentence[i - 1], sentence[i]))

    bigram_list_counter = Counter(bigram_list)

    P_flat = {
        bigram : bigram_list_counter[bigram] / words_counter[bigram[0]] 
        for bigram in set(bigram_list)
    }

    P = defaultdict(dict)

    for (x, y), v in P_flat.items():
        P[x][y] = v

    return P


def random_2gram_sentence(P):
    word1 = "<s>"
    word_list = []

    while True:
        P_word = P[word1]

        word2 = random.choices(
            list(P_word.keys()), 
            weights=list(P_word.values()), 
            k=1
        )[0]

        if word2 != "</s>":
            word_list.append(word2)
            word1 = word2
        else:
            break

    sentence = " ".join(word_list)

    return sentence


if __name__ == "__main__":
    print("Chapter 3\n")

    nltk.download('punkt_tab')
    nltk.download("gutenberg")

    text_raw = nltk.corpus.gutenberg.raw("bible-kjv.txt")

    text_clean = re.sub(r"\s+", " ", text_raw).strip()
    text = re.split(r"\b\d+:\d+\s*", text_clean)

    P_1 = calculate_1gram(text)
    P_2 = calculate_2gram(text)

    print(f"1gram sentence:\n{random_1gram_sentence(P_1)}\n")
    print(f"2gram sentence:\n{random_2gram_sentence(P_2)}\n")