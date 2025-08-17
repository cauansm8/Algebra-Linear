import numpy as np

dados_economicos = np.array([
    [2.1, 213, 3.2, 11.2],
    [21.4, 331, 2.1, 3.7],
    [14.3, 1439, 2.9, 3.8],
    [3.8, 83, 1.4, 3.2],
    [4.9, 126, 0.5, 2.8],
    [2.6, 67, 1.8, 8.1],
    [2.8, 67, 2.5, 4.1],
    [1.7, 38, 1.9, 5.7]
])

paises = np.array(["Brasil", "EUA", "China", "Alemanha", "Japão", "França", "Reino Unido", "Canadá"])


"""  Compare a semelhanca entre o Brasil e outros paises utilizando a distancia euclidiana entre
 os vetores de caracteristicas (PIB, Populacao, Inflacao, Desemprego). """

    # dist (a b): || a - b ||

distancia_euclidiana = np.zeros((8))

for i in range (dados_economicos.shape[0]):
    soma = 0
    
    for j in range (dados_economicos.shape[1]):
        subtracao = dados_economicos[0][j] - dados_economicos[i][j] 

        soma += subtracao ** 2

    distancia_euclidiana[i] = np.sqrt(soma)



print (f"\n\nDistância euclidiana entre Brasil e outros paises:\n{distancia_euclidiana}")


"""  Faca a padronizacao dos dados utilizando a tecnica de z-score em cada uma das carac-
 teristicas. Apos a padronizacao, compare novamente a semelhanca entre os paises. Explique
 a diferenca nos resultados comparados com o item anterior """

    # X_barra = X -avg(x) 

    # Z_score = X_barra / std(x) -> vetor

dados_padronizados = np.copy(dados_economicos)

for i in range(dados_padronizados.shape[1]): # 3
    soma_da_coluna = 0

    for j in range (dados_padronizados.shape[0]): # 8
        soma_da_coluna += dados_padronizados[j][i]
        
    avg_da_coluna = soma_da_coluna / dados_padronizados.shape[0]

    std_da_coluna = np.std(dados_economicos[:,i])

    for j in range (dados_padronizados.shape[0]):
        dados_padronizados[j][i] = (dados_padronizados[j][i] - avg_da_coluna) / std_da_coluna 


print (f"\n\nDados padronizados com z-score:\n{dados_padronizados}\n\n")

    # outra maneira de ser feita: 
    #   dados_padronizados = (dados_economicos - np.mean(dados_economicos, axis=0)) / np.std(dados_economicos, axis=0) 
                                                    # calcula a media da coluna                 # calcula o desvio padrão da coluna


"""  Compute a matriz de correlacao entre os paises. """

avg_x = np.mean(dados_economicos, axis=0)

# é o X_barra
dados_centrados = dados_economicos - avg_x

# matriz base para os dados -> correlação entre os países
#                           -> mais próximo de 1 = alta correlação
#                           -> mais próximo de -1 = baixa correlação
matriz_correlacao = np.zeros((dados_economicos.shape[0], dados_economicos.shape[0]))

for i in range (matriz_correlacao.shape[0]):
    vi = dados_centrados[i, :]

    for j in range (matriz_correlacao.shape[1]):
        vj = dados_centrados[j, :]

                # distancia entre vetores = aTb / (||a|| * ||b||)
        matriz_correlacao[i][j] = (np.dot(vi, vj)) / (np.linalg.norm(vi) * np.linalg.norm(vj))

        matriz_correlacao[j][i] = matriz_correlacao[i][j]


print (f"\n\nMatriz de correlação:\n{np.round(matriz_correlacao, 5)}")



matriz_correlacao_padronizado = np.zeros((dados_economicos.shape[0], dados_economicos.shape[0]))

for i in range (matriz_correlacao.shape[0]):
    vi = dados_padronizados[i, :]

    for j in range (matriz_correlacao.shape[1]):
        vj = dados_padronizados[j, :]

        matriz_correlacao_padronizado[i][j] = (np.dot(vi, vj)) / (np.linalg.norm(vi) * np.linalg.norm(vj))

        matriz_correlacao_padronizado[j][i] = matriz_correlacao_padronizado[i][j]


print (f"\n\nMatriz de correlação com a padronização z-score:\n{np.round(matriz_correlacao_padronizado, 5)}")



