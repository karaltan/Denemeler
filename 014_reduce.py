#!/usr/bin/env python3
from functools import reduce


def main():
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # reduce kullanmak için functools eklenmeli
    print(reduce(buyuk, liste))
    kelimeler = ["Python ", "programlama ", "dili ", "denemeleri "]
    print(reduce(birlestir, kelimeler))
    # her döngüde bir öncekinin sonucuna ekleme yaparak devam eder
    # faktoreyel hesabı
    sayilar = [1, 2, 3, 4, 5]
    print(reduce(carp, sayilar))
    # 1*2 = 2       ilk iki eleman gönderilince donen sonuç diğer döngünün ilk elemanı olacak
    # 2*3 = 6       (R * 3)
    # 6*4 = 24      (R * 4)
    # 24*5 = 120    (R * 5)


def buyuk(x, y):
    if x > y:
        return x
    else:
        return y


def birlestir(a, b):
    return a + b


def carp(a, b):
    return a * b


if __name__ == '__main__':
    main()
