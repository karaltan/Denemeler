#!/usr/bin/env python
import difflib


def main():
    kelimeler = ["ara", "arab", "araba", "abara", "arabaşı", "abera", "arabe", "arabo"]
    aranan = "araba"
    for i in kelimeler:
        oran = difflib.SequenceMatcher(None, aranan, i).ratio() * 100
        print("{}:\t{}\t ile \t % {} benzer".format(aranan, i, oran))


if __name__ == '__main__':
    main()
