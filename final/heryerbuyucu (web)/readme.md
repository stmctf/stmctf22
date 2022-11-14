# STMCTF'22 Final

## Soru İsmi:

`heryerbuyucu`

### Kategori:
 - `Web`

### Soru:
```
TR:
Dayımın kapı önünde fotoğrafı vardı açamıyorum :(

EN:
There was a photo of my uncle in front of the door, I can't open it
```

---

## Çözüm:
```
- West.Gate.jgp adında bir jpg dosyası veriliyor ancak açmaya çalıştığımızda açılmıyor. Steghide info komutu ile baktığımızda dosya is not supported diyor.
- Dosyanın magic number jpg magic number’ından farklı. Bunun için dosyayı hexeditor ile açıp  JPG için geçerli magic number’ı girdiğimizde dosya artık geçerli oluyor.
- West_Gate.jpg dosyasını açtığımızda görüntü bize Yüzüklerin Efendisi filminde geçen Moria Kapısını akla getirmektedir. Filmi bilmeyen bir kişi Google’da fotoğrafı aratırsa ipucu yakalayacaktır.
- Terminalde bu dosyayı steghide aracı ile incelediğimizde içinde bir dosya olduğunu ve bunu çıkarmak için bir passphrase girmek gerektiğini görüyoruz. Görüntüdeki kapının üstünde Elfçe “Söyle, dost öyle gir” yazıyor. Filmde bu kapıyı açmak için Elfçe dost anlamına gelen “mellon” kelimesini söylemek gerekiyor. 
- Bu anahtar kelimeyi girdiğimizde “altin_kapilarimiz_kan_oldu_tayfun.txt” adında bir text dosyası çıkıyor. Text dosyasında bir URL var.
- URL’i ziyaret ettiğimizde bir Post uygulaması bizi karşılıyor. 
- Bir post ekliyoruz.
- Sonrasında post başlıklarının bulunduğu sayfaya gidiyoruz. 
- Bir post’u görüntülediğimizde URL’de topic_id parametresi dikkatimizi çekiyor.
- Bu parametreye SQL Injection denediğimizde (7‘ or 1=1-- - gibi bir payload) bütün postların listelendiğini görüyoruz.
- Sorguyu otomatize etmek için SQLMap aracını kullanacağız. Bunun için istek paketini SQLMap’e vermek gerekiyor. İstek paketini Burp aracı ile yakalıyoruz.
- İsteği kopyalayıp bir dosyaya kaydediyoruz.
- İsteği kaydettiğimiz dosyayı SQLMap’e veriyoruz ve SQLMap ile veritabanını dump’lıyoruz.
- Dump edilen verilerde “secret_info” adında bir kolonda “enaktarlar_goltugun_altinda.php” adında bir veri dikkatimizi çekiyor. Bu directory’e gittiğimizde flag elde edilmiş olunuyor.
```
