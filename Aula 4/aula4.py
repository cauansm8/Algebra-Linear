import numpy as np

# testar se uma função é linear

    # 1 - valor_1 = f(alpha * x + beta *y)
    # 2 - valor_2 = alpha * f(x) + beta f(y)
    # 3 - return valor_1 == valor_2

def test_linear (f, x, y, a, b):
    
    valor_1 = f(a*x + b*y)
    valor_2 = a*f(x) + b*f(y)

    return np.allclose(valor_1, valor_2) # verifica se são iguais (considerando que o ponto é flutuante)

# usando com função média

# f = lambda x:np.mean(x) -> um forma de definir uma função como variável
f = np.mean # definindo uma função média numa variavel

# randomizando 5 elementos para o vetor x e y
x = np.random.rand(5)
y = np.random.rand(5)

# também pode ser valores aleatorios
a = np.random.rand(1)
b = np.random.rand(1)


eh_linear = test_linear(f, x, y, a, b)
print (f"É linear:{eh_linear}")

# se tiver algum caso que der false -> não é linear

# EXERCICIO !!!!!! -> fazer o teste múltiplo com avg e testar com a função max - min

def test_linear_multi(f, shape_input, num_test = 100):
    
    for i  in range (0, num_test):
        x = np.random.rand(shape_input)
        y = np.random.rand(shape_input)

        a = np.random.rand(1)
        b = np.random.rand(1)

        retorno = test_linear(f, x, y, a, b)

        if retorno == False:
            print ("Teste multiplo = false")
            return False

    print ("Teste multiplo = true")
    return True

# primeiro teste - com a funcao avg/média

print ("\nPrimeiro teste")
test_linear_multi(f, 5)

def max_min(vetor):
    
    menor = vetor[0]
    maior = vetor[0]
    i = 0

    while i < np.size(vetor):
        if vetor[i] > maior:
            maior = vetor[i]
        
        if vetor[i] < menor:
            menor = vetor[i]

        i += 1
    return maior - menor


# segundo teste - função max - min

f = max_min

print ("\nSegundo teste")
test_linear_multi(f, 5, 100)


# terceiro teste - xn - x1

def xn_xi(vetor):
    return vetor[-1] - vetor[0]

f = xn_xi

print ("\nTerceiro teste")
test_linear_multi(f, 5)


# EXERCICIO - encontrar o vetor a da função produto interno (se a função é linear)

def retorna_vetor_a (f, tamanho):
    a = np.zeros(tamanho)

    for i in range (tamanho):
        e = np.zeros(tamanho)
        e[i] = 1
        
        a[i] = f(e)

    return a

    # o produto interno de aTx é igual a função f(x)
    # f(x) = aTx

f = xn_xi
a = retorna_vetor_a(f, 5)
x = np.array([1, 3, 4, 5, 10])

print (f"\n\nFunção A do produto interno: {a}")
print (f"Vetor X do produto interno: {x}")
print (f"Produto interno aTx: {np.dot(a,x)}")
print (f"O resultado da função xn-x1: {xn_xi(x)}")

if f(x) == np.dot(a,x):
    print ("\n\nEncontramos o vetor A!")

