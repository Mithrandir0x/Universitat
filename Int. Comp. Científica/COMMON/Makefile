clean:
	del /s *.o

lib: utils.o

utils.o:
	gcc -c include/utils.c -o lib/utils.o -ansi -pedantic -O -Wall
