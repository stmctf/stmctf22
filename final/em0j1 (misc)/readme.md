# STMCTF'22 Final

## Soru İsmi:
`em0j1`


## Kategori:
- `Misc`


## Soru:

```
TR:
Yaka kartlarınıza bir not bıraktık.

EN:
We left a note on your badges.
```


---

## Çözüm:

Flag önce binary'e çevrilip 4'e bölünmüştü. Daha sonra her bir grup için farklı iki adet emoji seçilip 1 ve 0 yerine bu emojiler koyulmuştu. Dört farklı emoji grubu yarışmacı takımın dört farklı üyesinin kartlarına yapıştırmıştık. Üç kişilik takımlarda bir kartta iki emoji grubu olmuştu. Emoji gruplarının sırasının bulunması için STMCTF ile başlayanın ilk, } ile bitenin son grup olduğu bulunduktan sonra 2 ve 3'üncü gruplar da denenerek bulunabiliyordu. Örnek bir emoji grubu şu şekildedir.

Emoji gruplarının herbiri 8'in tam katı şeklinde omayabilir. Bir sonraki grup ile bağlantılı olan kısımları bulunabilmektedir. 

👍👎👍👎👍👍👎👎👍👎👍👎👍👎👍👍👍👎👍👍👎👎👍👎👍👎👍👍👍👍👎👎👍👎👍👎👍👎👍👍👍👎👍👍👍👎👎👍👍👎👎👎👎👍👎👎👍👎👍👍👍👍👎👍👍👎👎👎👍👎👍👎👍👎👍👎👎👎👎👎👍👎

👻👽👽👽👻👽👽👻👻👽👻👽👽👻👽👻👻👻👽👽👻👽👽👻👽👻👻👻👻👻👽👻👻👽👻👻👻👻👽👻👻👻👻👽👽👻👽👻👻👻👽👻👽👻👽👻👻👽👻👻👻👽👽👻👽👻👻👻👻👻👽👻👻👽👻👻👽👻👽👻👻👻

🐞🦋🐞🦋🐞🐞🦋🦋🦋🦋🦋🦋🐞🦋🐞🦋🦋🦋🦋🦋🐞🦋🐞🐞🐞🐞🦋🐞🐞🦋🦋🐞🦋🐞🐞🦋🐞🦋🦋🦋🦋🐞🦋🐞🐞🦋🦋🐞🦋🐞🐞🦋🐞🦋🐞🦋🦋🦋🦋🦋🐞🦋🦋🦋🐞🦋🐞🦋🐞🦋🦋🦋🦋🐞🐞🦋🐞🦋🦋🐞🐞🐞

😬🥶😬🥶🥶🥶😬😬🥶😬😬😬🥶🥶😬😬😬🥶😬🥶🥶🥶🥶😬😬🥶😬🥶🥶😬🥶🥶🥶🥶😬🥶🥶🥶😬😬🥶😬😬🥶😬🥶🥶🥶🥶🥶😬🥶🥶😬🥶🥶😬🥶😬🥶🥶🥶😬🥶😬🥶😬😬🥶🥶🥶🥶🥶🥶😬🥶🥶🥶🥶🥶😬🥶


```
1
"\U0001F44E" # thumbs down  👎
"\U0001F47B" # ghost        👻
"\U0001F98B" # butterfly    🦋
"\U0001F976" # cold face    🥶

0
"\U0001F44D" # thumbs up        👍
"\U0001F47D" # alien            👽
"\U0001F41E" # lady beetle      🐞
"\U0001F62C" # grimacing face   😬
```