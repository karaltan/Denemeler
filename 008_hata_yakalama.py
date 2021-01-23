#!/usr/bin/env python3

def main():
    # uygulamada olaşabilecek beklenen veye beklenmeyen hatalar için
    # try .. except .. finaly kullanımı
    # olmayan bir dosyayı açmaya kalkıyoruz
    # FileNotFoundError: [Errno 2] No such file or directory: 'deneme.txt' hatasını aldık
    try:
        dosya = open("deneme.txt").readlines()
        print(dosya)
    except Exception as e:
        print("hata sebebi", e)
        # Exception as e kullanımı işimizi kolaylaştıracak hatanın ne olduğunu bulmamız için şart
        # standart kullanımda except yalın haliyle kullanılabilir lakin pek önerilen bişey değildir
    finally:
        print("Program hata versede vermesede bu kod blogu çalışacak.")

    # başka bir örnek
    sayi = 1
    bolum = 0
    try:
        sonuc = sayi / bolum
        print(sonuc)
    except Exception as e:
        print("hata sebebi", "'", e, "'")
        # sıfıra bölünme hatası alacağız
    finally:
        # finally kullanmak zorunda değili ama olası durumlarda kod hata versede devam ettirlmesi gereken
        # işlemler olabilir bu durumda finally her defasında hata olmasa dahi çalışacak
        print("program durdu")


if __name__ == '__main__':
    main()
