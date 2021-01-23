#!/usr/bin/env python3

def main():
    # temel olarak sözlükler her biri ikişerli olmak üzere anahtar ve değer içeren öğeler alır
    # her anahtar benzersiz olmak zorundadır, yani aynı anahtardan birden fazla olamaz
    # sözlükler bir defaya mahsus program yazılırken oluşturulur sonradan üzerinde
    # değişiklik yapılamaz, eklema çıkarma vs.
    # çalışma mantığı çağırılan anahtarın karşısındaki veriyi geri döndürmesidir örn.
    # "1": "Bir" eğer sözlüğe "1" değerini sorarsak bize "Bir" çıktısını verecektir
    sozluk = {"1": "Bir", "2": "İki"}
    print(sozluk["1"], sozluk["2"])


if __name__ == '__main__':
    main()
