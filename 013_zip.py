#!/usr/bin/env python3

def main():
    # zip fonksiyonu birbirine eşit yada farklı uzunluktaki
    # listeleri alıp birleştirir kısa olan liste baz alınır
    isimler = ["Ayşe", "Berker", "Ali"]
    yaslar = [30, 28, 18]
    # zip verisini ham olarak almak yerine listeye çeviriyoruz
    sonuc = list(zip(isimler, yaslar))

    if isinstance(sonuc, list):
        # isistance ile veri türünü tesbit ediyoruz
        # list, dict, tuple, int, str vs.
        print("Veri türü sözlük")
    else:
        print("Veri türü sözlük değil")

    print(sonuc)

    for i, y in sonuc:
        print("{} {} yaşında".format(i, y))


if __name__ == '__main__':
    main()
