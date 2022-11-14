# STMCTF'22 Ön Eleme

## Soru İsmi:
`Chaos`


## Kategori:
- `Web`


## Soru:

```
TR:
Sistem yöneticimiz parolasını unuttu, bize yardım edin !

EN:
Our system manager forgot his password, help us !
```

---

## Çözüm:
```
1) 8000. Port üzerinden yayın yapan web sayfasının giriş sayfasına erişim sağlanır
2) Giriş denemesi için gerçekleştirilen istek ve cevap paketleri proxy yardımı ile incelendiğinde "X-Powered-By: PHP/7.0.33" başlığı içerisinde yer alan PHP sürüm bilgisi elde edilir.
3) PHP'nin“type juggling” veya “type coercion” adı verilen özelliği bulunmaktadır. Bu, farklı türdeki değişkenlerin karşılaştırılması sırasında PHP'nin önce bunları ortak, karşılaştırılabilir bir türe dönüştüreceği anlamına gelir.
Örneğin, PHP'nin "7 köpekyavrusu" dizesini 7 tamsayısıyla karşılaştırması gerektiğinde, PHP dizeden tamsayıyı çıkarmaya çalışacaktır. Dolayısıyla bu karşılaştırma True olarak değerlendirilecektir.
- (“7 köpekyavrusu” == 7) -> True
4) PHP'deki bu özelliğin istismar edilmesinin en yaygın yolu, onu kimlik doğrulamasını atlamak için kullanmaktır. Kimlik doğrulamayı işleyen PHP kodunun şöyle göründüğünü varsayalım:
 - if ($_POST["password"] == "Admin_Password") {login_as_admin();}
Ardından, 0'lık bir tamsayı girişi göndermek, başarılı bir şekilde yönetici olarak oturum açmanızı sağlar, çünkü bu, Doğru olarak değerlendirilecektir:
 - (0 == “Admin_Password”) -> True
Giriş için gerekli "user" parametresine "admin" kullanıcı adı girilerek, kimlik doğrulama atlatması için gerekli işlemi gerçekleştirmek için; "password" parametresine 0 ya da NULL değeri döndürmesi için dizi (array) yapısı ile girdi "password[]=1234" sağlanması 
5) Admin Panel ‘ine (dashboard) giriş yapılması
6) Admin Paneli üzerinde "Latest Members" alanında yer alan kullanıcıların fotoğrafları üzerine fare imleci ile gelindiğinde Base64 formatında veri bulunduğu tespit edilmesi
7) "Latest Members" alanındaki sayfa içeriği incelendiğinde "title" parametresinde yer alan Base64 formatındaki veriler deşifre edildiğinde, Nadia kullanıcısına ait "title" bilgisi içerisindeki Base64 değerinde flag'in elde edilmesi
```