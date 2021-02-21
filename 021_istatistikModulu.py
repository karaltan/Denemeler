#!/usr/bin/env python

import statistics


def main():
    veriler = [10, 15, 12, 17, 22, 35, 28, 19, 13, 21]
    sapma = statistics.stdev(veriler)  # fx-82MS sx ( s-var 3 ) standart sapma
    sapma_karesi = statistics.variance(veriler)  # varyans x² standart sapmanın karesi
    ortalama = statistics.mean(veriler)  # mean fx-82MS sx ( s-var 2 ) ortalama
    print("Standart Sapma: {}\nKaresi: {} \nOrtalama: {}".format(sapma, sapma_karesi, ortalama))


if __name__ == '__main__':
    main()
