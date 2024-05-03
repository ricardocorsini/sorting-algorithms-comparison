# Empirical comparison of sorting algorithms

## Algorithms implemented and analyzed

- **Bubble Sort**: Compara cada par de elementos adjacentes e os troca se estiverem na ordem errada. É repetido até que nenhum elemento precise ser trocado, indicando que a lista está ordenada.

- **Selection Sort**: Divide a lista em uma sublista ordenada e outra não ordenada. Continuamente remove o menor elemento da parte não ordenada e o adiciona ao final da parte ordenada.

- **Insertion Sort**: Constrói a lista final de elementos ordenados um item por vez, encontrando o local apropriado para cada elemento e inserindo-o ali.

- **Merge Sort**: Divide o array em duas metades, ordena cada metade recursivamente e depois mescla as duas metades ordenadas de volta em uma única lista ordenada.

- **Quick Sort**: Escolhe um elemento como pivô (mediana entre o primeiro, o meio e o último elemento do segmento do array que está sendo considerado) e particiona os demais elementos em dois subconjuntos, os que são menores que o pivô e os que são maiores, para então ordenar os subconjuntos.

- **Heap Sort**: Transforma a lista em um heap binário, de modo que o maior elemento seja movido para a base do heap. O elemento é então removido do heap e colocado na posição correta na lista.

- **Radix Sort**: Processa cada dígito dos números, da unidade até o dígito mais significativo, usando algum outro algoritmo de ordenação estável ou um sistema de filas.

## Métodos para criação dos inputs 

- **totally_random(n)**: Gera uma lista aleatória com n números

- **descending_order(n)**: Gera uma lista com n valores ordenados de forma decrescente

- **partially_sorted(n, disorder_percentage)**: Gera uma lista parcialmente ordenada. A porcentagem de valores desordenados é o parâmetro disorder_percentage, que vai de 0 a 100

