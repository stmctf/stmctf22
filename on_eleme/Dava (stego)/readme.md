# STMCTF'22 Ön Eleme

## Soru İsmi:
`Dava`


## Kategori:
 - `Steganografi`


## Soru:

```
TR:
Johnny-Amber davası sonuçlandı.Ama elimizde basına sızmayan deliller var.

EN:
The Johnny-Amber case is over. But we have evidence that hasn't leaked to the media.
```

---

## Çözüm:

```
Dosyayı windows media player ile aç veya exiftool ile qr kodu elde et. 
Qr kodu tara 
Pdf dosyasının şifresini kır 
pdfcrack -f case.pdf -w /usr/share/wordlist.rockyou.txt
Pdf dosyasında ctrl A diyince beyaz bir şekilde flag var
```

