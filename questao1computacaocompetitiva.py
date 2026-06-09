import math

def pre_computar_primos(limite):
    crivo = [True] * (limite + 1)
    crivo[0] = False
    crivo[1] = False
    for p in range(2, math.isqrt(limite) + 1):
        if crivo[p] == True:
            for i in range(p * p, limite + 1, p):
                crivo[i] = False
    return crivo
def avaliar_t_primos():
    tamanho_maximo_raiz = 1000000
    gabarito_primo = pre_computar_primos(tamanho_maximo_raiz)
    numeros_teste = [4, 5, 6, 9, 16, 49]
    for x in numeros_teste:
        raiz = math.isqrt(x)
        if (raiz * raiz == x) and (gabarito_primo[raiz] == True):
            print(f"O numero {x} POSSUI exatamente 3 divisores ")
        else:
            print(f"O numero {x} NAO possui exatamente 3 divisores")

avaliar_t_primos()
