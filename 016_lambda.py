#!/usr/bin/env python

karesi = (lambda x: x * x)
toplam = (lambda y: y + y)
# lambda ifadesini () içine almak önemli bkz: pep


def main():
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in liste:
        print("karesi: {}\t Toplamı {}".format(karesi(i), toplam(i)))
        # \t ifadesi tab ile satırları sutunları hisalamak için
        # \n yeni satır \b satır başı \a alarm sesi


if __name__ == '__main__':
    main()
