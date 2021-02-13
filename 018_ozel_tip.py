#!/usr/bin/env python
from typing import NewType
import datetime

Mesafe = NewType('Mesafe', float)
Surat = NewType('Sürat', float)


def main():
    yol = Mesafe(100)
    kms = Surat(90)
    sonuc = hesap(yol, kms)
    saat = str(datetime.timedelta(hours=sonuc))
    print("{} Saat Sürer".format(saat))
    print(hesap.__annotations__)


def hesap(yol: 'Mesafe', hiz: 'Surat') -> 'float':
    return float(yol / hiz)


if __name__ == '__main__':
    main()
