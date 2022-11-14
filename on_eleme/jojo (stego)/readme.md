# STMCTF'22 Ön Eleme

## Soru İsmi:
`JOJO`


## Kategori:
- `Steganography`


## Soru:

```
TR:
JOJO karakterlerin spoiler'ları burda.

EN:
Spoilers for JOJO characters are here.
```

---

## Çözüm:
```markdown
Açılan ilk sayfada çıkan resimler indirilerek exiftool ile fotoğrafların "Comment" kısmında yazılan japonca kelimelere/cümlelere translate'den bakılır JOJO karakterinden biri olan Dio brando'nun  fotoğrafında "このディオだ" ve diğerlerinde de "私じゃない" ve "間違いなく私ではない" gibi "ben değilim anlamındaki" cümleler vardır. Login ekranında username'i "dio" olup password'u "bu dio" (このディオだ'nın çevirisi) başka bir sayfaya giriş yapılır. 

Bu sayfada sadece JOJO karakterlerin soundtrack'leri bulunmaktadır. İndirilen .wav dosyaları ;

steghide extract -sf *.wav

ile kontrol edilir ve 3.satırın ilk dosyasından elde edilen wav dosyasından steghide ile flag.txt diye bir dosya çıkar ve flag bulunur.
```
