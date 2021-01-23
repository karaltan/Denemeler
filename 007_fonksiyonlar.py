#!/usr/bin/env python3

def main():
    # bu konuda kendi fonksiyonlarımızı yazmayı ele alacağız
    # örnek olarak dairenin alınını ve çevresini hesaplayacağız
    alan = alan_hesaplama(5)
    print(alan)
    # eğer pi sayısını 3.14 değilde 3 almak istersek
    # alan = alan_hesaplama(5, 3)
    cevre = cevre_hesaplama(5)
    print(cevre)


def cevre_hesaplama(yaricap, pi=3.14):
    # fonksiyonlara değer atamak ve varsayılan değeri kullanmak
    """
    :param yaricap:
    :param pi:
    :return: float
    """
    # çalıştırılacak formul 2 x π x 5
    return float(2 * pi * yaricap)


def alan_hesaplama(yaricap, pi=3.14):
    # fonksiyonlara değer atamak ve varsayılan değeri kullanmak
    """
    :param yaricap:
    :param pi:
    :return: float
    """
    # çalıştırılacak formul π x 5^2
    return float(pi * (pow(5, 2)))


if __name__ == '__main__':
    main()
