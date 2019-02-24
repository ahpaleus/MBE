# lab8C
> After the first three standard file descriptors, each additional file descriptor will be increased by one.(e.g. 3, 4, 5, etc.). 
> http://www.phearless.org/istorija/razno/fdleak.txt

```bash
lab8C@warzone:/levels/lab08$ ./lab8C -fn=/home/lab8B/.pass -fd=3
"<<<For security reasons, your filename has been blocked>>>" is lexicographically equivalent to "3v3ryth1ng_Is_@_F1l3
"
```
File descriptor: 
```sh
fd = 3
```
bypasses:
```c
if(fd1 == 0 || fd2 == 0)
	{
		printf("Invalid fd argument.\n");
		printf("(We're still fixing some bugs with using STDIN.)\n");
		printf("Usage: %s {-fn=<filename>|-fd=<file_descriptor>} {-fn=<filename>|-fd=<file_descriptor>}\n", argv[0]);
		return EXIT_FAILURE;
	}
```
