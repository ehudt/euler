from collections import defaultdict
from itertools import combinations, permutations
from typing import Generator, Tuple
from gmpy2 import is_square  # type: ignore


def gen_replacements(a: str, b: str) -> Generator[Tuple[int, int]]:
    for perm in permutations("1234567890", len(a)):
        map = {x: perm[i] for i, x in enumerate(a)}
        a_repl = "".join([map[x] for x in a])
        b_repl = "".join([map[x] for x in b])
        if a_repl[0] == "0" or b_repl[0] == "0":
            continue
        yield int(a_repl), int(b_repl)


def main():
    # 0. load 0098_words.txt
    words = [word.strip('"') for word in open("0098_words.txt").read().split(",")]
    # 1. find all anagram classes
    anagram_classes = defaultdict(list)
    for word in words:
        anagram_classes["".join(sorted(word))].append(word)
    #   1.1 generate all anagram pairs
    pairs = []
    for _, values in anagram_classes.items():
        if len(values) <= 1:
            continue
        for a, b in combinations(values, 2):
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
