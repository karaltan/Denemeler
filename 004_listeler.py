#!/usr/bin/env python3

def main():
    # listeler ve özellikleri.
    # boş bir liste için aşağıdaki kod ile başlanabilir
    # listede her elemanın bir index numarası olur ve 0 dan başlar
    # ilk eleman her zaman 0 olur, eğer listedeki son elemanı
    # çağırmak istersek liste[-1] ile sonuncu elemanı buluruz.
    liste = []
    # listeye eleman eklemek için .append(eleman) kullanılır örn.
    liste.append("mesaj")
    liste.append("yeni emsaj")
    liste.append("son mesaj")
    print(liste)
    # tüm listeyi ekrana basacaktır
    # tüm listeyi değilde liste elemanlarını sırayla bastırmak için
    for i in liste:
        print(i)
    # listeden eleman silmek için
    liste.remove("mesaj")
    # burda listedeki mesaj isimli elemanı siler
    print(liste)
    # başka bir yöntem ile silmek
    liste.remove(liste[0])
    # listedeki sıfırıncı yani ilk eleman
    print(liste)
    # başka bir yöntem ile silmek
    liste.pop(0)
    # bu durumda listedeki silinen elemanın ne olduğuda yazılıcaktır.
    print(liste)
    # son halinde [] çıktısı ile karşılaşırız boş liste bu şekilde döner


if __name__ == '__main__':
    main()
