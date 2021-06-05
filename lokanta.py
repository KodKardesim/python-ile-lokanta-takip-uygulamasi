from os import system

masalar = {}  # Masa sözlüğünü oluşturduk.

for i in range(1, 11):
    masalar[i] = 0  # Her masaya başlangıç olarak 0 tl atadık.

while True:
    system("cls")
    # While tekrar döndüğünde önceki herşeyi silecek
    # Bu sayede anlık olarak güncellenen bir listeye sahip olacağız.

    print("Lokantamıza hoşgeldiniz.")

    for i in range(1, 11):
        print(f"{i}. masa hesabı {masalar[i]} TL.")

    print("""[1] Hesap Ekle
             [2] Hesap Sil
             [Q] Çıkış Yap """)

    islem = input("İşlem seçiniz : ")
    if islem == "1":
        masano = int(input("Masa no giriniz : "))
        mevcut = masalar[masano]
        eklenecek = int(input("Ekelenek miktar : "))
        masalar[masano] = mevcut + eklenecek
        print(f"{masano} nolu masaya {eklenecek} TL eklendi.")
        input("Devam etmek için 'enter'a basınız.")
    elif islem == "2":
        masano = int(input("Masa no giriniz : "))
        mevcut = masalar[masano]
        silinecek = int(input("Silinecek miktar : "))
        masalar[masano] = mevcut - silinecek
        print(f"{masano} nolu masadan {silinecek} TL silindi.")
        input("Devam etmek için 'enter'a basınız.")

    elif islem == "q" or islem == "Q":
        print("Çıkış yapıldı")
        break
    else:
        print("Hatalı işlem.")
        input("Devam etmek için 'enter'a basınız")
