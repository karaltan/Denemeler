#!/usr/bin/env python3
from random import randint
# import random şekilinde tüm kütüphaneyi çağırmaktansa işimize yarayan kısmı almak daha mantıklı
# random kütüphanesinden randint fonksiyonunu içeri aktardır
# bu fonksiyon bize belirlenen iki farklı sayı arasında sayı üretecek


def main():
    # pythonda listeler işimizi kolaylaştıran bir veritipidir
    # içerisine herhangi bir veriyi (bu sayı veya metin şeklinde olabilir) ekleyebiliriz
    # detayları ilerki derslerde anlatılacak.
    liste = []
    while len(liste) < 6:
        # liste boyutu altı elemandan çükük olduğu sürece çalışacak
        # len ile liste içindeki öğelerin sayısını alıyoruz
        # altıdan küçük olduğu sürece döngü devam edecek
        sayi = randint(1, 49)
        if sayi not in liste:
            # eger sayı liste içinde yoksa
            liste.append(sayi)
    liste.sort()
    # listemizi sıralamak için
    print(liste)
    # görüldüğü üzere listemizde altı farklı numara oluştu hepsi birbirinden farklı ve sıralanmış.

    liste.clear()
    # listemizi temizledik ve yukardaki kodu farklı bir şekilde yeniden yazıyoruz

    while 1:
        # burda sonsuz döngü oluşturduk 1 değeri her durumda True olacağı için şart sağlanmış olacak
        sayi = randint(1, 49)
        if sayi not in liste:
            liste.append(sayi)
        if len(liste) == 6:
            break
            # dizi boyutu 6 adet olduysa break ile durduruyoruz.
            # burda atlamamız gereken konu listenin ilk elemanı sıfırdır
            # 0 dan başladık ve 0 ve 5 dahil olmak üzere toplam altı adet elemanımız oldu
    liste.sort()
    print(liste)


if __name__ == "__main__":
    main()
