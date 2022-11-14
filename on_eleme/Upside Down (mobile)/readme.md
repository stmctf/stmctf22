# STMCTF'22 Ön Eleme

## Soru İsmi:
`Upside Down`


## Kategori:
- `Mobile`


## Soru:

```
TR:
Zaman bir yandan kısıtlı bir yandan beklemeli

EN:
Time is limited on the one hand and must wait on the other hand
```

---

## Çözüm:

```
Uygulama API 29 ve üstü . Google Pixel 3a emülatör kullanılabilinir.

1-Apk çalışınca login ekranında görünmeyen bir buton var, decompiler edilip buton görünür hale getirilip tekrar paketlenir
veya butona gören yarışmacı butona tıklayarak register sayfasından üye olup tekrar login sayfasına login olur.
Kayıtlı bir kullanıcı yok. Mutlaka register sayfasından kullanıcı oluşturulmalı
2-Login olduktan sonra açılan sayfada bir soru karşılıyor. 3 denemeden sonra uygulamadan atılıyor.
Sorunun çözümü

M:300
A:180
B:0
T:240

Sonuç:720
3-720 yazılarak tamama tıklanır. Bir süre sonra hızlı bir video açılıyor. Videonun son dk flag ortaya çıkıyor.
Android tarafında aşağıdaki kod yazılarak video yavaş çalıştırılır ve flag görülür veya ekrandan flag yaklanmaya çalışılır


Video yavaşlatan kod 
------------------------------------------
 videoView.setOnPreparedListener(new MediaPlayer.OnPreparedListener() {
            @RequiresApi(api = Build.VERSION_CODES.M)
            @Override
            public void onPrepared(MediaPlayer mp) {
               
                PlaybackParams myPlayBackParams = new PlaybackParams();
                myPlayBackParams.setSpeed(0.25f); 
                mp.setPlaybackParams(myPlayBackParams);

                videoView.start();//start your video.
            }
        });

```