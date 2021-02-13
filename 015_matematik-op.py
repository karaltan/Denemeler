#!/usr/bin/env python3

def main():
    a = 5
    b = 3
    print("a ile b toplamı", a + b)

    c = 15
    d = 5
    print("c ile d çarpımı", c * d)

    e = 18
    f = 4
    print("e ile f çıkarımı", e - f)

    x = 15
    y = 4
    print("x bölü y", x / y)
    print("X bölü y kaça bölünür", x // y)
    print("X bölü y kalanı", x % y)

    print(ord("a"))
    # ord("a") a harfinin sayısal karşılığını verir
    print(oct(97))
    # oct(97) sayısınızn sekizlik karşılığını verir
    print(bin(67))
    # bin(67) 67 satısının ikilik sistemde karşılığını verir
    print(hex(67))
    # hex(67) 67 satısının onaltılık sistemde karşılığını verir
    print(abs(-128))
    # abs(-128) mutlak değeri dönderir
    print(round(12.2))
    print(round(12.9))
    print(round(23/6, 5))  # sondan 5 hane olacak şekilde yuvarlar
    # tam sayıya en yakın yerden yuvarlama yapar
    liste = [False, 1, 2, 3, 4]
    print(all(liste))
    # liste elemanlarının hepsi True ise True dönecek, false varsa False dönecek
    liste2 = [True, False]
    print(any(liste2))
    # liste elemanlarından en az birisi True ise True dönecek.
    print(ascii("ı ğ d ı r"))
    # ascii karakteri unikod formatında döküm verecek
    print(repr(False))
    # paremetre olarak verilen herşeyi yazılı (string) olarak geri dönderir
    print(bool(2))
    # verilen parametrenin bool olarak karşılığını geri verir True yada False
    print(chr(97))
    # verilen sayının harf karşılığını verir
    print(divmod(8, 2))
    # bir sayının başka bir sayıya bölümünden "bölümü" ve "kalanı" verir
    print(max(liste))
    # bir listedeki en büyük sayıyı verir 4
    print(min(liste))
    # bir listedeki en küçük sayıyı verir 1 yada False
    topla = [1, 2, 3, 4, 5]
    print(sum(topla))
    # bir listedeki tüm sayıları toplar


if __name__ == '__main__':
    main()
