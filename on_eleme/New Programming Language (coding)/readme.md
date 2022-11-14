# STMCTF'22 Ön Eleme

## Soru İsmi:
`New Programming Language`


## Kategori:
- `Coding`


## Soru:

```
TR:

Arkadaşım tam bir "programlama dilleri ustası", o kadar ki, kendisi bir tane yapmaya karar verdi!

Dil şöyle çalışır:

 Dil yığına dayalıdır (biraz dizi gibi çalışır)
 Başlangıçta yığın, değeri 0 olan bir öğeden oluşur.

 "-" yığının son elemanının değerini 1 azaltır
 
 "+", yığının son öğesinin değerini 1 artırır
 
 ">" ilk öğeyi yığının sonuna koyar ve her birini aşağı kaydırır
 
 "<" son öğeyi yığının başına koyar ve her birini yukarı kaydırır
 
 "@" son 2 öğeyi değiştirir
 
 "." yığının son öğesini çoğaltır ve yığının sonuna koyar
 
 "€", her yığının öğesinin değerini ASCII olarak yazdırır (ilk öğeden son öğeye kadar)

Bu bilgilere dayanarak bana input.txt dosyasının çıktısını verebilir misiniz?


EN:

My friend is a total "programming languages master", to the point, that he's decided to make one himself!

The language works like that:

 Language is based on stack (works somewhat like an array)
 Initially stack consists of one element, which value is 0

 "-" decreases stack's last element's value by 1
 
 "+" increases stack's last element's value by 1
 
 ">" puts first element at the end of the stack and shifts every other down
 
 "<" puts last element at the beginning of the stack and shifts every other up
 
 "@" exchanges last 2 elements
 
 "." duplicates stack's last element and puts it at the end of the stack
 
 "€" prints out every stack's element's value in ASCII (from the first to the last element)

Based on that info, could you give me the output of input.txt?
```

---

## Çözüm:
```java
package ctf;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class CTF {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("İnput Giriniz:");
		Scanner girdi = new Scanner(System.in);
		String input = girdi.nextLine();

		ArrayList<Integer> list = new ArrayList<Integer>(); // Create an ArrayList object
		list.add(0);

		for (int i = 0; i < input.length(); i++) {
			String karakter = input.substring(i, i + 1);
			
			if(karakter.equals("+")) {
				int temp = list.get(list.size()-1);
				list.remove(list.size()-1);
				temp = temp + 1;
				list.add(temp);
			}
			
			if(karakter.equals("-")) {
				int temp = list.get(list.size()-1);
				list.remove(list.size()-1);
				temp = temp - 1;
				list.add(temp);
			}
			
			if(karakter.equals(">")) {
				int temp = list.get(0);
				list.remove(0);
				list.add(temp);
			}
			
			if(karakter.equals("<")) {
				int temp = list.get(list.size()-1);
				list.remove(list.size()-1);
				list.add(0, temp);
			}
			
			if(karakter.equals("@")) {
				Collections.swap(list, list.size() - 2 , list.size() - 1);
			}
			
			if(karakter.equals(".")) {
				int temp = list.get(list.size()-1);
				list.add(temp);
			}
			
			if(karakter.equals("€")) {
				#System.out.println(list);
				for(int j = 0 ; j < list.size(); j ++) {
					int a = list.get(j);
					char ch = (char) a;
					System.out.print(ch);
				}

			}

		}

	}

}

```