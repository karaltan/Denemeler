#!/usr/bin/env python
import locale
import time


def main():
    locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')
    # linux sistemlerde yerel bilgisi için konsoldan "locale -a" ile hangi diller ayarlı görünür
    simdi = time.strftime("%d %B %A %Y %X")
    # %d Gün, %B Ay, %A Gün adı, %Y Yıl, %X saat
    print(simdi)


if __name__ == '__main__':
    main()
