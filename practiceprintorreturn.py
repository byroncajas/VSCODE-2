def numero_maximo(a, b):
    if a > b:
        maximo = a
    else:
        maximo = b
    return maximo
numero_maximo(10,5)
print("numero maximo =",numero_maximo(10,5))


def num_min(a,b,c):
    if a<b<c:
        minimo=a
    if b<a<c:
        minimo=b
    if c<a<b:
        minimo=c
    return minimo
num_min(2,10,15)
print("número menor =",num_min(2,10,15))