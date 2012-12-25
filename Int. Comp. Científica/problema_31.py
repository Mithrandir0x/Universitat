
import math

def f(x):
    return math.sqrt(x)

def integral_composta_trapezi(d):
    n = len(d)
    a = d[0][0]
    b = d[n - 1][0]
    h = ( b - a ) / ( 2.0 * n )
    sum = 0.0
    for i in range(1, n - 1):
        sum += d[i][1]
    return h * ( d[0][1] + ( 2.0 * sum ) + d[n - 1][1] )

def integral_composta_simpson(d):
    n = len(d)
    a = d[0][0]
    b = d[n - 1][0]
    h = ( b - a ) / ( 3.0 * n )
    sum0 = 0.0
    sum1 = 0.0
    for i in range(1, n - 1):
        if i % 2 != 0:
            sum1 += d[i][1]
        else:
            sum0 += d[i][1]
    return h * ( d[0][1] + ( 4.0 * sum1 ) + ( 2.0 * sum0 ) + d[n - 1][1] )

def main():
    data = [
        [1.00, 1.00000],
        [1.05, 1.02470],
        [1.10, 1.04881],
        [1.15, 1.07238],
        [1.20, 1.09544],
        [1.25, 1.11803],
        [1.30, 1.14017]
    ]

    print integral_composta_trapezi(data) #13.5018345
    print integral_composta_simpson(data) #13.502377

main()
