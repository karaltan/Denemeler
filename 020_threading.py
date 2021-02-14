#!/usr/bin/env python

from time import sleep as bekle
import threading


def gorev():
    # ana gövdeden hariç çalışacak kod blogu burda tanımlandı
    for i in range(8):
        bekle(1)
    print("Görev sonlandı...")


def sayac():
    # bu biraz işin rengi olsun diye bir çeşit progress bar
    liste = [".", "..", "...", "....", "....."]
    for i in liste:
        print(i, " ", end="\r")
        bekle(0.1)


def main():
    # kanal1 isminde threading yapılacak blogu tanımladık
    # tanımlama yaparken target=gorev kısmına dikkat edelim () yok
    # ilerki kodlarda kanala argüman eklemeyide göreceksiniz.
    kanal1 = threading.Thread(target=gorev)
    kanal1.start()
    while 1:
        # is_alive() halihazırda çalışan kanalımız işi bitmediyse True dönecek
        if kanal1.is_alive():
            # kanal1 çalışırken bizde farklı işlemleri çalıştırabiliriz
            sayac()
        else:
            # false durumunda göngüden çıkılacak.
            break
    bekle(1)
    print("Main durdu")


if __name__ == '__main__':
    main()
