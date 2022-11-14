# STMCTF'22 Ön Eleme

## Soru İsmi:
`Captain's Logs`


## Kategori:
- `Web`


## Soru:

```
TR:
Kaptan yanlislikla bayragi seyir defteri icinde kaybetmis. Onu bulmasina yardimci olabilir misin?

EN:
Captain has lost his flag in his logs. Can you help him find it?
```

---

## Çözüm:

Soruya baglanildiginda asagidaki ekran ile karsilasilir:

![alt img1](solution/s1.png "main page")

Ekranda yer alan alanlar tek tek Server Side Template Injection icin denenir ve **Isim** alaninin bu zafiyeti icerdigi gorulur:

![alt img2](solution/s2.png "testing for injection")
![alt img3](solution/s3.png "injection successful")

Sunucu uzerinde kod calistirilip calistirilamayacagi kontrol edilir. Bunun icin flask uygulamasinin **config.items()** listesinden yararlanilir. 

Oncelikle mevcut olan **config.items()** listesi kontrol edilir:

![alt img4](solution/s4.png "checking for config.item()")
![alt img5](solution/s5.png "output")

Diger kutuphanelerde mevcut olan fonksiyonlarin cagirilabilmesi icin once yuklenmeleri gerekir. Dosya sistemi ile iletisime gecmek icin **Subprocess.Open** fonksiyonu kullanilabilir. Bu fonksiyonu cagirabilmek icin once **os** kutuphanesinin yuklenmesi gerekir.

![alt img6](solution/s6.png "loading os library")
![alt img7](solution/s7.png "output")

Yeni yuklenen kutuphaneleri listenir ve Popen fonksiyonunun cagirilmasi icin liste icindeki indeksi deneme yoluyla bulunur.

![alt img8](solution/s8.png "listing and finding popen function")
![alt img9](solution/s9.png "listing and finding popen function")
![alt img10](solution/s10.png "listing and finding popen function")
![alt img11](solution/s11.png "listing and finding popen function")

Fonksiyonun indeksinin **395** oldugu bulunur. Asagidaki yontem ile dosyalar listenir.

![alt img12](solution/s12.png "listing and finding popen function")
![alt img13](solution/s13.png "listing and finding popen function")

Listenen dosyalar arasinda flag.txt gorulur. **cat flag.txt** komutu ile dosya icerigi listenelir.

![alt img14](solution/s14.png "listing and finding popen function")
![alt img15](solution/s15.png "listing and finding popen function")
