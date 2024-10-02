# STOx's Planner

STOx's Planner é um algoritmo de planejamento de caminho projetado para ambientes com obstáculos. Ele gera um caminho reto da posição inicial até a posição final e, quando detecta obstáculos, calcula um subobjetivo próximo ao obstáculo para dividir o caminho em subproblemas menores de forma recursiva.

## Como o Algoritmo Funciona

1. **Gera uma linha reta** da posição inicial até a posição final.
2. **Verifica a presença de obstáculos**:
   - Se o caminho intercepta um obstáculo:
     1. Gera um subobjetivo próximo ao obstáculo.
     2. Divide o caminho em dois subproblemas menores.
     3. Repete o processo recursivamente até que o obstáculo seja evitado.

## Características de Desempenho

- **Muito rápido** quando o número de obstáculos é baixo.
- **Pouco flexível** para ambientes complexos com muitos obstáculos.

## Exemplo de Visualização

Abaixo está uma representação visual de como o STOx's Planner funciona:

- **Figura 3**: Caminho sem obstáculos.
- **Figura 4 (a)**: Caminho com um obstáculo. Um subobjetivo é criado para evitar o obstáculo.
- **Figura 4 (b)**: Novos caminhos criados após a adição do subobjetivo.

![Exemplo do STOx's Planner](image.png)

## Benefícios e Limitações

- **Rápido** em ambientes com poucos obstáculos.
- **Não é adequado** para ambientes que exigem um alto nível de flexibilidade ou lidam com obstáculos dinâmicos.

---

Este projeto faz parte de um ambiente de simulação robótica, onde o objetivo é encontrar caminhos eficientes para robôs enquanto evitam obstáculos.
