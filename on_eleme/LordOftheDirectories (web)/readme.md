# STMCTF'22 Ön Eleme

## Soru İsmi:
`Lord Of the Directories`


## Kategori:
- `Web`


## Soru:

```
TR:
Bayrağı bulmak için yüzüğü ara

EN:
Search the ring to find the flag
```

---

## Çözüm:
```
Button1 ve 2’ye tıklayarak yukarıda url değiştiğini görülür.
Inspector’u açınca: 
<div>
	<a href=“lotr.php?file=2.php>
		<div>
			<div>
				<div>
					<!- -  HTML Comment “Hint is under /flag/flag.php”  - ->
bulunur.


Sorguya: 
- info.php 
- /flag/flag.php
- ../flag/flag.php
ve benzeri bir sorgu girilebilir ancak herhangi bir sayfaya yönlendirilmez.

Eğer sorguya “..././info.php” girerse php info sayfasına erişilebilir.
Buradan sonra kullanılması gereken payloadın “..././“ olduğu anlaşışır ve “…/./flag/flag.php” payload’ı ile flag’e erişir. 	
```