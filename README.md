# Métodos Numéricos — 2026.2

Repositório com as resoluções das listas de exercícios da disciplina de
**Métodos Numéricos**, ministrada pelo Prof. Thales Vieira, no Instituto de
Computação da Universidade Federal de Alagoas (UFAL) — curso de Engenharia
de Computação, semestre **2026.2**.

**Dupla:**
- Davi Celestino
- Thiego Macena

## Regras seguidas em todas as implementações

- **Lista 1:** nenhuma biblioteca numérica (ex.: `numpy`, `scipy`) é utilizada
  nos algoritmos, conforme exigido no enunciado.
- **Lista 2:** `q1.py` e `q3.py` não utilizam bibliotecas numéricas. O `q2.py`
  utiliza `numpy` apenas para arrays e operações vetoriais básicas
  (`np.dot`, `np.outer`), sem recorrer a rotinas prontas de álgebra linear
  (`numpy.linalg`, `scipy`).
- `matplotlib` é usada apenas para gerar gráficos (não realiza cálculo
  numérico).
- A biblioteca `decimal`, da biblioteca padrão do Python, é usada apenas
  quando a questão exige explicitamente aritmética de precisão controlada.

## Lista 1 e 2

Cada questão de programação foi implementada em um arquivo `.py` separado
(`qN.py`). As questões puramente teóricas (como a Questão 4 da Lista 2) são
resolvidas por escrito em arquivos pdf.

## Como rodar

Requer Python 3 e a biblioteca `matplotlib` (usada apenas em questões que
pedem plotagem de gráficos). O `q2.py` da Lista 2 também requer `numpy`:

```bash
pip install matplotlib numpy
```

Cada questão pode ser executada individualmente, dentro da pasta da lista
correspondente:

```bash
python3 qN.py
```

(por exemplo, `python3 q3.py` na pasta `Lista 2`).

Arquivos de imagem gerados ao rodar:
- Lista 1: `q4.py` salva `questao4a_validacao.png` e `questao4b_bissecao.png`.
- Lista 2: `q2.py` salva `comparacao_6_curvas.png` e `q3.py` salva
  `questao3c_placa.png`.

## Entrega

A versão final de cada lista é consolidada em um notebook único (Google
Colab), reunindo as questões resolvidas por cada integrante da dupla. Os
notebooks das Listas 1 e 2 (`Lista1_MetodosNumericos.ipynb` e `Lista2_MetodosNumericos.ipynb`) estão na raiz do
repositório.