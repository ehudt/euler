from collections import defaultdict
from itertools import combinations
from typing import Generator, Tuple
from gmpy2 import is_square  # type: ignore


def gen_replacements(a: str, b: str) -> Generator[Tuple[int, int]]:
    yield (1, 2)


def main():
    # 0. load 0098_words.txt
    words = [word.strip('"') for word in open("0098_words.txt").read().split(",")]
    # 1. find all anagram classes
    anagram_classes = defaultdict(list)
    for word in words:
        anagram_classes["".join(sorted(word))].append(word)
    #   1.1 generate all anagram pairs
    pairs = []
    for anagram_class in anagram_classes:
        if len(anagram_class) <= 1:
            continue
        for a, b in combinations(anagram_class, 2):
            pairs.append((a, b))
    # 2. for each anagram pair
    max_square = 0
    for a, b in pairs:
        #   2.1 generate all digit replacements (unique, no leading zeros)
        for a_num, b_num in gen_replacements(a, b):
            #   2.2 for each digit replacement, if both numbers are squares, update max_square
            if is_square(a_num) and is_square(b_num):
                max_square = max(max_square, max(a_num, b_num))
    # 3. return max_square
    print(max_square)


if __name__ == "__main__":
    main()
