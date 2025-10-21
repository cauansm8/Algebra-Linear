import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# MATRIZES!!!!!!!!!!!!

""" 

COISAS BÁSICAS DE MATRIZ


 """


# (a gente ja tava usando matrizes, mas agr vamos introduzir de fato)

# o primeiro argumento é o shape (linha por coluna)
# shape sempre entre parênteses
zeros = np.zeros((3, 4))

ones = np.ones((3,4))

# matriz cheia de 7
m_full = np.full((3,3), 7)

# matriz aleatoria
m_rand = np.random.rand(3, 4)

# matriz específica (valores já propostos)
m = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# identidade
i = np.eye(4, 4)

# matriz diagonal -> somente os valores na diagonal (o resto é zero)
# 0 -> diagonal principal
# + -> diagonal pra cima
# - -> diagonal pra baixo
d = np.diag([1, 2, 3, 4, 5], -2)

# pega os elementos da diagonal
D_rand = np.diag(m_rand)


# transposta -> .T

m_rand_t = m_rand.T


# reshape -> pega um vetor e transforma em matriz

vetor = np.arange(12)

vetor_reshape = vetor.reshape((3, 4))



""" 
OPERAÇÕES COM MATRIZES


 """

# soma

a = np.random.rand(3, 4)
b = np.random.rand(3, 4)


""" print (f"\n{a + b}")  """


# primeira linha

""" print (m_rand[0, :]) """

# primeira coluna

""" print (m_rand[:,0]) """

# slice

""" print (f"\n{m_rand}")

print (f"\n{m_rand[0, 1: 3]}") """



""" 
OPERAÇÕES COM MATRIZES

 """
    # cos O     - sen O
    # sen O       cos O

# matriz rotação
def matriz_rotacao (angulo, rad = False):
    if not rad:
        angulo = np.deg2rad(angulo)
    
    return np.array([
        [np.cos(angulo) , -np.sin(angulo)],
        [np.sin(angulo), np.cos(angulo)]

    ])

vet = np.array([1,3])
M_rot = matriz_rotacao(90)
vet_rot = M_rot @ vet


# matriz reflexão -> imagine como um espelho da reta
def matriz_reflexao(angulo, rad = False):
    if not rad:
        angulo = np.deg2rad(angulo)
        angulo *= 2

    return np.array([
        [np.cos(angulo) , np.sin(angulo)],
        [np.sin(angulo), -np.cos(angulo)]

    ])

def get_linha_reflexao(angulo, xlim = [-5,5], rad=False):
    if not rad:
        angulo = np.radians(angulo)
    m = np.tan(angulo)
    b = 0
    x = np.array(xlim)
    y = m * x + b
    return x, y

angulo_reflexao = 90
vet = np.array([1, 0])
M_reflexo = matriz_reflexao(angulo_reflexao)
vet_reflexo = M_reflexo @ vet

""" 

EXERCICIO -> fórmula: matriz de projeção

    M(u)_proj @ Vet = proj_u(v)

 """

def proj(u, v):
    return ((np.dot(u,v ) / np.dot(u, u)) * u)

def get_matriz_proj(u):
    proj = np.array([
        [u[0] ** 2, u[0]*u[1]],
        [u[0] * u[1], u[1] ** 2]
    ])

    proj /= np.dot(u, u)

    return proj

# outer é o produto externo (vetorial)

def get_matriz_proj2(u):
    proj = np.outer(u, u) / np.dot(u, u)
    return proj

vetor_u = np.array([1., 2])

vetor_v = np.array([1., 0])

resultado_proj = proj(vetor_u, vetor_v)

matriz_proj = get_matriz_proj2(vetor_u)

print (matriz_proj)













