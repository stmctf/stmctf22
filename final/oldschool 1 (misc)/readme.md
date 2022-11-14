# STMCTF'22 Final

## Soru İsmi:
`oldschool 1/3`


## Kategori:
- `Misc`


## Soru:

```
TR:
ZIP dosyasını açın, flag orada.

EN:
Unzip the ZIP file, the flag is there.
```

---

## Çözüm:

Zip'li dosya açıldığında içerisinden boyutları ve MD5 HASH değerleri aynı olan 41166 adet dosya çıkmaktadır. İlk dosyalara bakıldığında hepsinin içeriğinin aşağıdaki şekilde olduğu görülüyor.


```text
base64.b64decode('RkxBRyBidSBkb3N5YWRhIGRlZ2lsL1RoZSBGTEFHIHlvdSBhcmUgbG9va2luZyBmb3IgaXMgbm90IGluIHRoaXMgZmlsZQ==') # PYTHON3 COMMAND
......
......
STMCTF'22 final istanbul
```

Dosyanın başlangıcında bulunan python kodu çalıştırıldığında 'FLAG bu dosyada degil/The FLAG you are looking for is not in this file' verisini goruyoruz.

```python
>>> import base64
>>> base64.b64decode('RkxBRyBidSBkb3N5YWRhIGRlZ2lsL1RoZSBGTEFHIHlvdSBhcmUgbG9va2luZyBmb3IgaXMgbm90IGluIHRoaXMgZmlsZQ==')
b'FLAG bu dosyada degil/The FLAG you are looking for is not in this file'
>>>
```

Dosya isimleri şüpheli görülmektedir. (Çözüm için bu adım atlanabilir. **Tuzak olarak koyulmuştur.**)

```
000000_4d5a9000
000001_03000000
000002_04000000
000003_ffff0000
000004_b8000000
000005_00000000
000006_40000000
000007_00000000
000008_00000000
000009_00000000
.....
.....
.....
041156_456e7465
041157_72437269
041158_74696361
041159_6c536563
041160_74696f6e
041161_4034005f
041162_5f696d70
041163_5f5f6677
041164_72697465
041165_00
```


Dosyalar, dosya isimlerine göre küçükten büyüğe doğru sıralanırsa ilk dosya isminin _  karakterinden sonra 4 byte'lık veri olduğu anlaşılabilir. MZ olan PEEXE header bilgisi olan **4d5a** değeri bu şüpheyi kuvvetlendiriyor. Eğer dosya isimleri kullanılarak PEEXE dosyası çıkartılmak istenirse aşağıdaki python kodu kullanılabilir.


```python
from os import walk
f = []
with open("pefile.exe","wb") as bin:
    for (dirpath, dirnames, filenames) in walk("flag"):
        for f in filenames:
            print(f)
            d = f.split("_")[1]
            bin.write(bytearray.fromhex(d))
        break
```

veya aşağıdaki bash kodu kullanılabilir.
```bash
for i in $(ls -1); do bytes=$(echo $i | cut -d "_" -f2); echo "$bytes" | xxd -r -p; done > pefile.exe
```

Elde edilen pefile.exe dosyasını çalıştırdığımızda aşağıdaki ekran ile karşılaşıyoruz. Malesef aradığımız flag burada da değil.

```raw

				   _|_|_|  _|_|_|_|_|  _|      _|    _|_|_|  _|_|_|_|_|  _|_|_|_|    _|_|      _|_|
				 _|            _|      _|_|  _|_|  _|            _|      _|        _|    _|  _|    _|
				   _|_|        _|      _|  _|  _|  _|            _|      _|_|_|        _|        _|
				       _|      _|      _|      _|  _|            _|      _|          _|        _|
				 _|_|_|        _|      _|      _|    _|_|_|      _|      _|        _|_|_|_|  _|_|_|_|
				 _|              _|                          _|                  _|
				       _|_|_|  _|_|_|_|    _|_|_|  _|_|_|    _|_|_|    _|    _|  _|
				 _|  _|_|        _|      _|    _|  _|    _|  _|    _|  _|    _|  _|
				 _|      _|_|    _|      _|    _|  _|    _|  _|    _|  _|    _|  _|
				 _|  _|_|_|        _|_|    _|_|_|  _|    _|  _|_|_|      _|_|_|  _|


				:( Ugrastin, eline saglik. Ama FLAG bu dosyada degil.
				:( You worked hard, good luck. But FLAG is not in this file.


				@misc{cryptoeprint:2004/199,
				author = {Xiaoyun Wang and Dengguo Feng and Xuejia Lai and Hongbo Yu},
				title = {Collisions for Hash Functions MD4, MD5, HAVAL-128 and RIPEMD},
				howpublished = {Cryptology ePrint Archive, Paper 2004/199},
				year = {2004},
				note = {\url{https://eprint.iacr.org/2004/199}},
				url = {https://eprint.iacr.org/2004/199}
				}
```

Çalıştırdığımız dosyanın ekrana bastığı bilgilerden Collisions for Hash ve URL adresindeki yayından MD5 collision olma ihtimalini elemediğimizi anlıyoruz. ZIP dosyası içerisinden çıkan 41166 adet dosyada bazı dosyaların farklı olabileceği aklımıza geliyor. Aşağıdaki komutlar ile farklı dosyayı bulmaya çalışıyoruz.

```bash
md5sum * | cut -f1 -d " "  | sort | uniq
592b0212688f238c478b683cf33901e8

sha256sum * | cut -f1 -d " "  | sort | uniq
aab4de510190bbd9bfdb088faf618c147eaf95fa9dda4023e89f5f7521f1c606
caf9540acc1842b655fc88f8413cae63727fd8a18781849e72c0548725ca1279
```

SHA256 değeri farklı bir dosya olduğu anlaşılıyor. Bu dosyanın içeriğine baktığımızda FLAG olabilecek bir başka python kodu çıkıyor.

```bash
sha256sum * | grep -v caf9540acc1842b655fc88f8413cae63727fd8a18781849e72c0548725ca1279
aab4de510190bbd9bfdb088faf618c147eaf95fa9dda4023e89f5f7521f1c606  034452_00000000

cat 034452_00000000
base64.b64decode('U1RNQ1RGe01ENV9IMUNfZ3V2ZW5pbGlyX2RlZ2lsXzpEfSBTVE1DVEZ7TUQ1X2lTX24wdF9yZWxpNGJsZV9hdF9hbGxfOkR9') # PYTHON3 COMMAND          
??b??STMCTF'22 final istanbul
```

Python kodunu çalıştırdığımıza flag karşımıza çıkıyor.
```python
>>> import base64
>>> base64.b64decode('U1RNQ1RGe01ENV9IMUNfZ3V2ZW5pbGlyX2RlZ2lsXzpEfSBTVE1DVEZ7TUQ1X2lTX24wdF9yZWxpNGJsZV9hdF9hbGxfOkR9')
b'STMCTF{MD5_H1C_guvenilir_degil_:D} STMCTF{MD5_iS_n0t_reli4ble_at_all_:D}'
```
