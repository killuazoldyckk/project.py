import random

def tebak(x):
    angka_acak = random.randint(1,x) # dimasukkan sebuah angka acak dengan range antara 1 dan x kedalam variabel angka_acak. 
    tebak=0 #store value before using its contain
    while tebak != angka_acak :
        tebak = int(input(f'Tebak angka antara 1 dan {x}: '))
        if tebak < angka_acak :
            print('Maaf, coba lagi. Tebakan terlalu rendah')
        elif tebak> angka_acak :
            print('Maaf, coba lagi. Tebakan terlalu tinggi')
    
    print(f'Selamat, anda berhasil menebak angka {angka_acak} dengan benar !')
    
x=int(input('Masukkan batas atas angka : '))    
tebak(x)
    