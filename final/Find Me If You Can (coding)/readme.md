# STMCTF'22 Final

## Soru İsmi:

`Find Me If You Can`

### Kategori:
 - `Coding`

### Soru:
```
TR:
Sizlere şöyle bir soru sormak istiyorum. Sorunun cevabı olan flag aşağıdaki şekilde olmalıdır.
STMCTF{harflerSAYI}
harfler: verilen data.txt dosyasında uzunluğu 8 olan satırlar yukarıdan aşağı sıralanır. Bu satırlar binary formattan decimal formata çevirilir. Elde edilen decimal değerlerin ASCII karşılığındaki harfler yazılır. Harfler yukarıdan aşağı okunduğunda flag'in harf kümesi elde edilir.
SAYI: Verilen data dosyasında 0' ların sayısının 3'ün katı veya 1'lerin sayısının 2'nin katı olan kaç adet satır olduğu

Not: Bulunan veri STMCTF{} formatı içerisine yazılmalıdır.

EN:
I want to ask you a question. The flag, which is the answer to the question, should be as follows:
STMCTF{lettersNUMBER}
letters: Lines with a length of 8 in the given data.txt file are sorted from top to bottom. These lines are converted from binary format to decimal format. The letters in the ASCII equivalent of the decimal values obtained are written. When the letters are read from top to bottom, the letter set of the flag is obtained.
Number: How many rows in the given data file where the number of 0's is a multiple of 3 or the number of 1s is a multiple of 2

Note: The found data should be written in STMCTF{} format.
```

---

## Çözüm:
```java
package dosya;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class DosyaOku {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		File file = new File(``); //data.txt dosyasının pathi verilmelidir.
		FileReader fileReader = new FileReader(file);
		String line;
		BufferedReader br = new BufferedReader(fileReader);
		int str = 0;
		int temp0 = 0;
		int temp1 = 0;
		while ((line = br.readLine()) != null) {
			// System.out.println(line);
			for (int i = 0; i < line.length(); i++) {
				char karakter = line.charAt(i);
				if (karakter == '1') {
					temp1 = temp1 + 1;
				}
				if (karakter == '0') {
					temp0 = temp0 + 1;
				}
			}
			if (line.length() == 8) {
				System.out.println(line);
				int decimal=Integer.parseInt(line,2);  
				System.out.println(decimal);
				System.out.println((char)decimal);
			}
			if (temp0 % 3 == 0 || temp1 % 2 == 0) {
				str = str + 1;
			}
			temp0 = 0;
			temp1 = 0;

		}
		System.out.println(`0'ların sayısı 3ün, 1lerin sayısı 2'nin tam katı olan satır sayısı: `+ str);
		br.close();

	}

}
```
