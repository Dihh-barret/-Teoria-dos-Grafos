# -Teoria-dos-Grafos
Use seus conhecimentos em programação para explicar como podemos usar a Linguagem Python
para trabalhar com Grafos. Vocês devem fazer uma relação entre os conceitos visto em sala de aula 
com a aplicação em Python: exemplo: Vocês devem também usar o conceito de Matriz (biblioteca 
numpy) de Adjacência para implementar os algoritmos para determinar a matriz de alcançabilidade 
(Operação Booleana ou das matrizes A2
, ..., An e o algoritmo de Warshal).

Problemas a serem Implementados:
Para os Exercícios 1 a 4, escreva um programa de computador em Python no Google Colab que 
dê a resposta desejada a partir dos dados de entrada indicados. 

1. Dados de entrada: Matriz de adjacência A de um grafo direcionado. 
Resposta: Matriz de alcançabilidade R do grafo, calculada pela fórmula R = A ∨ A(2) ∨ ... ∨
A(n) . O programa deve mostrar cada matriz separadamente e por fim a matriz de 
alcançabilidade.

2. Dados de entrada: Matriz de adjacência A de um grafo direcionado. 
Resposta: Matriz de acessibilidade R do grafo, calculada pelo algoritmo de Warshall. O 
programa deve mostrar cada matriz separadamente e por fim a matriz de alcançabilidade.

3. Dados de entrada: Matriz de adjacência A de um grafo. 
Resposta: Mensagem indicando se o grafo tem um caminho de Euler. 

4. Dados de entrada: Matriz de adjacência A de um grafo simples com peso ou de um grafo 
direcionado e dois nós no grafo. 
Resposta: Distância correspondente ao caminho mínimo entre os dois nós ou uma 
mensagem de que não existe nenhum caminho; os vértices no caminho mínimo, se existir. 
(Sugestão: Você vai precisar encontrar uma maneira de denotar quais os vértices que 
pertencem, atualmente, a IN.) 

Grafos para criar as Matrizes Pré-cadastradas para serem usadas como testes:
![image](https://github.com/Dihh-barret/-Teoria-dos-Grafos/assets/66051980/f09ee012-3365-491a-96bc-f1a519ebf513)


Informações Importantes:

(i) No início do programa deve ser criado um menu com as opções de escolhas entre os 4 exercícios;

(ii) Ao entrar no exercício deve haver a opção de escolher a matriz desejada;

(iii) Deve-se usar a biblioteca Python networkX para mostrar os grafos;
