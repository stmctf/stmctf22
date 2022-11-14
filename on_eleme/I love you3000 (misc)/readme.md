# STMCTF'22 Ön Eleme

## Soru İsmi:
`I love you 3000`


## Kategori:
- `misc`


## Soru:

```
TR:

EN:

```

---

## Çözüm:

```python
import urllib.request
for i in range(450000):
    contents = urllib.request.urlopen("http://iloveyou3000.ctf.local/").read()
    print(contents)
```

scripti çalıştırılarak flag'in ekrana yazılması beklenir.