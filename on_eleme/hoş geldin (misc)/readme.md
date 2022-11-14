# STMCTF'22 Ön Eleme

## Soru İsmi:
`hoş geldin`


## Kategori:
- `misc`

## Soru:

```
TR:
STMCTF'22 ön elemelerine hoşgeldin. İlk flag resmin içinde. Isınma turu olarak düşün.

EN:
Welcome to the STMCTF'22 preselection. The first flag is in the picture. Think of it as a warm-up lap.
```

---

## Çözüm:
```
strings flag.jpeg | grep -i stmctf
```
