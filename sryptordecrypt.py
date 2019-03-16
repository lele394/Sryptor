import binascii
import random
import os

def decrypt():
    final = open(str(input("file name :\n> ")), "r")
    final = final.read()

    data=final.strip()
    data=data.replace('\n', '')
    data = binascii.a2b_hex(data)
    with open('tampon', 'wb') as image_file:
        image_file.write(data)

    # ========= tampon ========
    filename = 'tampon'
    file = open(filename, "r")
    c = file.read()
    file.close()
    c = c.split("g")

    key = str(input("key :\n> "))
    k = [ord(i) for i in key]

    cr = []
    c.remove('')
    le = len(c)
    #===========================================code
    for i in range(le):

        a = c[i]
        b = k[(le+i)%len(k)]
        d = int(a) - int(1)
        cr.append(chr(d))
    #===========================================code
    d = cr

    d = "".join(d)
    data=d
    data=data.strip()
    data=data.replace('\n', '')
    data = binascii.a2b_hex(data)
    with open(str(input("final file name :\n> ")), 'wb') as image_file:
        image_file.write(data)

    os.remove("tampon")

decrypt()
