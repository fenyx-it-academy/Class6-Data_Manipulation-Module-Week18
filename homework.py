import numpy as np
import pandas as pd
# 1. Numpy’da Vektor ve Matrisin farkini tek cumle ile ifade ediniz.
# Vektör, tek boyutlu bir dizidir (satır ve sütun vektörleri arasında fark yoktur), matris ise iki boyutlu bir diziyi ifade eder"

# 2. 10 elemanli bir listeden NumPy Array’i olusturunuz.
# a = np.arange(10)
# print(a)

# 3. Icerisinde ‘0’ lar olan, ve veri tipi integer olan 10X10’luk bir matris olusturunuz.
# b = np.zeros((10,10), dtype=int)
# print(b)

# 4. Icerisinde ‘1’ ler olan, veri tipi float olan 10X10’luk bir matris olusturunuz.
# c = np.ones((10,10),dtype=float)
# print(c)

# 5. Icerisinde ‘9’ lar olan, veri tipi integer olan 10X10’luk bir matris olusturunuz.
# d = np.full((10,10),9 , dtype=int)
# print(d)

# 6. 5 ile 25 arasinda, 3’er 3’er atlayan tek boyutlu bir Array olusturunuz.
# e = np.arange(5,25,3)
# print(e)

# 7. -1 ile 1 arasinda 30 adet Array olusturunuz.
# f = np.linspace(-1,1,30)
# print(f)

# 8. 0 ile 30 arasinda 5x6’lik bir matris olusturun.
# g = np.random.randint(0,30,(5,6))
# print(g)

# 9. Kosegenleri 1 olan 10x10’luk bir matris olusturunuz.
# h = np.eye(10)
# print(h)

# 10. 0 ile 10 arasinda 5x10’lik bir matris olusturun. (integer) ve bu matrisin;
# i = np.random.randint(0,10, (10,10))
# print("Boyut sayisi =  ",i.ndim) 
# print("satir, sutun bilgisi =  ",i.shape)
# print("Toplam eleman sayisi =  ",i.size)
# print("Veri tipi =  ",i.dtype)

# 11. 0 ile 10 arasindaki degerlerden olusan 3 adet 4x7’lik bir matris olusturunuz. (3 boyutlu bir matris olusturulacak)
# k = np.random.randint(10, size=(3,4,7))
# print(k)

# 12. Bir vektor olusturunuz ve daha sonrasinda ayni vektoru bir matrise ceviriniz. (boyut sayisini degistirin.)
# l= np.arange(6)
# ll = l.reshape(3,2)
# print(ll)

# 13. 4 tane ayri tek boyutlu array’i birlestirerek bir array olusturunuz.
# x=np.array([1,2,3,4])
# y=np.array([1,2,3,4])
# z=np.array([1,2,3,4])
# t=np.array([1,2,3,4])
# xx=np.concatenate([x,y,z,t])
# print(xx)

# 14. 2 boyutlu bir vektor ve bir matris olusturun(ayri ayri), bu iki arrayi numpy metodlarini kullanarak sutun bazli birlestiriniz,
# m = np.array([[9, 8, 7], [6, 5, 4]])
# mm=np.random.randint(0,10, (2,2))
# mmm=np.hstack([m,mm])
# print(mmm)

# 15. Numpy’da “axis=1” ve “axis=0” arasinda ne fark vardir. Teorik olarak yaziniz?
# Eksen 0, birinci boyut (satır) ve eksen 1, ikinci boyut (sütun).

# 16. Farkli boyutlardaki arraylari satir ve sutun bazli ayri ayri birlestiriniz.
# o= np.array([1, 2, 3])
# oo= np.array([[9, 8, 7], 
#                 [6, 5, 4]])
# ooo=np.vstack([o,oo]) 
# print(ooo)
# print(oo)
# print(o)

# 17. 10 elemanli bi liste olusturunuz ve bu listeyi Numpy metodlariyla bolerek(split) 4 ayri array olusturunuz.
# s=np.array=([1,2,3,4,5,6,7,8,9,10]) 
# s = np.arange(10)
# ss,sss,ssss,sssss =np.split(s, [3,6,9])
# print(ss)
# print(sss)
# print(ssss)
# print(sssss)

# 18. Random bir array olusturunuz ve bu arrayi buyukten kucuge dogru siralayiniz. Sonra hangi elemanin hangi indexte oldugunu gosteren bir metod uygulayiniz.
# tt=np.random.randint(30,size=10)
# ttt = np.sort(tt)
# print(ttt)

# 19. 20 elemanli random bir vektor olusturunuz. Bu vektorun 3. 5. ve 7. elemanlarina ulasin.
# v=np.random.randint(50, size=20)
# print(v)
# print(v[3],v[5],v[7])

# 20. 10 elemanli random bir vektor olusturunuz ve bu arrayin 4. elemanini farkli bir sayiyla degistiriniz.
# v=np.random.randint(20, size=10)
# v[4]=20000
# print(v)

# 21. “Diagonal Matrix” ve “Trace Matrix” kavramlari hakkinda bir arastirma yapip bunlarin ne oldugunu belirten kucuk bir aciklama yaziniz.
#Diagonal Matrix=The unit matrix is every nxn square matrix made up of all zeros except for the elements of the main diagonal that are all ones.
#Trace Matrix = It is the sum of the elements on the main diagonal, from the upper left to the lower right, of the matrix.

