# STMCTF'22 Ön Eleme

## Soru İsmi:
`GPS Spoofing`


## Kategori:
- `Misc`


## Soru:

```
TR:
Manevra kabiliyeti yüksek ve maksimum hızı 144 m/s olan deneysel deniz aracının,
rüzgarsız ve sakin deniz koşullarında yapılan testleri sırasında "GPS Spoofing" yapıldığından şüpheleniyoruz.
Görevin Seyrüsefer verisini inceleyip olası "GPS Spoofing" yapılan ilk UTC zamanı hh:mm:ss formatında bulmak.


EN:

We suspect "GPS Spoofing" is being done during the tests of the experimental vessel with high maneuverability and maximum speed of 144 m/s in windless and calm sea conditions.
Your task is to analyze the Navigation data and find the first UTC time with possible "GPS Spoofing" in the format hh:mm:ss.
```

---

## Çözüm:

*Soruda platform hız limiti değeri verilmiştir. GPS alıcısının hız hesabını basite indirgeyecek olursak, raporlama zaman aralığı ve ardışık 2 koordinat arasındaki mesafe bilgilerini kullanarak hesaplamaktadır.
Project X10 .nmea dosyası text editörde açılır içindeki $GPRMC cümleciklerindeki "UTC of position fix" ve "speed over ground " alanlarını incelenir.
144m/s = 279.9 knot değeri platform maksimum hız değeridir. Bu değerden büyük ilk değer olası GPS spoofing  yapılması sonucunda oluşacaktır.*
