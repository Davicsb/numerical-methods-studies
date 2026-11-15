# Questão 3 - Lista 3 - Métodos Numéricos
# I(t) = exp(-t^2) * sin(t^3): amostragem, derivada numérica e integral numérica

# ---------- a) amostragem do sinal ----------
import sympy as sp
import matplotlib.pyplot as plt


def amostrar(expr_str, a, b, n):
    """Recebe a string de I(t), o intervalo [a, b] e n amostras.
    Retorna as listas t e I(t), com n pontos igualmente espaçados."""
    t_sym = sp.Symbol("t")
    expr = sp.sympify(expr_str)
    h = (b - a) / (n - 1)
    t = [a + i * h for i in range(n)]
    I = [float(expr.subs(t_sym, ti)) for ti in t]
    return t, I


EXPR = "exp(-t**2)*sin(t**3)"

t200, I200 = amostrar(EXPR, 0.0, 3.0, 200)
plt.figure(figsize=(8, 4))
plt.plot(t200, I200)
plt.xlabel("t (s)")
plt.ylabel("I(t) (A)")
plt.title("Corrente I(t) = exp(-t²)·sin(t³), n = 200")
plt.grid(True)
plt.show()


# ---------- b) derivada por diferenças de 3 pontos ----------
def derivada_3pontos(t, I):
    """Diferenças de 3 pontos em malha uniforme:
    interior -> centrada;  extremos -> unilaterais de 3 pontos."""
    n = len(t)
    h = t[1] - t[0]
    d = [0.0] * n
    d[0] = (-3 * I[0] + 4 * I[1] - I[2]) / (2 * h)
    for i in range(1, n - 1):
        d[i] = (I[i + 1] - I[i - 1]) / (2 * h)
    d[n - 1] = (3 * I[n - 1] - 4 * I[n - 2] + I[n - 3]) / (2 * h)
    return d


t15, I15 = amostrar(EXPR, 0.0, 3.0, 15)
dI15 = derivada_3pontos(t15, I15)

print(f"{'i':>2} {'t':>8} {'I(t)':>10} {'dI/dt':>10}")
for i in range(15):
    print(f"{i:2d} {t15[i]:8.4f} {I15[i]:10.6f} {dI15[i]:10.6f}")

i_max = max(range(15), key=lambda i: dI15[i])
print(f"\nMaior taxa de crescimento (n=15): dI/dt = {dI15[i_max]:.6f} A/s em t = {t15[i_max]:.4f} s")

plt.figure(figsize=(8, 4))
plt.plot(t15, I15, "o-", label="I(t)")
plt.plot(t15, dI15, "s-", label="dI/dt")
plt.axvline(t15[i_max], color="gray", linestyle="--", label=f"t_max ≈ {t15[i_max]:.3f} s")
plt.xlabel("t (s)")
plt.title("I(t) e dI/dt (diferenças de 3 pontos, n = 15)")
plt.legend()
plt.grid(True)
plt.show()

# conferência com malhas mais finas
for n_ref in (101, 1001):
    tr, Ir = amostrar(EXPR, 0.0, 3.0, n_ref)
    dr = derivada_3pontos(tr, Ir)
    im = max(range(n_ref), key=lambda i: dr[i])
    print(f"Conferência n={n_ref}: t_max = {tr[im]:.4f} s, dI/dt = {dr[im]:.4f} A/s")


# ---------- c) integral por Simpson composta ----------
def simpson_composta(expr_str, a, b, n):
    """Simpson composta com n subintervalos (n par)."""
    if n % 2 != 0:
        raise ValueError("n deve ser par")
    t, I = amostrar(expr_str, a, b, n + 1)
    h = (b - a) / n
    soma = I[0] + I[n]
    for j in range(1, n):
        soma += (4 if j % 2 == 1 else 2) * I[j]
    return h / 3 * soma


ns = list(range(2, 51, 2))
Qs = [simpson_composta(EXPR, 0.0, 3.0, n) for n in ns]

print(f"{'n':>3} {'Q (C)':>14}")
for n, q in zip(ns, Qs):
    print(f"{n:3d} {q:14.10f}")
print(f"\nQ (n = 50) = {Qs[-1]:.8f} C")

plt.figure(figsize=(8, 4))
plt.plot(ns, Qs, "o-")
plt.xlabel("n (subintervalos)")
plt.ylabel("Q (C)")
plt.title("Carga Q em função de n (Simpson composta)")
plt.grid(True)
plt.show()