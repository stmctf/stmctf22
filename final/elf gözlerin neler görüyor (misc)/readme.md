# STMCTF'22 Final

## Soru İsmi:
`Elf gözlerin neler görüyor`


## Kategori:
- `Misc`


## Soru:

```
TR:
Masanıza size özel bir zarf bıraktık. Zarf içerisinde sizin için özel hazırlanan bir A3 kağıdı var.
Bu kağıdın bir başka kopyası yok. Flag bu kağıttaki bir QR kodunda. Eğer doğru QR kodunu bulursan flag sende. Flag'i encode etmedik, binary tarzı saklamadık; açık olarak STMCTF formatında QR'da.

EN:
We left a special envelope for you on your table. There is an A3 paper specially prepared for you in the envelope.
There is no other copy of this paper. Flag is in a QR code on this paper. If you find the correct QR code, you have the flag. We did not encode the flag, we did not store the binary style; clearly in the QR in STMCTF format.
```

---

## Çözüm:

A3 kağıdında bulunan butun QR kodları cep telefonu ile büyüterek taranabiliyor. Ancak 2000'den fazla QR kodun bu sekilde taranması pratik degil. 

A3 kağıdı fotoğrafını bilgisayara aktarıp, bilgisayar ekrandan QR kodlarını tek tek cep telefonu ile taramak da mümkün olabiliyor. Belli bir düzende bu işlemi yapabilirsiniz ama yine çok zaman harcamanız gerekiyor.

İşinizi şansa bırakmak istemiyorsanız bizim bir çözümümüz var. 

Cep telefonu ile A3 kağıdını 4 parça olarak fotoğraflayıp (kullanılan cep telefonun eski olması durumunda bindirmeli şekilde A3 kağıdı 16 veya 20 parçaya bölünüp fotoğraflanabilir), QR kodu büyüklüğünden biraz daha büyük bir parça crop alarak resim üzerindeki olası tüm QR kodlarını Python kütüphanelerini kullanarak tarayabiliriz.


Çözüm için 2011 ve 2015 yıllarında piyasaya çıkmış iki farklı cep telefonunu denedik. Her ikisinde de aşağıdaki kodu kullanarak flag elde edilebildik. 

* [iphone6s](https://tr.wikipedia.org/wiki/İPhone_6S)
* [Samsung Galaxy Gio (GT-S5660)](https://tr.wikipedia.org/wiki/Samsung_Galaxy_Gio)

Iphone 6s kullandığımızda A3 kağıdını 4 parça olarak fotoğrafını çekmemiz yeterli olurken, Samsung Galaxy Gio ile en az 16 parça olarak fotoğraflamamız gerekti. Parçaların kesiştiği yerleri ayrıca tekrar fotoğraflayarak ölü bölge kalmamasını sağladık. Fotoğraf çekme işlemlerini ofis ortamında normal gerçekleştirdik. Daha eski kamera özellikli telefonlarda parça sayısı arttırılabilir. 

Çözüm scriptindeki *img_size* değişkeni çektiğiniz fotoğraftaki QR kodlarının büyüklüğüne göre değiştirmeniz gerekmektedir. Bunu kontrol etmek için de DEBUG 3 bölümünü açıp *dir_out* klasorundeki croplanan resimlerin içeriğine bakmanız gerekmektedir. Eğer QR kodarı resim içine sığmıyorsa img_size'ı büyütmeniz, QR kodları küçük kalıyorsa da küçültmeniz gerekmektedir. 

iphone6s Fotoğraf
![iphone6s](assets/iphone6s_1.png)

Samsung Galaxy Gio (GT-S5660) Fotoğraf 1
![Samsung Galaxy Gio (GT-S5660) 1](assets/GT-S5660_1.png)

Samsung Galaxy Gio (GT-S5660) Fotoğraf 2
![Samsung Galaxy Gio (GT-S5660) 2](assets/GT-S5660_2.png)

Samsung Galaxy Gio (GT-S5660) Fotoğraf 3
![Samsung Galaxy Gio (GT-S5660) 3](assets/GT-S5660_3.png)

Samsung Galaxy Gio (GT-S5660) Fotoğraf 4
![Samsung Galaxy Gio (GT-S5660) 4](assets/GT-S5660_4.png)


### Çözüm Scripti
```python
from PIL import Image
from pyzbar.pyzbar import decode

import os

## Fotografi cekilen QR kodlarinin dizin adı
dir_in = "dir_in"

##  Fotograf Dosya Tipi
filetype = ".png"

## Imajin boyutuna gore degistirilmesi gerekiyor
## QR kodundan biraz buyuk olmasi yeterli
img_size = 110 # iphone6s ile cekilen foto (1/4)
img_size = 140 # samsung_GT_S5660 ile cekilen foto (1/16)

## QR kodlarinin uzerinde yururken her adimda ne kadar ilerlenecegi
## Kucuk olursa zaman uzuyor, buyuk olursa flag kacirilabiliyor
image_walk = 5

## dir_in klasorundeki tum dosyalari list olarak alir
resimler = next(os.walk(dir_in), (None, None, []))[2]
resimler.sort()

## Tum resimlerde deniyoruz
for resim in resimler:

    ## Baska dosyalar varsa onlari islemesin
    if filetype not in resim:
        continue

    filenamepath = os.path.join(dir_in, resim)
    print ("Dosya ismi: ", filenamepath)

    img = Image.open(filenamepath)
    w, h = img.size

    ## DEBUG 1
    ## Acilan imajin boyutu
    # print ("imaj w, h: ", w, h)

    # Dikeyde yurume
    flagfound = False
    for walk_h in range(0, h, image_walk):

        ## DEBUG 2
        # print ("walk_h: ",walk_h)

        ## Yatayda yurume
        for walk_w in range(0, w, image_walk):

            ## Belirlenen olculerde resmi buyuk resimden alma
            cropped = img.crop((walk_w, walk_h, walk_w+img_size, walk_h+img_size))

            ## DEBUG 3
            ## Islenen resimlerin ne oldugunu gormek icin
            ## img_size degiskeninde verilen deger ile croplanan imaj, qr kodlarindan kucuk olmamalidir.
            ## bu bilgiyi de asagidaki kodu calistirarak yapabiliriz.
            # save_path = os.path.join("dir_out","croped " + str(walk_w) + "-" +  str(walk_h) + ".png")
            # cropped.save(save_path,'PNG')

            ## DEBUG 4
            # data = decode(Image.open(save_path))

            data = decode(cropped)
            if len(data) > 0:

                ## DEBUG 5
                # print(str(data[0]))

                if "STMCTF" in str(data[0]):
                    print(str(data[0]))
                    flagfound = True
                    break

        if flagfound:
            break

            ## DEBUG 6
            # os.remove(save_path)
```