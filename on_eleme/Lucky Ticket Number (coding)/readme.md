# STMCTF'22 Ön Eleme

## Soru İsmi:
`Lucky Ticket Number`


## Kategori:
- `Coding`


## Soru:

```
TR:
Diyelim ki bir makinemiz veya simülasyonumuz var. (Bu, C, C++, Java vb. olarak kodlanabilir.)
Bu makine veya simülasyon, girdi olarak verdiğiniz bir tarihi alır ve size benzersiz bir bilet numarası verir.
Tarihi noktalama işareti kullanmadan "29091923" olarak girmeniz gerekmektedir. [GGAAYYYY]
Bu makine/simülasyon, çıktı almak için çeşitli algoritmalar kullanır.
Girilen tarih değerine göre aşağıdaki algoritmalar kullanılmaktadır.
- Gün ve Ay birbirine eşit ise örneğin her ikisi için 08 girilir. Girilen tarihi 19031903 olarak kabul etmesi ve çıktı alması beklenir.
- Yıl değeri çift ise girilen tarih değeri ters çevrilerek 100 yıl eklenir ve beklenen çıktıyı verir.
- Ay ve yıl tek ise yıl değerine 50 eklenir ve beklenen çıktıyı verir.
- Yıl değeri tek, gün ve ay değeri çift ise yıl değerine 1 ekleyin ve beklenen çıktıyı verir.
- Yıl değeri tek ve gün ve ay tek ise, yıl değerinden 1 çıkar ve beklenen çıktıyı verir.
- Diğer tüm durumlarda tarihi olduğu gibi kabul edip çıktısını verecektir.

Bugünün şanslı bilet numarası nedir?

EN:
Let's say we have a machine or a simulation. (This can be coded as C, C++, Java, etc.)
This machine or simulation takes a date you give as input and gives you a unique ticket number.
You need to enter the date as "29091923" without using any punctuation. [DDMMYYYY]
This machine/simulation uses various algorithms to output.
The following algorithms are used according to the entered date value.
- If Day and Month are equal to each other, for example, 08 was entered for both. It is expected to accept the entered date as 19031903 and output it.
- If the year value is even, 100 years is added by inverting the entered date value and it gives the expected output.
- If month and year are odd, 50 is added to the year value and gives the expected output.
- If year value is odd and day and month value is even, add 1 to year value and it gives expected output.
- If the year value is odd and the day and month are odd, subtract 1 from the year value and gives the expected output.
- In all other conditions, it will accept the date as it is and give the output.

What is today's lucky ticket number?

```

---

## Çözüm:
```c++
using namespace std;
#include<iostream>
#include<stdio.h>
#include<string.h>
#include <cstdio>
#include <sstream>
#include <stdlib.h>



/* Function to reverse arr[] from start to end*/
void reverseArray(int arr[], int start, int end)
{
    while (start < end)
    {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void decToHexa(int n)
{
    char hexaDeciNum[100];
    int i = 0;
    while (n != 0) {
        int temp = 0;
        temp = n % 16;
        // check if temp < 10
        if (temp < 10) {
            hexaDeciNum[i] = temp + 48;
            i++;
        }
        else {
            hexaDeciNum[i] = temp + 55;
            i++;
        }
        n = n / 16;
    }
    // printing hexadecimal number array in reverse order
    for (int j = i - 1; j >= 0; j--)
        cout << hexaDeciNum[j];
}

int main() {
    char date[10];
    int tot, n, x, a = 0, i = 0, j = 0, num[10];
    int parsedNum[10] = {};
    int reversedNum[10] = {};
    cout << "Enter the Date: \n";
    fgets(date, 10, stdin);
    tot = strlen(date);
    for (i = 0; i < tot; i++) {
        if (date[i] >= '0' && date[i] <= '9') {
            num[j] = date[i];
            num[j] = num[j] - 48;
            j++;
        }
    }


    for (i = 0; i < j; i++) {
        parsedNum[a] = num[i];  //get only number in integer array

        a++;
    }

    int numberx = 0;
    int numbery = 0;

    for (int i = 0; i < a; i++) {
        numberx *= 10;
        numberx += parsedNum[i]; //convert int array to integer
    }

    n = a;

    if (parsedNum[0] == parsedNum[2] && parsedNum[1] == parsedNum[3]) {
        numberx = 19031903;
        cout << "\nFlag => STM{";
        decToHexa(numberx);
        cout << "}";
    }
    else if (numberx % 2 == 0) {
        cout << "\nYear is even number for that get reverse the all line ";
        // Function calling
        reverseArray(parsedNum, 0, n - 1);
        cout << endl << "Reverse Opp Value:  ";
        for (x = 0; x < a; x++) {
            cout << parsedNum[x];
            reversedNum[x] = parsedNum[x];
        }
        for (int i = 0; i < a; i++) {
            numbery *= 10;
            numbery += reversedNum[i]; //convert int array to integer
        }
        numbery += 100;
        cout << "\nLast number=" << numbery << endl;
        cout << endl;
        cout << "\nFlag => STM{";
        decToHexa(numbery);
        cout << "}";
    }

    else if (parsedNum[1] % 2 == 1 && parsedNum[3] % 2 == 1 && parsedNum[7] % 2 == 1) {
        numberx = numberx - 1;
        cout << "\n-1 YEAR";
        cout << endl;
        cout << "\nFlag => STM{";
        decToHexa(numberx);
        cout << "}";
    }
    else if (parsedNum[3] % 2 == 1 && parsedNum[7] % 2 == 1) {
        cout << endl;
        cout << "\nFlag => STM{";
        numberx += 50;
        decToHexa(numberx);
        cout << "}";
    }


    else {
        cout << endl;
        if (parsedNum[1] % 2 == 0 && parsedNum[3] % 2 == 0) {
            numberx = numberx + 1;
            cout << "\n+1 YEAR";
            cout << endl;
            cout << "\nFlag => STM{";
            decToHexa(numberx);
            cout << "}";
        }

        cout << endl;
        cout << "\nFlag => STM{";
        decToHexa(numberx);
        cout << "}";
    }

    return 0;
}
```
