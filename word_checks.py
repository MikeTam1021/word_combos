import enchant
import itertools
import sys

if __name__ == "__main__":
    letters = sys.argv[1]
    word_length = int(sys.argv[2])
    d = enchant.Dict("en_US")
    all_combo = itertools.permutations(letters, word_length)
    new_com = [''.join(tup) for tup in list(all_combo)]

    for combo in set(new_com):
        if d.check(combo):
            print combo
