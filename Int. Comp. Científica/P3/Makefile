clean:
	del *.o *.exe *.res

all: clean p1.exe

ex2: p2.exe
	type inputs\ex2.in | p2

ex1_ap_a: p1.exe
	type inputs\ex1_ap_a.in | p1

p2.exe:
	gcc -c p2.c -ansi -pedantic -O -Wall
	gcc p2.o ../COMMON/lib/utils.o -o p2.exe -lm

p1.exe:
	gcc -c p1.c -ansi -pedantic -O -Wall
	gcc p1.o -o p1.exe -lm
