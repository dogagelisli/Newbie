import smtplib
print("####################")
print("        d4nt        ")
print("####################")

content = input("Mesajınızı giriniz: ")
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
login = input("Gönderici Mail adresinizi giriniz: ")
pw = input("Gönderici Mail adresinizin parolasını giriniz: ")
mail.login(login,pw)
mail1=input("Göndermek istediğiniz mail adresini yazınız: ")
sayi = int(input("Kaçtane mail göndermek istiyorsunuz ?: "))
for a in range(sayi):
    mail.sendmail(login,mail1,content)
    print("+\n", end="")
print("BAŞARIYLA GÖNDERDİNİZ")