# 22. 5x5’lik Diagonal bir matris olusturunuz ve Diagonaline denk gelen indexlere ulasiniz.(ayri ayri)
# x=np.eye(5)
# print(x[0,0],x[1,1],x[2,2],x[3,3],x[4,4])

# 23. 10 ile 20 arasinda bir vektor olusturunuz. Ve 3. indexten son indexe kadar olan degerleri yazdiriniz.
# a = np.arange(10,20,1)
# print(a)
# print(a[3:])

# 24. 24. 10X10 luk bir matris olusturunuz ve 3.satirin 5.sutununa ulasiniz. Ayrica;
# * a. 5.sutunun tum satirlarina ulasiniz.
# * b. Tum sutunlarin 2.satirlarina ulasiniz.
# * c. tum sutunlarin 2 ile 7 arasindaki satirlarina ulasiniz.
# * d. satir indexi 2’den 5’e ve sutun indexi 3 den 7’ye kadar olan degerlere ulasiniz.
# * e. satir indexi 5’den en sona ve sutun indexi en bastan 4’e kadar olan degerlere ulasiniz.
# * f. sutun indexi sadece 3, 6,9 olan kolonlarin(sutunlarin), tum satirlarina ulasiniz.
# * g. 5. indexli satir ve 5.indexli sutuna denk gelen degeri, dogum yilinizla degistiriniz.
# kk =np.random.randint(50, size = (10,10))
# print(kk)
# print(kk[2,4])
# # a
# print(kk[:,5])
# # b
# print(kk[2,:])
# # c
# print(kk[2:7,:])
# # d
# print(kk[2:5,3:7])
# # e
# print(kk[5:,:4])
# # f
# print(kk[:,(3,6,9)])
# e
# kk[5,5]=1992
# print(kk)

# 25. 0’dan 50’ye kadar 5’er 5’er atlayarak giden bir array olusturunuz (tek boyutlu) ve numpy metodlariyla asagidaki islemleri uygulayin;
#a. 20 den buyuk olan kac deger var.
#b. 30’dan kucuk kac deger var.
#c. icerisinde 3 gecen kac deger var
#d. olusturulan arrayin tum elemanlarini 5 ile carpin.
#e. olusturulan arrayin tum elemanlarinin 2 ile bolumunden kalanlari yazdiriniz.
# aa = np.arange(0,50,5)
# print(aa)
# a.
# aaa=np.sum(aa > 20)   
# print(aaa)
# b
# bbb=np.sum(aa < 30)
# print(bbb)
# d
# ddd = aa*5
# print(ddd)
# f
# fff=aa%2
# print(fff)

# 26. 0 ile 1 arasinda 50 elamanli bir array olusturunuz ve ortalamasini aliniz. Ayrica;
# a. standart sapmasini aliniz.
# b. varyansini aliniz.
# c. median’ini aliniz.
# d. en kucuk degeri bulunuz.
# e. en buyuk degeri bulunuz.
# cc = np.linspace(0,1,50)
# print(c)
# a
# a = np.std(cc)
# print(a)
# b
# b = np.var(cc)
# print(b)
# c
# c = np.median(cc)
# print(c)
# d
# d = np.min(cc)
# print(d)
# e
# e = np.max(cc)
# print(e)

# 27. Pandas seriler ve numpy arrayler arasindaki farklar nelerdir yaziniz.
#Panda can have different data types and it can be changed in the index

# 28. Indexi buyuk harflerden olusan, icinde farkli veri tipleri bulunan 5 elemanli bir seri olusturunuz.
# seri=pd.Series([1,1.5,False,True,None],index=('A','B','C','D','E'))
# print(seri)

#29. Key’ler ulke adlari, value’lar baskentleri olacak sekilde 5 elemanli bir sozluk olusturup onu seriye ceviriniz. (ornek: fransa:paris)
# dict={'Netherlands':'Amsterdam','Turkey':'Ankara','ABD':'Washington','England':'London','Greece':'Athens'}
# seri1=pd.Series(dict)
# print(seri1)

# 30. 10 elemanli random bir vektor olusturun.
# Vektoru seriye cevirip indexleri str olarak belirleyin.
#   (ornek: a,b,c,d,e,f,g.. seklinde)
# Index ismine gore serinin 3. elemanina ulasin.
#   (ornek: c indexine karsilik gelen deger)
# Serinin index sirasina gore 1. Elamanina ulasin.
# Index ismine gore serinin  2. Ve 7. Elemanlarina ayni anda ulasin.
#   (Ornek: b ve g indexine karsilik gelen degerler)
# Index ismi ile serinin 2. Ve 7. Elemanlari arasindaki degerleri yazdirin.
#   (Ornek: b,c,d,e,f,g indexlerine karsilik gelen degerler)
# Index sirasiyla serinin 4. indexinden son indexine kadar olan degerleri yazdirin.
# ax=np.random.randint(10,size=10)
# seri2=pd.Series(ax,index=('A','B','C','D','E','F','G','H','I','J'))
# print(ax)
# print(seri2)
# print(seri2['C'])
# print(seri2[0])
# print(seri2[['B','G']])
# print(seri2['B':'G'])
# print(seri2[3:])
