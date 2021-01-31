#!/usr/bin/env python3

def main():
    # map fonksiyonu kullanımı
    # map fonksiyonu paremetre olarak aldığı listedeki her elemanı
    # belirtilen fonksiyona gönderir
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sonuc = list(map(karesi, liste))
    print(sonuc)
    # iki farklı listeyi map ile kullanmak
    tekler = [1, 3, 5, 7]
    ciftler = [2, 4, 6, 8]
    carpim = list(map(lambda x, y: x * y, tekler, ciftler))
    print(carpim)


def karesi(x):
    return pow(x, 2)
    # pow python içinde "x^2" olarak kullanılan yerleşik bir fonksiyon
    # yani verilen sayının karesini alır bunun yerine "x * x" de kullanılabilir


if __name__ == '__main__':
    main()
