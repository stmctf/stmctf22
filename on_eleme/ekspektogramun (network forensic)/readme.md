# STMCTF'22 Ön Eleme

## Soru İsmi:
`Expecto Gramun`


## Kategori:
- `network Forensic`


## Soru:

```
TR:
Bilinmeyen bir numaradan gelen acil arama. 

EN:
Emergency call from an unknown number.
```

---

## Çözüm:
```
Flag template e baktığımda kaçak bir kişinin adı ve bir yerin adını bulmamız isteniyor. arama.zip adlı dosya içerisinde aramaKaydi.txt adlı bir metin dosyası olduğunu görüyoruz ancak bu dosyayı okuyabilmek için parolaya ihtiyacımız var. acil_arama.mp4 adlı videoya girdiğimde hepimizin aşina olduğu eski bir telefon, aşina olmadığımız bir zil sesi ile çalıyor. Normalde telefonun markasının yazdığı kısımda da bize ipucu verilmiş. Burada sorunun adı bize yol gösterici oluyor. Sorunun adını dikkatli okursak “ekSPEKTOGRAMun” ifadesini farkedebiliriz ki bu da bize verilmiş olan bir başka ipucu: Spektograma bak. 
Açık kaynak ses düzenleme uygulaması olan audacity ile videoyu açtığımda ses dalgalarını görebiliyorum. 
```
![dalga](https://user-images.githubusercontent.com/74919981/191695272-33e3d48f-4622-4557-824e-a73ddf56695b.png)
```
Kırmızı ile işaretli açılır pencereden spektogramı seçip görüntülediğimde bir takım numaraların var olduğunu görüyorum.
```
![specto](https://user-images.githubusercontent.com/74919981/191695322-9128806a-e31c-4bb9-a943-842ce5cf49b3.png)
```
Bu aşamada videoda telefon üzerinde bize verilen ipucu aklıma geliyor ve telefon tuş takımı üzerinden deşifre etmeye çalışıyorum.
```

```
7777=>s    7=>p    33=>e    2=>a   55=>k   0=>boşluk 
333=>f   777=>r   444=>i   33=>e   66=>n    3=>d   0=>boşluk 
2=>a   66=>n   3=>d   0=>boşluk
33=>e   66=>n   8=>t   33=>e   777=>r


Elde ettiğimiz metin===> speak friend and enter

Ve flagimizi bulduk:

STMCTF{speak friend and enter}
```


