Kullanici1 = "Doga"
Parola1 = "Doga1"

while(True):
    Kullanici2 = input("Kullanici adini giriniz: ")
    Parola2 = input("Parolayı giriniz: ")
    if (Kullanici1 == Kullanici2 and Parola1 == Parola2):
        print("Hoşgeldiniz.",Kullanici2)
        break
    elif (Kullanici1 != Kullanici2 and Parola1 == Parola2):
        print("Kullanıcı adını yanlış girdiniz.")
    elif (Kullanici1 != Kullanici2 and Parola1 != Parola2):
        print("Kullanıcı adını ve Parolayı yanlış girdiniz.")
    elif (Kullanici1 == Kullanici2 and Parola1 != Parola2):
        print("Yanlış parola girdiniz.")
        cevap = input("Parolanızı değiştirmek istermisiniz [e][h]: ")
        if (cevap == 'e' or cevap == 'E'):
            yeniparola = input("Yeni parola: ")
            print("Lütfen bekleyin..")
            Parola1 = yeniparola
            print("Başarıyla değiştirdiniz")
        else:
            print("Tekrar deneyin.")
