# STMCTF'22 Final

## Soru İsmi:
`STMCTF FINAL HOSGELDIN`


## Kategori:
- `Misc`

## Soru:

```
TR:
STMCTF'22 final yarışmasına hoşgeldin. İlk flag PNG içinde.

EN:
Welcome to the STMCTF'22 final competition. The first flag is in PNG.
```

---

## Çözüm:
```bash
strings flag.png | grep -i stm
```