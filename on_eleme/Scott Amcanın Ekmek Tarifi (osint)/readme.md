# STMCTF'22 Ön Eleme

## Soru İsmi:
`Scott Amcanın Ekmek Tarifi`


## Kategori:
- `OSINT`


## Soru:

```
TR:
 Scott amca ziyaretine gelecek, ona bir süpriz yapıp sana yıllar önce öğrettiği ekmekten yapmaya karar verdin.
 Fakat kullandığı unu bir türlü hatırlayamıyorsun.Scott amcaya mesaj atıp hangi unu kullanacağını sordun.
 Cevap olarak sadece bir ses dosyası geldi.
EN:

 Uncle Scott is coming to visit, you decide to surprise him and make the bread he taught you years ago.
 But you can't remember the flour he used. You texted Uncle Scott and asked which flour he would use.
 Only one audio file came in response.
```

---

## Çözüm:

```
Ekmek.mp3 dosyasının meta datası incelenir.Genre kısmında MGRS !!! yazdığı görülür.
 Askeri Grid Referans Sistemi (MGRS), NATO orduları tarafından Dünya üzerindeki noktaların yerini belirlemek için kullanılan coğrafi koordinat standardıdır.
 Ekmek.mp3 dosyası dinlendiğinde belirli yerlerde farklı seslerin varlığı anlaşılır.Dosyanın spectrogramı incelenir ve "58c eu 33874 81823" yazdığı görülür.MGRS formatında konumdur.
Herhangi Online mgrs  latlon dönüştürücüden konum  dönüşümü yapılır -77.6361810°, 166.4173056° bulunur. Google maps  kullanılarak ilgili konuma gidilir. Street view açılarak kulubenin içinde girilir.
rafta yer alan kutunun üstünden colman's flour yazmaktadır. 
```
