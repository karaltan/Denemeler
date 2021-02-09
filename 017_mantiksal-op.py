#!/usr/bin/env python


def main():
    a = True
    b = False
    c = [0, 1, 2]
    print("True and False:\t", a and b)
    # iki veya daha fazla şartında doğru olduğu durumuda kullnılır
    print("True or False:\t", a or b)
    # iki veya daha fazla şarttan en az birinin doğru olması durumunda kullanılır
    print("3 [0, 1 ,2] içinde değil:\t", 3 not in c)
    # değil operatörü, 3 c içinde değilse
    print("3 [0, 1, 2] içinde:\t", 3 in c)
    # bu durumda false verecektir.
    print("1 eşittir 1:\t", 1 == 1)
    # iki değerinde eşit olmasında True
    print("1 eşit değil 2:\t", 1 != 2)
    # iki değerin eşit olmadığı durumda True
    print("3 büyüktür 4:\t", 3 > 4)
    # ilk değer ikinci değerden büyükse True, ek olarak >= büyük veya eşitse
    print("3 küçüktür 4:\t", 3 < 4)
    # ilk değer ikinci değerden küçükse True, ek olarak <= küçük veya eşitse


if __name__ == '__main__':
    main()
