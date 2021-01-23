#!/usr/bin/env python3

def main():
    # input konsol ekranından veri almak için
    # alınan değer string veridir int() ile sayısal bir değere dönüştürüyoruz
    yas = int(input("Yaşınız: "))
    if yas < 18:
        print("18 yaşından küçükler giremez.")
    elif yas >= 18 and yas <=35:
        print("Yaş aralığı uygun")
    else:
        print("Geçerli değil")
    # bu karşılaştırmada yaş aralığı 18den küçük ise
    # veya 18 ila 35 dail aralıktaysa uygun kodlar yürütülecek
    # and operator her iki şartıda doğru olacak şekilde kontrol eder
    # or operatörü her şarttan en az birisinin doğru olmasında geçerlidir
    # not operatörü tersi durumu geçerli kabul eder
    # bu aralık dışında kalan else ile devam edecek
    # not operatörü için örn.
    kontrol = [1, 2, 3, 4, 5, 6, 7, 9, 0]
    if 8 not in kontrol:
        print("8 listede değil")
    else:
        print("8 listede.")
    # bu örnekte 8 herhangi bir değişken olabilir.


if __name__ == '__main__':
    main()
