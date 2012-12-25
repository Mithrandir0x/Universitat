
class BinaryHeap():
    pass

class EnterpriseCost():
    def __init__(self, id, coste):
        self.id = id
        self.coste = coste

def coste_acumulado(e_d):
    sum = 0
    for i in range(len(e_d)):
        sum += M[i][e_d[i]]
    return sum

def coste_final(M, l):
    sum = 0
    ml = len(M)
    for i in range(ml - 1, ml - len(l) - 1, -1):
        sum += M[i][l[i]]
    return sum

def coste_minimo(M, p, e_d):
    l = len(M)
    min = [ float('inf') for i in range(l) ]
    for i in range(p + 1, l):
        for j in range(l):
            if not j in e_d:
                if M[i][j] < min[j]
                    min[j] = M[i][j]
    r = 0
    for i in range(l):
        if min[i] != float('inf')
            r += min[i]
    return r


def buscar(M, cota_inferior, cota_superior, p_a = 0, e_d = []):
    c = BinaryHeap()
    l = len(M)
    for i in range(l):
        if not i in e_d:
            m = coste_minimo(M, p_a, e_d + [i])
            if m < cota_superior:
                c.append(EnterpriseCost(i, m))
    if len(c) == 0:
        return []
    if len(c) == 1 and p_a == l - 1:
        ec = c.pop()
        return [ec.id]
    best_ec = None
    best_l = None
    for ec in c:
        if ec.coste < cota_superior:
            l = buscar(M, cota_inferior, cota_superior, p_a + 1, [ec.id] + e_d)
            if cota_superior > coste_acumulado(e_d) + coste_final(l)
                cota_superior = coste_acumulado(e_d) + coste_final(l)
                best_ec = ec
                best_l = l
    return [best_ec.id] + best_l

def reparto_empresas(M):
    l = len(M)
    cota_superior = 0
    cota_inferior = 0
    
    for i in range(l):
        cota_superior += M[i][i]

    for i in range(l):
        min = float('inf')
        for j in range(l):
            if M[i][j] < min:
                min = M[i][j]
        cota_inferior += min

    return buscar(M, cota_inferior, cota_superior)

