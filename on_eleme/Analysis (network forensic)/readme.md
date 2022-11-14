# STMCTF'22 Ön Eleme

## Soru İsmi:
`Analysis`


## Kategori:
- `Network Forensic`


## Soru:

```
TR:
Klasik bir pcap analiz sorusu.

EN:
A classic pcap analysis question.

```

---

## Çözüm:
```
Analysis.pcapng dosyasını wireshark ile açıyoruz. FTP trafiğini incelemek için ftp filtresi ile trafiği
filtreliyoruz.
```
![1](https://user-images.githubusercontent.com/74919981/191547773-f76616a4-28b7-45bb-8175-2af68cfdf43e.jpeg)
```
FTP sunucusu ile bağlantı kurulduğunda hata mesajı gibi görünen bir yanıt alıyoruz ancak 220
kodlu bu yanıt, sunucunun yeni bağlantı kuran istemci için hazır olduğunu belirtir. Sunucudan
dönen yanıt içerisinde gösterilen sözde hata mesajını online hash analiz toolu ile inceliyorum.
```
![2](https://user-images.githubusercontent.com/74919981/191547876-10b8df38-9726-4be0-bdba-2fd645412908.png)
```
İfadenin base64 ile kodlanmış olduğunu ve decode edilmiş halini görüyorum. Decode edilmiş metin
dosya parolasına benziyor: MY-V3rY_53CuR3_FtP_F1l3-P4Ss
Pcap dosyasındaki ftp trafiğini incelemeye devam ettiğimde x adlı uzantısı olmayan bir dosyanın
indirildiğini görüyoırum. İndirilen bu dosyayı yakalamak için pakete sağ tıklayıp Follow>TCP
Stream seçeneğini takip ediyorum. Streamler arasında biraz gezince 76 nolu streamde indirilen
dosyayı ve dosya uzantısının pdf olduğunu buluyorum.
```
![3](https://user-images.githubusercontent.com/74919981/191548090-4fe50ebf-316b-4e5b-974a-a8c34943e9ee.jpeg)
```
Show data as Raw seçerek ham veriyi dilediğim adda pdf uzantılı olarak kaydediyorum.
İndirilen x adlı pdf dosyasını yakalamış olduk ancak dosyayı açmaya çalıştığımda parola ile
korunuyor olduğunu görüyorum. Parola olarak yukarıda sözde hata mesajından elde ettiğim
parolayı kullanıyorum ve flag karşımda duruyor: 
**STMCTF{4R3_Y0U_N3TW0RK_M4ST3R?}**
```



