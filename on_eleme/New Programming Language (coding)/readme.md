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

### Java:

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

### Python:

```python
data = "++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++.----------->@>>.<@<<<.@<@<@<++++<.<@<@<<@<-----.<<<<<.<@<@<+<.+>@.-------.-------->>>.<@<@<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++>>>.<@<@<<.-----------<.>@>@<@><<.>@>@++++<.>@-----.>>>.<@<@<+<.>@+.-------.--------.+++++++++++++>>>>>>.<@<@<@<@<@<<.>@++.-------<.>@+++++++<<<.>@>@>@<<.>@>@<.>@-<.>@++++++++++++<<<.>@>@>@+++++++++++€"

stack = [0]

def firstToLast():
    stack.insert(len(stack)-1,stack.pop(0))

def lastToFirst():
    stack.insert(0,stack.pop(len(stack)-1))

def incLast():
    stack[-1] += 1

def decLast():
    stack[-1] -= 1

def exchangeLast2():
    stack[-1],stack[-2]=stack[-2],stack[-1]

def duplicateLast():
    stack.append(stack[-1])

def printAscii():
    result = ''
    for i in stack:
        result = result+chr(i)
    print(result)

def compiler(data):
    if data == '+':
        incLast()
    if data == '-':
        decLast()
    if data == '.':
        duplicateLast()
    if data == '@':
        exchangeLast2()
    if data == '>':
        firstToLast()
    if data == '<':
        lastToFirst()
    if data == '€':
        printAscii()

for x in data:
    compiler(x)
```