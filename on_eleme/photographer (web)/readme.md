# STMCTF'22 Ön Eleme

## Soru İsmi:
`Photographer`


## Kategori:
- `Web`


## Soru:

```
TR:
Bu meydan okuma, dahili bir sistemden fotoğraf indirme özelliğine sahiptir.

EN:
This challenge has a feature which download photos from an internal system.
```

---

## Çözüm:
```
1) 32292. Port üzerinden yayın yapan web sayfasının dizinleri tespit edilmeye çalışılır
2) "/images", "/test" ve "secret" isimli dizinlerin tespit edilmesi
3) "/test" dizini içerisinde yer alan sayfada Ping atılma denemesi için gerçekleştirilen istek ve cevap paketleri proxy yardımı ile incelenir ve sitenin 
statik olduğu her hangi bir işlem gerçekleştirilemediği tespit edilmesi
4) "/secret" dizini içerisinde flag'in hangi dizin altında olduğu "/flag/flag.php" tespit edilmesi
5) SSRF (Server Side Request Forgery),sunucu tarafı istek sahteciliği, bir saldırganın bir sunucunun işlevselliğini kötüye kullanmasına neden olarak, o sunucunun alanındaki, saldırganın doğrudan erişemeyeceği bilgilere erişmesine veya bunları değiştirmesine neden olduğu bir istismar türüdür.
5) "/images" dizini içerisinde yer alan "Image Downloader" uygulamasında SSRF zafiyeti bulunduğunun tespit edilmesi, url parametresine "http://localhost:32292/flag/flag.php" girdisi sağlanarak gerçekleştirilen istek ve cevap paketleri proxy yardımı ile incelendiğinde Flag elde edilir. İstek ve cevap paketleri incelenmezse, resim local cihaza indirilip incelenmesi ile
flag elde edilebilir.
```