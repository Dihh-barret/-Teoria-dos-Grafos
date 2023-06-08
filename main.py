import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import heapq


adjacency_matrix_a = np.array([[0, 1, 1, 1, 1, 0],
                              [1, 0, 0, 0, 0, 1],
                              [1, 0, 0, 0, 0, 1],
                              [1, 0, 0, 0, 0, 1],
                              [1, 0, 0, 0, 0, 1],
                              [0, 1, 1, 1, 1, 0]
])

adjacency_matrix_b = np.array([[0, 0, 0, 1, 1, 0],
                              [0, 0, 0, 1, 1, 1],
                              [0, 0, 0, 0, 1, 1],
                              [1, 1, 0, 0, 1, 0],
                              [1, 1, 1, 1, 0, 1],
                              [0, 1, 1, 0, 0, 0]])

adjacency_matrix_c = np.array([[0, 1, 1, 1, 1, 0],
                              [1, 0, 1, 1, 0, 1],
                              [1, 1, 0, 0, 1, 1],
                              [1, 1, 0, 0, 1, 1],
                              [1, 0, 1, 1, 0, 1],
                              [0, 1, 1, 1, 1, 0]])
#Matriz D
adjacency_matrix_d = np.array([
    [0, 3, 5, 0, 8, 1, 0, 0],
    [3, 0, 2, 0, 0, 0, 1, 0],
    [5, 2, 0, 1, 0, 0, 0, 2],
    [0, 0, 1, 0, 4, 0, 0, 0],
    [5, 0, 0, 4, 0, 6, 0, 1],
    [1, 0, 0, 0, 6, 0, 5, 0],
    [0, 1, 0, 0, 0, 5, 0, 1],
    [0, 0, 2, 0, 1, 0, 1, 0]
])

def matriz_alcancabilidade(adjacency_matrix):
    reachability_matrices = []
    reachability_matrix = adjacency_matrix.copy()
    reachability_matrices.append(reachability_matrix.astype(int))
    n = adjacency_matrix.shape[0]

    for _ in range(n-1):
        reachability_matrix = np.logical_or(reachability_matrix, np.dot(reachability_matrix, adjacency_matrix))
        reachability_matrices.append(reachability_matrix.astype(int))

    return reachability_matrices

def matriz_acessibilidade(adjacency_matrix):
    n = adjacency_matrix.shape[0]
    accessibility_matrices = []
    accessibility_matrix = adjacency_matrix.copy()
    accessibility_matrices.append(accessibility_matrix.astype(int))

    for k in range(n):
        accessibility_matrix = np.logical_or(accessibility_matrix, np.linalg.matrix_power(adjacency_matrix, k+1))
        accessibility_matrices.append(accessibility_matrix.astype(int))

    return accessibility_matrices

def tem_caminho_euler(adjacency_matrix):
    degrees = np.sum(adjacency_matrix, axis=1)
    if np.all(degrees % 2 == 0):
        return True
    else:
        return False

def caminho_minimo(adjacency_matrix, start_node, end_node):
    n = adjacency_matrix.shape[0]
    distance = np.full((n, n), float("inf"))
    path = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] > 0:
                distance[i][j] = adjacency_matrix[i][j]
                path[i].append(j)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i] = path[i][:path[i].index(k)+1] + path[k] + path[j][path[j].index(k):]

    if distance[start_node][end_node] == float("inf"):
        return None, None

    vertices_in_path = [start_node]
    current_node = start_node
    while current_node != end_node:
        current_node = path[current_node][-1]
        vertices_in_path.append(current_node)

    return distance[start_node][end_node], vertices_in_path

def dijkstra(adjacency_matrix, start_node):
    n = adjacency_matrix.shape[0]
    distance = np.full(n, float("inf"))
    distance[start_node] = 0
    visited = [False] * n
    heap = [(0, start_node)]
    path = [[] for _ in range(n)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if visited[current_node]:
            continue

        visited[current_node] = True

        for neighbor in range(n):
            weight = adjacency_matrix[current_node][neighbor]
            if weight > 0:
                new_dist = current_dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    path[neighbor] = path[current_node] + [current_node]
                    heapq.heappush(heap, (new_dist, neighbor))

    return distance, path
  
def exibir_grafo(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix)
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

while True:
    # Exibindo o menu
    print("Escolha uma opção:")
    print("1. Matriz de alcançabilidade")
    print("2. Matriz de acessibilidade")
    print("3. Verificar caminho de Euler")
    print("4. Caminho mínimo entre dois nós")
    print("0. Sair")
    opcao = int(input("Opção: "))

    if opcao == 0:
        break

    # Selecionando a matriz
    print("Escolha uma matriz:")
    print("1. Matriz A")
    print("2. Matriz B")
    print("3. Matriz C")
    print("4. Matriz D")
    matriz_opcao = int(input("Matriz: "))

    if matriz_opcao == 1:
        adjacency_matrix = adjacency_matrix_a
    elif matriz_opcao == 2:
        adjacency_matrix = adjacency_matrix_b
    elif matriz_opcao == 3:
        adjacency_matrix = adjacency_matrix_c
    elif matriz_opcao == 4:
        adjacency_matrix = adjacency_matrix_d
    else:
        print("Opção de matriz inválida.")
        continue

    if opcao == 1:
        # Matriz de alcançabilidade
        reachability_matrices = matriz_alcancabilidade(adjacency_matrix)
        print("Matrizes de Alcançabilidade:")
        for i, matrix in enumerate(reachability_matrices):
            print(f"Passo {i + 1}:")
            print(matrix)
            print()

        reachability_matrix = reachability_matrices[-1]
        print("Matriz de Alcançabilidade Final:")
        print(reachability_matrix)

        exibir_grafo(adjacency_matrix)

    elif opcao == 2:
        # Matriz de acessibilidade
        accessibility_matrices = matriz_acessibilidade(adjacency_matrix)
        print("Matrizes de Acessibilidade:")
        for i, matrix in enumerate(accessibility_matrices):
            print(f"Passo {i + 1}:")
            print(matrix)
            print()

        reachability_matrix = matriz_alcancabilidade(adjacency_matrix)[-1]
        print("Matriz de Alcançabilidade:")
        print(reachability_matrix)

        exibir_grafo(adjacency_matrix)

    elif opcao == 3:
        # Verificar caminho de Euler
        has_euler_path = tem_caminho_euler(adjacency_matrix)

        if has_euler_path:
            print("O grafo possui um caminho de Euler.")
        else:
            print("O grafo não possui um caminho de Euler.")

        exibir_grafo(adjacency_matrix)

    elif opcao == 4:
    # Caminho mínimo entre dois nós
      start_node = int(input("Digite o nó inicial: "))
      end_node = int(input("Digite o nó final: "))
  
      distance, path = dijkstra(adjacency_matrix, start_node)
  
      if distance[end_node] == float("inf"):
          print("Não existe caminho entre os nós.")
      else:
          print(f"Distância mínima: {distance[end_node]}")
          print("Caminho:")
          print(path[end_node] + [end_node])
  
    exibir_grafo(adjacency_matrix)
