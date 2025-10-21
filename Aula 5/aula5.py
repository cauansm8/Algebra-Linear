import numpy as np

# Como identificar se o conjunto de vetores (combinação linear) é l. independente ou l. dependente

# c1v1 + c2v2 + (...) cnvn = 0 -> c1 = c2 = (...) = cn = 0 -> linearmente independente
# se tiver algum ci != 0 -> linearmente dependente

    # posto/rank -> número maximo de vetores de uma combinação linear que são li


# rank = np.linalg.matrix_rank(lista_de_vetores/matriz)


v1 = np.array([1, 0 ,2])
v2 = np.array([0, 1, -1])
v3 = np.array([1, 1, 0])

lista = np.array([v1, v2, v3])

# retorna quantos são li
rank = np.linalg.matrix_rank (lista)
print (f"Posto: {rank}")

# se o rank é igual a quantidade de vetores -> li
if rank == np.size(lista):
    print ("\nSão li")


# projeção -> proj_u (v) = (v, u)     * u
#                           / (u, u)

#   retira a influência do vetor em outro (correlação)
#   por isso fica ORTONORMAL -> ângulo 90° e produto interno ou norma? = 1


# com os vetores LI (v1, v2, ..., vn) construimos (u1, u2, ..., u3) ortogonais:
# algoritmo de Gram-Schmidit
# u0 = v0
# u1 = v1 - proj_u0 (v1)
# u2 = v2 - proj_u0 (v2) - proj_u1 (v2)
# ...

# para se transformar em ortonormal
#   qi = ui / np.linalg.norm(ui)


""" CRIANDO A FUNÇÃO DE GRAM-SCHMITDIT """

def proj(v, u):
    return (np.dot(v, u) / np.dot(u, u)) * u

def ortogonalizar(vetores, normalizar = False):

    u = []
    u.append(vetores[0])

    for i in range (1, len(vetores)):

        subtracao = 0
        for j in range (i):
            subtracao += proj(vetores[i], u[j])

        u.append (vetores[i] - subtracao)

    norma = np.linalg.norm(u)
    # outra maneira de verificar se a norma é próxima de zero -> if np.allclose(u, 0): // verifica se todos os elementos são próximos de zero 
    #   lembrando que pe importante saber se é próximo de zero SE FOR NORMALIZAR (u = u / norma_de_u)

    # if para ver se norma é igual a zero (1 elevado a -10) -- erro de máquina não deixa chegar a zero
    if norma < 1e-10:
        print ("\nO conjunto é ld")

    if normalizar == True:
        u = u / (norma + 1e-10)
        # 1e-10 serve para: evitar erro (divisão por zero) e não ter muita diferença nos valores 

    return u

w1= np.array([1, 1, 1], dtype=float)
w2 = np.array([1, 1, 0], dtype=float)
w3 = np.array([1, 0, 0], dtype=float)

vetores = np.array([w1, w2, w3])

vet_ort = ortogonalizar(vetores, True)

for i, u in enumerate(vet_ort):
    for j, v in enumerate (vet_ort):
        prod = np.dot(u, v)

        print (f"<u_{i+1}, u_{j+1} > =  {prod}")
        if i == j:
            if not np.allclose(prod, 1):
                print ("\nERRO NA NORMALIZAÇÃO")
        else:
            if not np.allclose(prod, 0):
                print ("\nERRO NA NORMALIZAÇÃO")