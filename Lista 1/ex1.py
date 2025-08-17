import numpy as np

R = 6367.5

def calcular_x(latitude, longitude):
    return R * np.cos(np.radians(longitude)) * np.sin(np.radians(latitude))

def calcular_y(latitude, longitude):
    return R * np.cos(np.radians(longitude)) * np.cos(np.radians(latitude))

def calcular_z(longitude):
    return R * np.sin(np.radians(longitude))



coordenadas = np.array([
    [-23.5505, -46.6333],
    [40.7128, -74.0060],
    [35.6895, 139.6917],
    [-33.8688, 151.2093],
    [51.5074, -0.1278]
])

"""  Faca uma funcao que receba as coordenadas e retorne o vetor posicao correspondente. Teste
 nas seguintes cidades: """

posicao_correspondente = np.zeros((5, 3))


for i in range (5):
        
        j = 0

        posicao_correspondente[i][j] = calcular_x (coordenadas[i][0], coordenadas[i][1])

        j += 1

        posicao_correspondente[i][j] = calcular_y(coordenadas[i][0], coordenadas[i][1])

        j += 1

        posicao_correspondente[i][j] = calcular_z (coordenadas[i][1])


print (f"\n\nPosições de cada cidade: \n{posicao_correspondente}")



"""  Calcule as distancias euclidianas em 3D entre Sao Paulo e as outras cidades utilizando o
 vetor posicao. """

    # distância euclidiana = || a - b ||

distancias_euclidiana = np.zeros((5))

for i in range(5):
    subtracao = posicao_correspondente[0] - posicao_correspondente[i]
     
    soma = 0

    for j in range (3):
         
        soma += subtracao[j] ** 2 

    distancias_euclidiana[i] = np.sqrt(soma)



print (f"\n\nDistância entre as cidades:\n{distancias_euclidiana}")


"""  Faca uma funcao que calcule a distancia na superficie da Terra entre dois pontos dadas
 suas coordenadas. Utilize a formula d(a, b) = R∠(a, b) e teste no mesmo caso do exercicio
 anterior """


    # arcos θ (aT * b)            * R
    #            / ||a|| * ||b||

distancias_superficie = np.zeros((5))

for i in range(5):
    
    a = np.array((posicao_correspondente[0][0], posicao_correspondente[0][1], posicao_correspondente[0][2]))
    
    b = np.array((posicao_correspondente[i][0], posicao_correspondente[i][1], posicao_correspondente[i][2]))

    aTb = 0

    for j in range(3):
         
        aTb += a[j] * b[j]

    distancias_superficie[i] = np.arccos(aTb / (np.linalg.norm(a) * np.linalg.norm(b))) * R

print (f"\n\nDistância na superfície da Terra entre as cidades:\n{distancias_superficie}")