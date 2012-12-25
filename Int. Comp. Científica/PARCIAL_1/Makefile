clean:
	rm *.exe *.o

ex: clean B-LopezSanchezOriol-E1
	./B-LopezSanchezOriol-E1.exe

compile: B-LopezSanchezOriol-E1

B-LopezSanchezOriol-E1:
	gcc -c -g B-LopezSanchezOriol-E1.c -ansi -pedantic -O -Wall -Wno-unused-result
	gcc B-LopezSanchezOriol-E1.o -o B-LopezSanchezOriol-E1.exe -lm
