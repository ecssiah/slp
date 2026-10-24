import numpy as np
import pandas as pd
from collections import Counter
import nltk


if __name__ == "__main__":
    print("Chapter 3\n")

    nltk.download('punkt_tab')
    nltk.download("gutenberg")

    sentence_list = nltk.corpus.gutenberg.sents("bible-kjv.txt")

    word_list = []

    for sentence in sentence_list:
        word_list.append(["<s>"] + sentence + ["</s>"])

    word_list = [word for line in word_list for word in line]
    word_list = np.array(word_list)

    vocabulary = np.unique(word_list)
    counts = pd.Series(word_list).value_counts()

    p_1gram = counts / len(word_list)

    print(f"Jesus: {p_1gram["Jesus"]}")
    print(f"David: {p_1gram["David"]}")

    p_2gram = pd.Series(Counter(zip(word_list, word_list[1:])))
    
    for element in p_2gram:
        print(element)

