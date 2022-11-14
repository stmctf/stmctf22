# STMCTF'22 Final

## Soru İsmi:

`Netpoisoner`

### Kategori:
 - `PWN`

### Soru:
``` 
TR:


EN:

```

---

## Çözüm:
```
1) Hedef sistemde yalnızca TCP/22. portun açık olduğu tespit edilir.
2) Girdi noktasına IP adresi girilip çalıştırıldığında ping komutu çıktısı ekrana gelmektedir. Noktalı virgül (;), veya (||), ve (&&) gibi operatörler ile ping sonrası çalıştırılacak netcat komutu ile reverse shell alınabilir. 
3) ARP Spoof ile MITM saldırısı yapıldığında hedef sistemden bir takım DNS trafiğinin olduğunu görüyoruz. Gidilmek istenen domain www.example.com bu bir TLS trafiği olabilir.
4) DNS Spoof ile example.com domain'ine yapılan sorguları ortadaki adama (saldırı makinesi) yönlendirilir.
5) Saldırı makinesinde basitçe sertifika oluşturulur ve bu sertifika socat openssl ile TCP/443. port dinlenmesi için kullanılır. 
	openssl req -x509 -newkey rsa:4096 -keyout serverKey.pem -out serverCert.pem -days 10000 -nodes
	socat ssl-l:443,reuseaddr,fork,cert=serverCert.pem,key=serverKey.pem,verify=0 -
6) Gelen GET sorgusu içerisindeki Cookies parametresinde user kullanıcısının parolası bulunmaktadır.
7) User kullanıcısı ile hedef makineye SSH bağlantısı yapılır ve user.txt içerisindeki ilk bayrak yakalanır.
8) Yetki yükseltmek için systemctl programının SUID bitinin ayarlanmış olduğunu keşfedip buradan root hakkı elde etmeye çalışabilirsiniz. Yetki yükseltmede ikinci bir yöntem ise logeraser.sh 
dosyasının servis şeklinde çalıştığının, user kullanıcısı tarafından değiştirilebileceğinin farkına varılarak bu dosya içerisine tek satırlık netcat komutunun yazılması ve systemctl ile servisin yeniden başlatılmasıdır.
```