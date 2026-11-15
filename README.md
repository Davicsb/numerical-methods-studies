# Numerical Methods — 2026.2

Repository with the solutions to the exercise lists for the **Numerical Methods** course, taught by Prof. Thales Vieira, at the Institute of Computing, Federal University of Alagoas (UFAL), Computer Engineering course, 2026.2 semester.

**Team:**
- Davi Celestino
- Thiego Macena

---

## Rules Followed in All Implementations

- **List 1:** No numerical library (e.g., `numpy`, `scipy`) used in the algorithms, as required by the assignment.
- **List 2:** `q1.py` and `q3.py` do not use numerical libraries. `q2.py` uses `numpy` only for arrays and basic vector operations (`np.dot`, `np.outer`), without relying on ready-made linear algebra routines (`numpy.linalg`, `scipy`).
- `matplotlib` is used only for generating graphs (does not perform numerical calculation).
- The `decimal` library, from the Python standard library, is used only when the question explicitly requires controlled precision arithmetic.

---

## List 1 and 2

Each programming question was implemented in a separate `.py` file (`qN.py`). Purely theoretical questions (with Q4 from List 2) are solved in writing in PDF files.

---

## List 3

List 3 programming questions were implemented in separate `.py` files (`qN.py`) in the `Lista 3/ folder, following the same rules as previous lists: no numerical library ( numpy`, `scipy`) used in the algorithms. `matplotlib` Ã© usad only for generating graphs (does not perform numerical calculation).
---

## How to Run

Requires Python 3 and the `matplotlib` library (used only in questions that request graph plotting). List 2's `q2.py also requires `numpy`:

```bash
pip install matplotlib numpy
```

Each question can be executed individually, inside the corresponding list folder:

```bash
python3 qN.py
```

(Example: `python3 q3.py ` in the `Lista 2 folder`).

Generated image files when running:
- **List 1:** `q4.py` saves `questao4a_validadao.png`) and `questao4b_bissecao.png`.
- **List 2*: `q2.py` saves `comparacao_6_curvas.png` and `q3.py  saves `questao3c_place.png.
- **List 3:** ((images not yet generated))

---

## Delivery

The final version of each list is consolidated in a single notebook (Google Colab), gathering the questions solved by each team member. The notebooks for List 1 and List 2 (`Lista1_°�TodosNmnÃ©ricos.ipynb and `Lista1_°�TodosNuméricos.ipynb`) are in the repository branch.
