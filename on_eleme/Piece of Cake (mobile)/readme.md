# STMCTF'22 Ön Eleme

## Soru İsmi:
`Piece of Cake`


## Kategori:
- `Mobile`


## Soru:

```
TR:
Yeni şubemizden de sipariş verebilirsiniz.

EN:
You can also order from our new branch.
```

---

## Çözüm:
```
1-Uygulama emülatörde çalıştırılır.Pasta resimlerine tıklanarak "Bu yazılar boşuna yazılmadı" ipucundan apk decompile edilir. 
apktool d Bento Cake.apk
2-Kodta res/values/strings.xml alanından flag bulunur.
```