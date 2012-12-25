
import math

def ex30_f(x):
    return ( x * x ) - math.exp(x) + math.exp(-x)

def ex30_df(x):
    return ( 2.0 * x ) - math.exp(x) - math.exp(-x)

def diferencia_centrada(funcio, x, h):
    return ( funcio(x + h) - funcio(x - h) ) / ( 2.0 * h )

    """
    if rang == 2:
        A = diferencia_finita(funcio, x, h)
        B = diferencia_finita(funcio, x, h/2.0)
        return A + ( ( A - B ) / (-.5) )
    """
def richardson(funcio, diferencia_finita, x, h, rang = 2):
    if rang == 1:
        return diferencia_finita(funcio, x, h)
    else:
        A = richardson(funcio, diferencia_finita, x, h, rang - 1)
        B = richardson(funcio, diferencia_finita, x, h / 2.0, rang - 1)
        return  A + ( ( A - B ) / ( ( .5 ** (rang - 1) ) - 1 ) )

def main():
    x0 = .7
    h = 1

    df_x = ex30_df(x0)

    print "f'(%F) = %.15E" % ( x0, df_x )
    print

    for i in range(8):
        h = h / 10.0
        print "h = %e" % h
        aprox_df_x = diferencia_centrada(ex30_f, x0, h)
        print "f'(%F) = %.15E | Ea = %.15E (Diferencia finita)" % ( x0, aprox_df_x, abs(df_x - aprox_df_x) )
        for j in range(2, 5):
            richardson_df_x = richardson(ex30_f, diferencia_centrada, x0, h, j)
            print "f'(%F) = %.15E | Ea = %.15E (Richardson, j = %d)" % ( x0, richardson_df_x, abs(df_x - richardson_df_x), j )
        print

main()

#print ex30_f(0.7001)
#print ex30_f(0.6999)
