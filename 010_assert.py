#!/usr/bin/env python3

def main():
    # assert kelime anlamı olarak iddia etmek bu kullanımda bunu öğreneceğiz
    sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in sayilar:
        try:
            assert i % 2 == 0
            # % operatörü bölümden kalanı bulmak için kullanılır bkz. mod
            # elbette assert yerine if kullanarakta bu işlem yapılabilir
        except AssertionError:
            print("Sayı çift değil", i)


if __name__ == '__main__':
    main()
