#!/usr/bin/env python3

def main():
    # python dilinde diğer dillerdeki gibi "tip" değişken tanımlanmaz
    # bunun yerine değişkeni isimlendirip değeri = ile atayabiliriz. örn.
    # sayi = 128
    # cumle = "python programlama dili"
    # global değişken örneği için tüm fonksiyonların ( def ) dışında kalan bir alanda
    # genelde ismi BÜYÜK harfle yazılarak dosya içerisinde bir yere yazılabilir
    # örn. main() çağırdığımız kod bloğunun üzeri bunun için en iyi yer büyük harf kullanmanızı öneriyorum
    sayi = 128
    cumle = "python programlama dili örnekler."
    print(sayi)
    print(cumle)
    # burda global kullanarak aşağıdaki GENEL değişkenini çağırmayı deneyelim.
    # eğer global tanımını kullanmazsanız çalışmayacaktır
    # UnboundLocalError: local variable 'GENEL' referenced before assignment hatası verir
    # ve GENEL değişkeninin fonksiyon içindeki bir değişken olduğunu varsayar.
    global GENEL
    print(GENEL)
    # ardından değiştirmeyi deneyelim.
    GENEL = "Ben değiştim."
    print(GENEL)


GENEL = "Genel kullanım için tanımlanan değişken"

if __name__ == "__main__":
    # bu kod bloğu ise eğer pythonda main fonksiynu varsa misal yukardaki gibi
    # yorumlayıcıya hangi def ile başlayacağını gösteriyor isim illaki main olmak zorunda değil
    # ama genel kabul görmüş maindir alışkanlık edinmenizi öneririm
    # GNU/Linux Yada BSD kullanan arkadaşlar dosya başına mutlaka
    # #!/usr/bin/env python3 eklemelidir daha sonra dosyanın doğrudan çağrılıp çalıştırılması için chmod +x dosya.py
    main()
