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
mail.sendmail(login,mail1,content)



