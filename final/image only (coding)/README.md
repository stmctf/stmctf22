# STMCTF'22 Final

## Soru İsmi:

`image only`

### Kategori:
 - `Coding`

### Soru:
```
TR:
Resim birçok parçaya ayrılmış ve opaklaştırılmıştır, resmin orjinal haline dönüştürülmesinde yardım eder misin ?

Not: Bulunan veri STMCTF{} formatı içerisine yazılmalıdır.

EN:
The picture is divided into many parts and opaque, can you help to convert the picture to its original state?

Note: The found data should be written in STMCTF{} format.

```

---

## Çözüm:
```
Firstly, the puzzle must be solved. There are two ways for it. First one is cutting all the pieces and put them together
by a human hands and intelligence. Other way is using and algorithm. The appropriate approach is comparing pieces by their
edges in HSV channels. After solving the puzzle we shoulde have something like this https://ibb.co/fSG9dSX hence the first stage is solved.
Now we need to find the message. The message is hidden under the ...8888888.... characters but it cannot be detected by human eyes. So, we need
to apply appropriate masks to find it. The suggested method is using a slider that we can apply every color range. After using masks on solved
puzzle we can see something like this https://ibb.co/QMc3JL2. Here some of the text we saw is actually dummy data. Only the one in the up center is
meaning something. The message is "6962622E636F2F5A54665A584E4E" but it is hexadecimal characters. They translates into a link "https://ibb.co/ZTfZXNN"
wich is the flag
```