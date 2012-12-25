CC = gcc
CFLAGS = -ansi -pedantic -O -Wall -Wno-unused-result

clean:
	del /s *.o

clean_u:
	rm -r *.o

lib: algebra_lineal.o vector.o matriu.o zero_funcions.o

zero_funcions.o:
	$(CC) -c -g include/zero_funcions.c -o lib/zero_funcions.o $(CFLAGS)

vector.o:
	$(CC) -c -g include/vector.c -o lib/vector.o $(CFLAGS)

matriu.o:
	$(CC) -c -g include/matriu.c -o lib/matriu.o $(CFLAGS)

algebra_lineal.o:
	$(CC) -c -g include/algebra_lineal.c -o lib/algebra_lineal.o $(CFLAGS)
