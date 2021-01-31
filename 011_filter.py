#!/usr/bin/env python3

def main():
    # listemizde var olan sayılar için lambda ile tek satırda fonksiyon yazdık
    # geri dönen degeri "list" ile listeye çevirdik ve çift sayıları bulduk
    # filter adı üzerinde filtre eden bir yapı bu yapıya uygun fonksiyonu ve
    # listeyi veya sözlüğü verip işlem yaptırıyoruz.
    # filter(fonksiyon, liste) fonksiyonu illaki lambda ile yazmanıza gerek yok
    liste = [10, 12, 14, 4, 5, 6, 7, 9, 2, 3, 16, 18, 20]
    sonuc = list(filter(lambda x: x % 2 == 0, liste))
    sonuc.sort()
    print("çift sayılar", sonuc)
    # .sort üzerinde çalıştığınız listeyi sıralar


if __name__ == '__main__':
    main()
