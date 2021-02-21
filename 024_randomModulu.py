#!/usr/bin/env python
import random


def main():
    sayi = random.randint(1, 50)  # bir ve elli arasında bunlar da dahil olmak izere rastgele sayı üretir
    print(sayi)
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    print(random.choice(liste))  # listeden herhangi bir elemanı seçer
    random.shuffle(liste)
    print(liste)  # karşmış liste
    liste.sort()  # siralanmış liste
    print(liste)
    print(random.sample(liste, 6))  # listeden altı adet eleman seçer


if __name__ == '__main__':
    main()
