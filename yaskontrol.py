isim=input("İsminizi Giriniz: ")
yas=int(input("Yaşınızı Giriniz: "))

if(yas<18): 
    print("Sayın %s, 18 yaşından küçük olduğunuz için işleme devam edemezsiniz."%isim)
else:   
    print("Hoşgeldiniz %s!"%isim)