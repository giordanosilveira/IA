# Agentes inteligentes

## Agentes e Ambientes
Um agente é qualquer coisa que pode ver, assim como, peceber seu ambiente através **sensores** e agir sobre ele através de **atuadores**. Um ***ambiente*** por sua vez é uma parte do universo que ligamos na hora de desenhar o agente.

Utilizamos o termo **percepção** para se referir ao conteúdo que os sensores do agente estão percebendo. Uma **sequência de percebeção** é a história completa de tudo que o agente já percebeu. Matematicamente falando, um comportamento de um agênte inteligente é descrito pela **função do agente** que mapeia qualquer sequência dada a uma ação. Internamente, a função do agente for um agente artificial será implementada por um **programa do agente.** A função do agente é uma descrição matemática abstrata, a progrma é a implementação concreta, executando dentro de um sistema físico.

Um agente **racional** é o que faz a coisa certo, Mas certo em que perspectiva ? 

Nós obeservamos o comportamento de um agente através das suas consequências, i.e, consequencialismo. Um agente, quando 
é posto num ambiente, deixa uma sequência de ações seguindo suas percepções. Se a sequência é desejável, então o agente
performou bem. Essa noção de desejável é capturada por medidas de desempenho que avaliam qualquer sequência de estados.

Racionalidade -> Para cada sequência de percepção, um agente deve selecionar uma ação que é esperado que maximize suas
medidas de desempenho, dada a evidência fornecida pela sequência de percepções e qualquer conhecimento incorporado que o agente tenha.

## A Natureza de Ambientes

**task environment**: engloba medidas de desempenho, o ambiente e os atuadores e sensores do agente. 

(PEAS): Performance, Enviroment, Actuators, Sensors

Performance (measure): Qualidades dejesadas, por exemplo, para um carro automático poderia ser: Se está indo para o local correto, minimizando consumo de combustível, minimizando tempo e custo de viagem, minimizando violações de trânsitos, maximizando o conforto e segurança do passageiro.

Enviroment: Ambiente onde o agente vai atuar, por exemplo, para um carro automático poderia ser: Qual as ruas, o ambiente é rural, terá muita trágefo de pedestre, pode ter animais silvestres, etc. Quanto mais restrito é o ambiente, mais fácil é desenhar o problema.

Actuators: Como o agente irá atuar com o ambiente, por exemplo, para um carro automático poderia ser: Freios, acelerador, setas, buzina, etc.

Sensors: Como o agente irá receber informações do ambiente, por exemplo, para um carro automático poderia ser: Camêras, velocímetro, GPS, microfones, etc.

### Propriedades das task environment

Totalmente observável x Parcialmente observável: 
Se os sensores de um agente capturam todo o estado do ambiente em cada ponto do tempo, então dizemos que o sistema é totalmente obeservável. Um sistema T.O. é conveniente porque o agente não precisa manter qualquer estado interno para manter seu trajeto interno do mundo. Se um agente não tem sensores, então o ambiente é inobservável.

Single Agent x Multiagent:
Se tem um agente no ambiente é single agente, mais de um multiagente. Se os agente estão um contra o outro, então, além de multiagent, é competitivo, se estão cooperando, então é cooperativo. 

Determinístico x Não determinístico:
Se o próximo estado de um ambiente é completamente determinado pelo estado corrente e a ação executada pelo agente, então nós dizemos que o ambiente é determinístico, caso contrário é não determinístico. A princípio, um agente não precisa se preocupar sobre o incerto em um ambiente T.O e Determinístico. Estocástico é um ambiente que explicitamente lida com probabilidades, um ambiente não determinístico lida também com o incerto, mas não usa probabilidades diretamente.

Episódico x Sequencial: Se a experiência de um agente é dividida em episódios atômicos, isto é, em cada episódio o agente recebe informações e executa uma única informação e, crucialmente, o próximo episódio não depende de ações tomadas previamente, então é Episódido, caso contrário, é Sequencial.

Estático x Dinâmico: Se um ambiente pode mudar enquanto um agente está "pensando", então o ambiente é dinâmico, estático caso contrário. Ambiente estáticos são fáceis de lidar, porque o agente não precisa continuar olhando o mundo enquanto está decidindo uma ação, não é preciso se preocupar com a passagem do tempo. Se um ambiente não muda conforme a passagem do tempo, mas muda por causa do agente, então dizemos que o ambiente é semidinâmico.

Discreto x Contínuo:

Conhecido x não conhecido: Isso diz respeito ao quanto o agente sabe das do ambiente, istó é, ao diz repeito ao quanto o ambiente conhece sobre as "leis da física" daquele local. Em um ambiente conhecido, os resulados para toda ação são dados. Obviamente, se um ambiente é não conhecido, então o agente terá dificultade para apreder como tomar boas decisões.

Figure 2.6

## A estrutura dos agentes


A trabalho da inteligência artificial é desenhar um programa de um agente que implemente as funções do agente, mapeando as percepções para ações. 

Arquitetura de um agente:
agente = arquitetura + programa

Em geral, a arquitetura disponibiliza as percepções dos sensores para o programa, executa o programa e alimenta as escolhas de ação do programa para os atuadores à medida que são geradas.


### Programas dos agentes

Em geral, tem a mesma estrutura, pegar as percepções vindas dos sensores e retornam uma ação para os atuadores