import binascii
import random
import os

def crypt():
    filename = str(input("file name : \n> "))
    with open(filename, 'rb') as f:
        content = f.read()
    c = binascii.hexlify(content)
    #print(c)
    c = str(c).replace("b'", "")
    c = c.replace("'", "")

    a = []
    c = [ord(i) for i in c]
    le = len(c)


    key = str(input("key :\n> "))
    k = [ord(i) for i in key]

    cr = []
    #===========================================code
    for i in range(le):
        #print(i)
        a = c[i]
        b = k[(le+i)%len(k)]
        d = a + 1
        cr.append(str(d)+"g")
    #===========================================code

    tamp = open("tampon", "w")
    for i in range(len(cr)):
        tamp.write(str(cr[i]))
    tamp.close()
    ####===============================================================done
    filename = 'tampon'
    with open(filename, 'rb') as f:
        content = f.read()
    c = binascii.hexlify(content)

    c = str(c)
    c = c.replace("b'","")
    c = c.replace("'","")


    final = open(str(input("name of the output file :\n> ")), "w")
    final.write(c)

    final.close()

    os.remove("tampon")

crypt()
