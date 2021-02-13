#!/usr/bin/env python
from typing import NewType

Mesafe = NewType('Mesafe', float)
Surat = NewType('Sürat', float)


def main():
    yol = Mesafe(100)
    kms = Surat(95)
    sonuc = hesap(yol, kms)
    print("{:2f} Saat Sürer".format(sonuc))
    print(hesap.__annotations__)


def hesap(yol: 'Mesafe', hiz: 'Surat') -> 'float':
    return float(yol / hiz)


if __name__ == '__main__':
    main()
