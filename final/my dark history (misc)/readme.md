# STMCTF'22 Final

## Soru İsmi:

`my dark history`


### Kategori:
 - `Misc`

### Soru:
```
TR:
Otonom uçuşlarında kullanılan pixhawk uçuş verileri manipüle edilmiştir. Doğru verilerin elde edilmesinde yardımcı olur musun ?

Not:Bulunan veri STMCTF{} formatı içerisine yazılmalıdır.

EN:
Pixhawk flight data used in autonomous flights has been manipulated. Can you help in obtaining the correct data?

Note: The found data should be written in STMCTF{} format.
```

---

## Çözüm:

```
Change the first four characters of the "question.ulg" from "KAli" to "ULog" using a hex editor (Suggested: https://hexed.it).
Open the "question.ulg" with any flight review parser that supports .ulg files (Suggested: https://review.px4.io).
Check the pattern made by the UAV from above.
The pattern is the flag.
The flag -> https://ibb.co/8r4DS9z
```