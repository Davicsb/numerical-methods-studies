# Métodos Numéricos — 2026.2

Repositório com as resoluções das listas de exercícios da disciplina de
**Métodos Numéricos**, ministrada pelo Prof. Thales Vieira, no Instituto de
Computação da Universidade Federal de Alagoas (UFAL) — curso de Engenharia
de Computação, semestre **2026.2**.

**Dupla:**
- Davi Celestino
- Thiego Macena

## Regras seguidas em todas as implementações

- Nenhuma biblioteca numérica (ex.: `numpy`, `scipy`) é utilizada nos
  algoritmos, conforme exigido no enunciado das listas.
- `matplotlib` é usada apenas para gerar gráficos (não realiza cálculo
  numérico).
- A biblioteca `decimal`, da biblioteca padrão do Python, é usada apenas
  quando a questão exige explicitamente aritmética de precisão controlada.

## Lista 1

Cada questão da lista foi implementada em um arquivo `.py` separado.


## Como rodar

Requer Python 3 e a biblioteca `matplotlib` (usada apenas em questões que pedem plotagem de gráficos):

```bash
pip install matplotlib
```

Cada questão pode ser executada individualmente:

```bash
python3 q1.py
python3 q4.py
python3 q6.py
```

`q4.py` também salva os gráficos gerados como `questao4a_validacao.png` e
`questao4b_bissecao.png` na pasta atual.

## Entrega

A versão final da lista será consolidada em um notebook único (Google
Colab), reunindo as questões pares e ímpares resolvidas por cada integrante
da dupla.