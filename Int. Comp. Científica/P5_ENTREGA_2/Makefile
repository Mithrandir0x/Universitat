CC = gcc
CFLAGS = -ansi -pedantic -O -Wall -Wno-unused-result
DEPS = ../COMMON/lib/zero_funcions.o ../COMMON/lib/algebra_lineal.o ../COMMON/lib/vector.o ../COMMON/lib/matriu.o

clean:
	del *.o *.exe *.res

clean_u:
	rm *.exe *.o

compile: newton1 conca newton3

n1: newton1
	cat inputs/n1.in | ./newton1.exe > newton.out.txt

n2: conca
	cat inputs/n2.in | ./conca.exe > conca.out.txt

newton3:
	$(CC) -c -g newton3.c $(CFLAGS)
	$(CC) newton3.o $(DEPS) -o newton3.exe -lm

conca:
	$(CC) -c -g conca.c $(CFLAGS)
	$(CC) conca.o $(DEPS) -o conca.exe -lm

newton1:
	$(CC) -c -g newton1.c $(CFLAGS)
	$(CC) newton1.o $(DEPS) -o newton1.exe -lm