Um problema pode ser modelado para um problema de busca se tiver:
    - Um conjunto de possivel estados que o ambiente pode estar, nós chamamos isto de espço de estados
    - Um estado inicial onde o agente começa
    - Um conjunto de um, ou mais, estado alvo
    - Ações disponíveis para o agente
        - ACTIONS(S) = {a1, a2, a3}
    - Um modelo de transição> descreve o que cada ação faz:
        - RESULT(S, a1) = (S')
    - Uma função de custo de ação: dá o custo numerico de aplicar um ação a no estado s para chegar em s'
        - ACTION-COST(s, a, s')

Uma sequencia de ação forama um caminho e a solução é o caminho do estado inicial para o estado alvo.

Uma solução ótima tem o menor custo de caminho entre todas as soluções.

Nós precisamos remover detalhes da representação, i.e, abstrair. Se um agente tiver muito detalhes, o agente, provavelemte, nunca encontrará o caminho ótimo.

## Algorítimos de busca

Um algorítimo de busca pega um problema de busca como input e retorna uma solução, ou uma indicação de falha.

Podemos expandir o nó, considerando as ações disponíveis para o estado, usando o modelo de transição para ver onde essas ações levam e gerar um novo nodo (nodo filho, ou nodo sucessor) para cada um dos estados resultantes.

O conjunto de nodos expandidos: fronteira.
Podemos dizer que cada estado que teve novo nodo gerado foi **alcançado**.


## Estrutura de dados para o nodo

    - node.ESTADO: O estado que o nodo corresponde
    - node.PAI: O nodo' que gero nodo
    - node.ACAO: A ação que foi aplicada ao estado pai para gerar este nodo
    - node.CUSTO_CAMINHO: O custo total do caminho desdo do estado inicial para este nodo

## Estrutura de dados para a fronteira
    
    - lista:
        - fila de prioridade: Best-first
        - fila: Breadth-first
        - pilha: Depth-firts search
    - Na lista pode ser aplicada:
        - IS-EMPTY
        - POP: Remove o nodo do topo, topo definido por algum critério.
        - TOP
        - ADD

### Mensurando a performance de problemas de busca

    - Completude
    - É Otímo
    - Tempo (Complexidade)
    - Espaço (Complexidade)

A complexidade pode ser medida em termos de _d_, o quão fundo, ou o número de ações para a solução ótima, por _m_, o número máximo de ações para qualquer caminho e por _b_, o fator de ramificação, ou o número de sucessores de um nodo que precisa ser considerado.

### Best-first search
Expande um nodo, n, de valor mínimo, valor gerado uma função de avaliação _f()_. A cada iteração, escolhemos um nodo na fronteira com um valor mínimo de _f()_. Antes de expandir, testa se o estado é o estado alvo, caso contrário expande esse nodo. Cado nodo filho é adicionado na fonteira se ele não foi alcançado antes, ou é adicionado novamente se ele é alcançado por um caminho que tem um custo menor do que o que foi encontrado antes.


### Breadth-firts search
Busca em largura
Estratégia apropriada se todas as ações tem o mesmo custo
O nodo raíz é expandido primeiro, então todos os sucessores do nodo raíz são expandidos em sequência, então seus sucessores são expandido e assim vai.

Implementado com uma lista FIFO: novos nodos vão para o fim da fila, nodos antigos, os qual são mais rasos que novos nodos, são expandidos primeiro.

Uma vez encontrado um nodo, que é solução, ele é ótimo. Isto é nós podemos aplicar o _goal test_ cedo, checando se o gerado é a solução. Ele sempre encontra a solução ótima porque, quando é gerado os nodos na profundidade _d_, já foram gerados todos os nodos na profundidade _d - 1_, então se uma solução for encontrada, ela já é a que está na menor profundidade.

    Ele é completo
    ótimo
    Complexidade para tempo e espaço é O(n^2)

Complexidade exponencial para problema de busca não podem ser resolvidadas usando busca uniformes, a não ser que sejam instâncias pequenas.

### Dijkstra's algorithm or busca de custo uniforme

Quando as ações tem custo diferentes, uma escolha óbvia é usar o best-first onde a função de avaliação é o custo do caminho da raiz até o nodo corrente. 


### Depth-first search

Busca em profundidade, sempre expande o nodo mais profundo na fronteira primeiro. **Não mantém a árvore de busca**. A busca em profundidade não é ótima, ela retorna a primeira solução encontrada, mesmo se não é a mais barata. Para um conjunto finito de estados é eficiente e completo. Pode explorar a árvore inteira de busca. A Busca em profundidade é útil porque ela cabe na memória, pois ela não precisa manter todos os estados alcançados, a fronteira é bem pequena.

    Ele é não completo
    Não é ótimo
    Complexidade para tempo: O(b^m) 
    Complexidade para espaço é O(bm)

### Espaço limitado e busca profunda iterativa

Para evitar que a busca em profundidade se desvie por um caminho infinito, podemos usar a busca de profundidade limitada. Uma versão da busca em profundidade na qual delimitamos um _l_, uma profundidade limite, e tratamos todos os nodos até _l_ como se eles não tivessem sucessores. A complexidade de tempo é O(b^l) e a complexidade de espaço é O(bl). Infelizmente, se fizermos uma escolha ruim de _l_, o algorítimo irá falhar em achar uma solução. Tornando-o incompleto.


A busca de profundidade iterativa resolve o problema de pegar um bom valor _l_: ela tenta todos os valores. Ela itera sobre _l_ até que uma solução seja encontrada ou a busca com profundidade limitada retorne o valor de falha em vez do valor de corte. Essa busca une o melhor da busca em largura, com a busca em profundidade. A complexidade de espaço é O(bd), ou O(bm), se a busca varrer a árvore toda. Ela é ótima onde as ações tem a mesmo custo e é completa para espaços finitos e acíclicos. A complexidade de tempo é O(b^d), quando a solução, ou O(b^m), quando não há.


## Estratégias de busca informadas (heurísticas).

h(n) = custo estimado do caminho mias barato do estado no nodo _n_ até o estado alvo.

### Busca gulosa

É uma espécie de best-first search que expande o primeiro nodo com o menor valor de h(n), isto é, o nodo que aparenta estar mais próximo do alvo. A função de avaliação f(n) ficaria:
f(n) = h(n).

h(n) não pode ser computado pela descrição do problema, ele necessica de um certo conhecimento do mundo. O algorítmo guloso tem seus problemas: a solução encontrada pode não ser ótima, visto que, h(n) pode mostrar um valor maior, do que a soma do caminho ótimo e como o algorítimos gulosos não guardam o caminho, então o caminho ótimo pode ser perdido.

### A*

Usa a função de avaliação:
    f(n) = g(n) + h(n)

g(n) é o custo do caminho do estado inicial ao nodo _n_, 
e h(n) é o custo estimado do caminho mais curto do nodo
_n_ até o estado algo.

A* é completo. Se A* é ótimo depende de certas propriedades da
heurística. A chave principal é **admissibilidade**. Uma
heurística admissível é uma que num superestima o custo real 
do alvo. Uma heurística admissível é, portanto, otimista.

Toda heurística consistente é admissível, então com uma 
heurística admissível, A* é ótimo. Além disso, com uma heurística
consistente, a primeira vez que nós encontramos um estado, ele
será ótimo. Com uma heurística inconsistente, não podemos ter
múltiplos caminhos para um mesmo estado e, se cada novo caminho
tem um custo menor que o caminho anterior, então terminaremos
com múltiplos nodos para o nodo da fronteira. Custando para 
nós tempo e espaço.

Com uma heurística não admissível, A* pode (ou não) ser ótimo.

A* expande nós que estão dentro de um contorno de custo, ou seja, 
nós cujo f(n) é menor ou igual a um determinado valor. 
Esses contornos, visualizados como bandas concêntricas, 
permitem que o algoritmo se aproxime gradualmente do objetivo.

Monotonicidade: A A* expande nós de forma monotônica, ou seja, 
o custo nunca diminui ao avançar pelos nós. Isso garante que 
o algoritmo não precise revisar nós já expandidos, tornando-o 
eficiente.

Uma característica essencial da A* é que ela é capaz de podar 
nós desnecessários (eliminando possibilidades sem examiná-las) 
quando uma solução ótima é encontrada, reduzindo o espaço de 
busca.

O algoritmo A*, embora eficiente em termos de expansão de nós, pode consumir muita memória, já que ele precisa armazenar todos os nós abertos. Essa seção explora abordagens que tentam minimizar o uso de memória.

3.1 IDA* (Iterative Deepening A*):
O IDA* combina as vantagens da busca em profundidade iterativa 
com a A*, repetidamente expandindo nós até um limite de 
custo (f) crescente.

Contexto: O IDA* é uma solução para problemas que não cabem 
em memória, como puzzles grandes (por exemplo, o quebra-cabeça
de 8 peças). Ele é útil para problemas onde o espaço é 
mais limitado que o tempo.

3.2 RBFS (Recursive Best-First Search):
O RBFS usa uma estratégia recursiva que limita o uso de 
memória, mantendo apenas o caminho atual em memória e 
usando a melhor alternativa quando o caminho corrente 
não é promissor.

Contexto: O RBFS é mais eficiente que o IDA*, 
mas ainda sofre com a reexpansão de nós, pois esquece boa 
parte das informações sobre o que já foi explorado. Ele é 
adequado para problemas com heurísticas admissíveis e quando 
o espaço de busca é muito grande para ser armazenado.

3.3 SMA* (Simplified Memory-Bounded A*):
O SMA* é uma versão simplificada da A* que usa toda a memória 
disponível. Quando a memória é preenchida, ele descarta o nó 
menos promissor e armazena apenas o melhor caminho para poder 
recriá-lo, se necessário.

Contexto: O SMA* é uma boa escolha para encontrar soluções 
ótimas em problemas grandes, como buscas em grafos ou 
problemas de planejamento, onde a memória é um fator limitante.

4. Algoritmos de Busca com Limitações de Memória:
Beam Search: Explora apenas os k melhores caminhos, 
descartando o resto. Isso torna a busca mais rápida, 
mas potencialmente incompleta.

Busca com Contorno Flexível (Flexible Contour Search): Mantém 
todos os nós cujo custo está dentro de um valor δ do melhor 
nó expandido.
