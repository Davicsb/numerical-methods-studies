def questao_um(binary_str):
    # Remove espaços em branco
    binary_str = binary_str.replace(" ", "")
    
    # Extração dos campos
    s_bit = binary_str[0]
    e_bits = binary_str[1:12]
    f_bits = binary_str[12:]
    
    # 1Sinal
    s = int(s_bit)
    sign = -1 if s == 1 else 1
    
    # Expoente (conversão binário para decimal)
    e = 0
    for bit in e_bits:
        e = e * 2 + int(bit)
        
    actual_exponent = e - 1023
    
    # Mantissa / Fração (conversão fração binária para decimal)
    fraction_value = 0.0
    base = 0.5
    for bit in f_bits:
        if bit == '1':
            fraction_value += base
        base /= 2.0
        
    mantissa_value = 1.0 + fraction_value
    
    # Cálculo da potência de 2
    pow_2 = 1.0
    if actual_exponent >= 0:
        for _ in range(actual_exponent):
            pow_2 *= 2.0
    else:
        for _ in range(-actual_exponent):
            pow_2 /= 2.0
            
    # Valor decimal final
    decimal_value = sign * mantissa_value * pow_2
    
    return {
        "sinal": s_bit,
        "expoente_bits": e_bits,
        "expoente_decimal": e,
        "expoente_ajustado": actual_exponent,
        "mantissa_bits": f_bits,
        "valor_mantissa": mantissa_value,
        "valor_decimal": decimal_value
    }

# Execução
bin_a = "0 10000000101 0110100100000000000000000000000000000000000000000000"
bin_b = "1 10000000101 0110100100000000000000000000000000000000000000000000"
bin_c = "0 10000000000 0011010100000000000000000000000000000000000000000000"
bin_d = "0 10000000000 0011010100000000000000000000000000000000000000000001"

print("RESULTADOS DA QUESTÃO 1 (a)")
resultadoa = questao_um(bin_a)
print(f"Sinal (s): {resultadoa['sinal']}")
print(f"Expoente (bits): {resultadoa['expoente_bits']} -> Decimal: {resultadoa['expoente_decimal']} (Ajustado: {resultado['expoente_ajustado']})")
print(f"Mantissa (f): {resultadoa['mantissa_bits'][:12]}...")
print(f"Forma: (-1)^{resultadoa['sinal']} * (1.f)_2 * 2^{resultadoa['expoente_ajustado']}")
print(f"Valor Decimal Final: {resultadoa['valor_decimal']}")

print("RESULTADOS DA QUESTÃO 1 (b)")
resultadob = questao_um(bin_b)
print(f"Sinal (s): {resultadob['sinal']}")
print(f"Expoente (bits): {resultadob['expoente_bits']} -> Decimal: {resultadob['expoente_decimal']} (Ajustado: {resultado['expoente_ajustado']})")
print(f"Mantissa (f): {resultadob['mantissa_bits'][:12]}...")
print(f"Forma: (-1)^{resultadob['sinal']} * (1.f)_2 * 2^{resultadob['expoente_ajustado']}")
print(f"Valor Decimal Final: {resultadob['valor_decimal']}")

print("RESULTADOS DA QUESTÃO 1 (c)")
resultadoc = questao_um(bin_c)
print(f"Sinal (s): {resultadoc['sinal']}")
print(f"Expoente (bits): {resultadoc['expoente_bits']} -> Decimal: {resultadoc['expoente_decimal']} (Ajustado: {resultado['expoente_ajustado']})")
print(f"Mantissa (f): {resultadoc['mantissa_bits'][:12]}...")
print(f"Forma: (-1)^{resultadoc['sinal']} * (1.f)_2 * 2^{resultadoc['expoente_ajustado']}")
print(f"Valor Decimal Final: {resultadoc['valor_decimal']}")

print("RESULTADOS DA QUESTÃO 1 (d)")
resultadod = questao_um(bin_d)
print(f"Sinal (s): {resultadod['sinal']}")
print(f"Expoente (bits): {resultadod['expoente_bits']} -> Decimal: {resultadod['expoente_decimal']} (Ajustado: {resultado['expoente_ajustado']})")
print(f"Mantissa (f): {resultadod['mantissa_bits'][:12]}...")
print(f"Forma: (-1)^{resultadod['sinal']} * (1.f)_2 * 2^{resultadod['expoente_ajustado']}")
print(f"Valor Decimal Final: {resultadod['valor_decimal']}")