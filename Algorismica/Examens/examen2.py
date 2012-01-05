#
# examen2.py
#
# autor: olopezsa13
#

def anagrams(w1, w2):
    if len(w1) != len(w2): return 'No'
    w = w1 + w2
    pivotStart = 0
    pivotEnd = len(w) - 1
    print w
    while pivotStart < len(w1):
        i, j = pivotStart, pivotEnd
        print pivotStart, pivotEnd
        if w[i] == w[j]:
            pivotStart += 1
            pivotEnd -= 1
        else:
            while j > i:
                if w[i] == w[j]:
                    pivotStart += 1
                    break
                else:
                    j -= 1
            if j <= i: return 'No'
    print pivotStart, pivotEnd
    return 'Yes'

def intersection(v1, v2):
    result = []
    i, j = 0, 0
    while i < len(v1):
        if v1[i] == v2[j] and not v1[i] in result:
            result.append(v1[i])
            i += 1
        else:
            j += 1
        if j >= len(v2):
            j = 0
            i += 1
    return result

#print anagrams('amor', 'mora')
#print anagrams('amor', 'roma')
#print anagrams('mora', 'amor')
#print anagrams('roma', 'trai')
#print anagrams('armo', 'omar')
#print intersection([1, 3, 4, 8, 11], [2, 3, 4, 9, 11])
#print intersection([2, 2, 3, 3], [1, 2, 3, 4, 5, 6])
