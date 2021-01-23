#!/usr/bin/env python3

def main():
    # for dongüsü bir listenin veya bir verinin ilk elemanından başlar
    # son elemanına kadar listeyi tek tek işler örn
    for x in range(1, 9):
        print(x)
    # burda x için range ile oluşan listede 9 olana kadar 9 hariç
    # x deeğerini yazdırdık liste için aşağıdaki örneğe bakalım
    liste = ["GNU", "Linux", "Pyhton"]
    for i in liste:
        print(i)
    # range deyiminde 9 değerini almamıştı ama listede durum farklı
    # ilk elemandna son elemana kadar tüm değerler alındı


if __name__ == '__main__':
    main()
