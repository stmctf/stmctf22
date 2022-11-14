# STMCTF'22 Ön Eleme

## Soru İsmi:
`PASSW0RD`


## Kategori:
- `Reverse`

## Soru:

```
TR:
Flag HTML dosyada

EN:
FLAG is in the HTML file
```

---

## Çözüm:
```python
import hashlib
import base64
from cryptography.fernet import Fernet

image_bmp = "background_image.bmp"

digit_offset = 8190

users = ["guest", "fatma", "mehmet", "mustafa", "elif", "halil", "admin"]

file = open(image_bmp, "rb")
raw_bmp = list(file.read())
file.close()

pixel_and = [0b00000011, 0b00001100, 0b00110000, 0b11000000]

def get_string_from_bmp(start_address):
    string_in_bmp = ""
    endofstring = False
    while not endofstring:
        char = 0b00000000
        for x in range(4):
            pixel = raw_bmp[start_address]
            char = char | ((pixel & 0b00000011) << x*2)
            start_address += 1
        if char != 0:
            string_in_bmp += chr(char)
        else:
            endofstring = True
    return string_in_bmp


for user in users:
    print()
    print("Working...:", user)
    username_hash = (hashlib.md5(user.encode('utf-8')).hexdigest())
    username_hash_sum = 0
    for m in username_hash:
        if m.isdigit():
            z = int(m)
            username_hash_sum += z
    username_start_address = username_hash_sum * digit_offset
    username_in_bmp = get_string_from_bmp(username_start_address)
    if username_in_bmp == user:
        print("username_in_bmp OK:", username_in_bmp)
    else:
        print("Error in username")

    # PASSWORD HASH
    password_hash_start_address = username_start_address + username_hash_sum + 2048
    password_hash = get_string_from_bmp(password_hash_start_address)
    print("password_hash:", password_hash)


    # FLAG
    password_hash_sum = 0
    for m in password_hash:
        if m.isdigit():
            z = int(m)
            password_hash_sum += z
    flag_start_address = password_hash_start_address + password_hash_sum + 4096
    flag_in_bmp = get_string_from_bmp(flag_start_address)
    print("flag_in_bmp:", flag_in_bmp)

    password_hash_base64 = base64.urlsafe_b64encode(password_hash.encode('utf-8'))
    fernet = Fernet(password_hash_base64)
    flag_decrypted = fernet.decrypt(flag_in_bmp.encode())
    print("flag:", flag_decrypted.decode('utf-8'))

```
