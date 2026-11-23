# Вариант 23: разложение RSA при известной n и phi(n)

import math

n = 44003950675873
phi = 44003936975920

# Так как phi(n) = (p - 1) * (q - 1) = p*q - (p + q) + 1 = n - (p + q) + 1,
# находим сумму корней S = p + q:
s = n - phi + 1

# По теореме Виета p и q — корни квадратного уравнения: x^2 - S*x + n = 0
# Вычисляем дискриминант D = S^2 - 4*n
D = s * s - 4 * n

sqrt_D = math.isqrt(D)

p = (s - sqrt_D) // 2
q = (s + sqrt_D) // 2

print(f"p + q = {s}")
print(f"Дискриминант D = {D}")
print(f"Корень из D = {sqrt_D}")
print(f"p = {p}")
print(f"q = {q}")
print(f"Проверка p * q == n: {p * q == n}")
print(f"Проверка (p - 1) * (q - 1) == phi: {(p - 1) * (q - 1) == phi}")
