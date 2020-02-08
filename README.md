# Stock Exchange Challenge

## Objetivo

Calcular a maior diferença entre dois elementos de uma lista, de modo que o minuendo ocorra antes do subtraendo na ordem de iteração da lista.

##  O desafio

O senhor e-Deployer gostaria de comprar uma ação e vendê-la em um curto espaço de tempo, mas apenas se esta operação dê lucro. Para isso, é passado um array K com os valores das ações nos determinados dias, onde ele poderá escolher onde comprar e vender.

Determine o maior lucro dado esse array K de preços.

## Exemplos

#### Exemplo 1:

Input: [7,1,5,3,6,4]

Output: 5

Explicação: Este valor acontece quando compramos a ação no 2o dia e a vendemos no 5o dia (6 - 1)

#### Exemplo 2:

Input: [7,6,4,3,1]

Output: 0

Explicação: Neste caso, não há nenhuma operação que possa ser feita que dê lucro.

## Sobre o desenvolvimento

A solução que primariamente encontrei foi a mais simples. Com duas iterações, seria possível armazenar em uma variável
auxiliar (que chamei de _profit_) a menor diferença, fazendo o cálculo para as combinações entre cada elemento da lista
para com os elementos subsequentes à sua posição.

Porém, várias das combinações são de cálculo desnecessário. Alguns casos:

- Os elementos ocorrem de forma decrescente;
- O menor valor e o maior valor já foram iterados pelo loop, mas ele prossegue até o final.

Por isso, elaborei uma solução alternativa, com o intuito de diminuir as iterações irrelevantes. Usando somente um loop,
é possível identificar o menor valor da lista e sua posição e, com essa informação, identificar o elemento de maior
valor dentre os elementos subsequentes à posição do menor valor. O cálculo dessa forma fica mais diretivo e assertivo.

## Testes

Utilizei a biblioteca _pytest_ na versão 5.3.5 para elaborar inputs e testar outputs de acordo com a minha solução. É
necessário instalá-la, e pode-se utilizar o

`pip install -r requirements`

Lembrando que é boa prática utilizar o ambiente virtual (venv) para cada projeto desenvolvido.

Para executar os testes, digitar no terminal:

`pytest`

Automaticamente, a biblioteca identifica (nos arquivos que comecem ou terminem com "test") as funções com assert e as
executa, exibindo no terminal o resultado.