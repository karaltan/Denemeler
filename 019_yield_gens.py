#!/usr/bin/env python


def carpim():
    # generator her çağrıldığında
    # yield bir sonraki nesneyi dönderecek
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in liste:
        yield i * i


def main():
    uretec = carpim()
    print(type(uretec))
    print(type(carpim))
    # generator icin uretec isminde bir tanım yapiyoruz
    # uretec generaorde tanımli olan liste boyutu kadar çalısacak
    # iterator durunca for döngüsüde bitecek.
    for i in uretec:
        print(i)


if __name__ == '__main__':
    main()
