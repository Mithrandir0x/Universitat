clean:
	del *.o *.exe *.res

all: clean p1.exe p2.exe p3.exe p4.exe p5.exe

tots: clean ex1_ap_a ex1_ap_bcd ex1_ap_bcd_float ex2_ap_a ex2_ap_b

ex3: p5.exe
	type inputs\ex3_01.in | p5
	type inputs\ex3_02.in | p5
	type inputs\ex3_03.in | p5
	type inputs\ex3_04.in | p5

ex2_ap_b: p4.exe
	type inputs\ex2_ap_b.in | p4

ex2_ap_a: p3.exe
	type inputs\ex2_ap_a.in | p3

ex1_ap_bcd_unix: p2.exe
	cat inputs\ex1_ap_b_100.in | ./p2.exe > coefs_ex1_ap_b_100.res

ex1_ap_bcd_float: p2_float.exe
	type inputs\ex1_ap_b_100.in | p2_float > coefs_ex1_ap_b_float_100.res

ex1_ap_bcd: p2.exe
	type inputs\ex1_ap_b_100.in | p2 > coefs_ex1_ap_b_100.res

ex1_ap_a: p1.exe
	type inputs\ex1_ap_a_100.in | p1 > coefs_ex1_100.res
	type inputs\ex1_ap_a_1000.in | p1 > coefs_ex1_1000.res
	type inputs\ex1_ap_a_10000.in | p1 > coefs_ex1_10000.res

p5.exe:
	gcc -c p5.c -ansi -pedantic -O -Wall
	gcc p5.o ../COMMON/lib/utils.o -o p5.exe -lm

p4.exe:
	gcc -c p4.c -ansi -pedantic -O -Wall
	gcc p4.o -o p4.exe -lm

p3.exe:
	gcc -c p3.c -ansi -pedantic -O -Wall
	gcc p3.o -o p3.exe -lm

p2_float.exe:
	gcc -c p2_float.c -ansi -pedantic -O -Wall
	gcc p2_float.o -o p2_float.exe -lm

p2.exe:
	gcc -c p2.c -ansi -pedantic -O -Wall
	gcc p2.o -o p2.exe -lm

p1.exe:
	gcc -c p1.c -ansi -pedantic -O -Wall
	gcc p1.o -o p1.exe -lm
