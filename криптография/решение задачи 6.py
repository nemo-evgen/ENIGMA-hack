# Вариант 23: взлом RSA с малым модулем n

n = 190019041
e = 257
c = 54492007


# 1. Разложение числа n на два простых множителя перебором делителей
def factorize(num):
    d = 2
    while d * d <= num:
        if num % d == 0:
            return d, num // d
        d += 1
    return None, None


# 2. Поиск обратного элемента d = e^(-1) mod phi (расширенный алгоритм Евклида)
def mod_inverse(e, phi):
    old_r, r = e, phi
    old_s, s = 1, 0

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s

    # Делаем d положительным по модулю phi
    return old_s % phi


# 3. Перевод расшифрованного числа в текст (по 2 цифры на ASCII-код)
def number_to_text(m):
    s = str(m)
    text = ""
    for i in range(0, len(s), 2):
        code = int(s[i:i + 2])
        text += chr(code)
    return text


p, q = factorize(n)
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)

# Расшифрование: m = c^d mod n
m = pow(c, d, n)
plaintext = number_to_text(m)

print(f"p = {p}")
print(f"q = {q}")
print(f"Проверка: p * q = {p * q}")
print(f"phi(n) = {phi}")
print(f"d = {d}")
print(f"Проверка: (e * d) % phi = {(e * d) % phi}")
print(f"Расшифрованное число m = {m}")
print(f"Открытый текст: {plaintext}")

# 4. Оценка времени перебора делителей для 1024-битного n
# В худшем случае (p ≈ q ≈ sqrt(n)) нужно проверить делители до sqrt(2^1024) = 2^512
divisions = 2 ** 512
speed_per_sec = 10 ** 9
seconds_in_year = 365 * 24 * 60 * 60

years = divisions / (speed_per_sec * seconds_in_year)
print(f"\nОценка для 1024-битного n:")
print(f"Количество делений (до 2^512): {divisions:.3e}")
print(f"Время перебора: {years:.3e} лет")
