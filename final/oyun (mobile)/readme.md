# STMCTF'22 Final

## Soru İsmi:

`Oyun`

### Kategori:

- `Mobile`

### Soru:

```
TR:


EN:

```

---

## Çözüm:
```
PS: '' içindekiler komutlardır.

APK çalıştırılmaya çalışılınca açılmayacak. Açılması için;
İlk Başta Source kodu ele geçirmek için;
'apktool d oyun.apk' (ile source kod elde edilir) (burada mainActivity sınıfında intent'in açılması için extra eklemeleri gerektiğini görecekler ve apk'nın açılması için aşağıdaki komut çalıştırılactır.)
Uygulamanın açılması için, adb.exe'nin olduğu dosyaya gidip (Android studioda sdk dosyasının içinde bulunan platform-tools dosyasının içinde) terminal açılıcak ve gerekli komutlar;
'adb shell' (adb shell'i açılır)
'am start -a android.intent.action.MAIN --es acil "susam" -n com.example.oyun/.MainActivity'

yazılır. Açıldıktıktan sonra 5 tane bulmaca tarzında boşluk doldurma ile karşılaşılır.
İlk bulmacanın cevabı;
Hint Kumaşı
İkinci bulmacanın cevabı;
Bir Kadın Çizeceksin
Üçüncü bulmacanın cevabı;
Her Aşk Ölümü Tadacak
Dördüncü bulmacanın cevabı;
Işıkları Söndürseler Bile
Beşinci bulmacanın cevabı;
We Could Be The Same

Son sayfaya gelince sayfada "Belki bir komponent eklemen lazım" diye bir mesajla karşılaşırlır. Source koda bakılınca bu sayfaya (activity_last.xml) bağlı backend kısmında (LastActivity.java) getFlag adlı kullanılmayan bir metot olduğu gözükülür ve yeni bir buton oluşturulup bu butonun da "onClick" attribute'una "getFlag" metodu verilir.

Uygulamanın apk haline getirilmesi için;
'apktool b oyun' (komutu çalıştırılarak apk dosyası oyun/dist/oyun.apk dizininde bulunur)

Apk build edildiği için imzalanmalıdır. Bu yüzden aşağıdaki komutlarla apk imzalanılır;
'keytool -genkey -v -keystore my.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias app'
'zipalign -p 4 oyun.apk aligned.apk'
'apksigner sign --ks-key-alias app --ks my.keystore aligned.apk'

Uygulama yeniden çalıştırıldığında ve son sayfaya tekrar geldiğinde butona basılır ve flag ekrana basılır.
```