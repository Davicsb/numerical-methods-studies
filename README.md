# Métodos Numéricos — 2026.2

Repositório com as resoluções das listas de exercícios da disciplina de
**Métodos Numéricos**, ministrada pelo Prof. Thales Vieira, no Instituto de
Computação da Universidade Federal de Alagoas (UFAL) — curso de Engenharia
de Computação, semestre **2026.2**.

**Dupla:**
- Davi Celestino
- Thiego Macena

## Regras seguidas em todas as implementações

- **Lista 1:** nenhuma biblioteca numérica (ex: `numpy`, `scipy`) utilizada
  nos algoritmos, conforme exigido no enunciado.
- **Lista 2:** `q1.py` e `q3.py ns�io utilizam bibliotecas numéricas. O `q2.py 
 utiliza `numpy apenas para arrays e operaáões vetoriais básicas
  (`np.dot`, `np.outer`), sem recorrer às rotinas prontas de álgebra linear
  (`numpy.linalg`, `scipy`).
- `matplotlib` é usada apenas para gerar gráficos (não realiza cálculo numérico).
- A biblioteca `decimal`, da biblioteca padrão do Python, é usada apenas quando
  a questão exige explicitamente aritmética de precisão controlada.

## Lista 1

- `q1.py`: Implementação do método de Bresenham para traçado de linhas.
- `q2.py`: Implementação do método de Newton para raízes de funções.
- `q3.py`: Implementação do método da bisseção para raízes de funções.
- `q4.py`: Implementação do método de Richardson para extrapolação de Richardson.
- `q5.py`: Implementação do método de Euler para equações diferenciais ordinárias.
- `q6.py`: Implementação do método de Runge-Kutta de 4ª ordem para EDOs.
- `q7.py`: Implementação da regra de Simpson 1/3 para integração numérica.
- `q8.py`: Implementação da regra de Simpson 3/8 para integração numérica.
- `q9.py`: Implementação da quadratura Gaussiana para integração numérica.

## Lista 2

- `q1.py`: Sistema linear via método de Gauss-Jacobi.
- `q2.py`: Sistema linear via método de Gauss-Seidel.
- `q3.py`: Decomposição LU com pivotação parcial.
- `q4.py`: Decomposição Cholesky para matrizes simétricas definidas positivas.

## Lista 3

- `q1.py`: Interpolação de Lagrange para ajuste de curvas.
- `q2.py`: Interpolação de Newton para ajuste de curvas.
- `q3.py`: Ajuste de curvas pelo método dos mínimos quadrados.

## Notas

Cada questão de programação foi implementada em um arquivo `.py` separado conforme
o enunciado do ramo do repositório.
