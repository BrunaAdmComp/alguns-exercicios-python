def fatorial(num):
    if num < 2:
        resultado = 1
    else:
        resultado = num*fatorial(num-1)
    return resultado

def funcao(N):
    for i in range(1,N):
        if fatorial(i) > N:
            return int(fatorial(i-1))
lista = []
N = int(input())
aux = 0
while N > 0:
    if N <= 2:
        valor = N
        aux += 1
        break
    else:
        valor = funcao(N)
        N = N - valor
        aux += 1
print(aux)