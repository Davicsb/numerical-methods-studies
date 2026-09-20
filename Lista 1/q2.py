import math
from decimal import Decimal, getcontext

# Contadores globais de operacoes aritmeticas (usados nos itens b e d)
mult_count = 0
add_count = 0

def dmul(x, y):
    """Multiplicacao contabilizada (incrementa mult_count)."""
    global mult_count
    mult_count += 1
    return x * y

def dadd(x, y):
    """Soma contabilizada (incrementa add_count)."""
    global add_count
    add_count += 1
    return x + y

def fatorial_decimal(n):
    return Decimal(math.factorial(n))

def calcular_coeficientes_maclaurin_cos():
    a0 = Decimal(1)
    a1 = -(Decimal(1) / fatorial_decimal(2))
    a2 = (Decimal(1) / fatorial_decimal(4))
    a3 = -(Decimal(1) / fatorial_decimal(6))
    a4 = (Decimal(1) / fatorial_decimal(8))
    return a0, a1, a2, a3, a4

def potencia_direta(x, n):
    if n == 0:
        return Decimal(1)
    resultado = x
    for _ in range(n - 1):
        resultado = dmul(resultado, x)
    return resultado

def avaliar_sem_aninhamento(coefs, x):
    global mult_count, add_count
    mult_count = 0
    add_count = 0

    a0, a1, a2, a3, a4 = coefs

    termo0 = a0
    termo1 = dmul(a1, potencia_direta(x, 2))
    termo2 = dmul(a2, potencia_direta(x, 4))
    termo3 = dmul(a3, potencia_direta(x, 6))
    termo4 = dmul(a4, potencia_direta(x, 8))

    resultado = termo0
    resultado = dadd(resultado, termo1)
    resultado = dadd(resultado, termo2)
    resultado = dadd(resultado, termo3)
    resultado = dadd(resultado, termo4)

    return resultado, mult_count, add_count

def avaliar_aninhada(coefs, x):
    global mult_count, add_count
    mult_count = 0
    add_count = 0

    a0, a1, a2, a3, a4 = coefs

    u = dmul(x, x)  # u = x^2

    acc = a4
    acc = dadd(dmul(acc, u), a3)
    acc = dadd(dmul(acc, u), a2)
    acc = dadd(dmul(acc, u), a1)
    acc = dadd(dmul(acc, u), a0)

    return acc, mult_count, add_count

# Execucao
getcontext().prec = 4  # k = 4 digitos significativos, arredondamento automatico

coefs = calcular_coeficientes_maclaurin_cos()
a0, a1, a2, a3, a4 = coefs
x = Decimal("0.5")

print("RESULTADOS DA QUESTAO 2 (a)")
print(f"a0 = {a0}")
print(f"a1 = {a1}   (coef. de x^2)")
print(f"a2 = {a2}   (coef. de x^4)")
print(f"a3 = {a3}   (coef. de x^6)")
print(f"a4 = {a4}   (coef. de x^8)")
print(f"P8(x) = {a0} + ({a1})*x^2 + ({a2})*x^4 + ({a3})*x^6 + ({a4})*x^8")

print("\nRESULTADOS DA QUESTAO 2 (b)")
cos_direta, mults_direta, adds_direta = avaliar_sem_aninhamento(coefs, x)
print(f"cos(0.5) aproximado (sem aninhamento) = {cos_direta}")
print(f"Multiplicacoes realizadas: {mults_direta}")
print(f"Somas realizadas:          {adds_direta}")

print("\nRESULTADOS DA QUESTAO 2 (c)")
print("Forma aninhada (Horner), com u = x^2:")
print(f"P8(x) = {a0} + u*({a1} + u*({a2} + u*({a3} + u*{a4})))")

print("\nRESULTADOS DA QUESTAO 2 (d)")
cos_aninhada, mults_aninhada, adds_aninhada = avaliar_aninhada(coefs, x)
print(f"cos(0.5) aproximado (forma aninhada) = {cos_aninhada}")
print(f"Multiplicacoes realizadas: {mults_aninhada}")
print(f"Somas realizadas:          {adds_aninhada}")

print("\nRESULTADOS DA QUESTAO 2 (e)")
cos_exato = math.cos(0.5)
erro_direta = abs(Decimal(str(cos_exato)) - cos_direta)
erro_aninhada = abs(Decimal(str(cos_exato)) - cos_aninhada)

print(f"Valor exato (double): {cos_exato}")
print(f"{'Abordagem':<20}{'Aproximacao':<14}{'Erro abs.':<14}{'Mults':<8}{'Somas'}")
print(f"{'Sem aninhamento':<20}{str(cos_direta):<14}{str(erro_direta):<14}{mults_direta:<8}{adds_direta}")
print(f"{'Aninhada (Horner)':<20}{str(cos_aninhada):<14}{str(erro_aninhada):<14}{mults_aninhada:<8}{adds_aninhada}")
print()
print("Conclusao: as duas formas chegam ao mesmo valor aproximado (0.8776),")
print("pois envolvem as mesmas operacoes algebricas reorganizadas. A forma")
print("aninhada usa muito menos multiplicacoes, pois reaproveita a potencia")
print("comum u = x^2 em vez de recalcular cada potencia do zero; o numero")
print("de somas e o mesmo nas duas formas.")