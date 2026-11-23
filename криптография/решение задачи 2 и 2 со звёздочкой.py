
# Бинарный метод возведения в степень по модулю: (base ^ exp) mod mod
def binary_pow(base, exp, mod):
    result = 1
    current = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * current) % mod
        current = (current * current) % mod
        exp = exp // 2
    return result


# Проверка числа на простоту (малая теорема Ферма: a^(p-1) mod p == 1)
def is_prime(num):
    for a in [2, 3, 5, 7, 11]:
        if binary_pow(a, num - 1, num) != 1:
            return False
    return True


# Алгоритм Евклида (прямой ход) + расширенный алгоритм Евклида (обратный ход)
def euclid_find_d(e, phi):
    a = phi
    b = e
    quotients = []   
    remainders = []  

    while b != 0:
        q_step = a // b
        r_step = a % b
        quotients.append(q_step)
        remainders.append(r_step)
        a = b
        b = r_step

    nod = a

    # Обратный ход: поднимаемся по цепочке частных снизу вверх
    quotients.reverse()
    x = 1
    y = 0
    for q_step in quotients:
        new_x = y
        new_y = x - y * q_step
        x = new_x
        y = new_y

    # y — коэффициент при e (если он получился отрицательным, прибавляем phi)
    d = y
    if d < 0:
        d = d + phi

    return nod, d, remainders


p = 11777623253100600606475568688692467522395803125194264009546341998455853099782265804864870878594598047222934141798969832793441585484966407147720677990883619
q = 12353978300203236372526910502422393557961726275268960264014521143951779860477853396347304933752339630927134439217791364721884908085632288618105974588440853


print("=== ЗАДАЧА 2 ===")

# Шаг 1. Проверяем, что p и q — простые числа
print("Шаг 1. p простое?", is_prime(p), "| q простое?", is_prime(q))

# Шаг 2. Перевод первых 3 букв фамилии в числа (по условию задачи № 2: A=1 ... Z=26)
surname = "Titeev"
letters = surname[:3].upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = []
for letter in letters:
    num = alphabet.index(letter) + 1
    numbers.append(num)

print("Шаг 2. Буквы:", letters, "-> числа:", numbers)

# Шаг 3. Вычисляем n = p * q
n = p * q
print("Шаг 3. n =", n)

# Шаг 4. Вычисляем функцию Эйлера phi(n) = (p - 1) * (q - 1)
phi = (p - 1) * (q - 1)
print("Шаг 4. phi(n) =", phi)

# Вариант 23 
e = 1093

# Шаги 5 и 6. Проверяем НОД(e, phi) = 1 и находим d расширенным алгоритмом Евклида
nod, d, remainders = euclid_find_d(e, phi)
print("Шаг 5. Остатки алгоритма Евклида:", remainders)
print("Шаг 5. НОД(e, phi) =", nod)
print("Шаг 6. d =", d)
print("Шаг 6. Проверка (e * d) mod phi =", (e * d) % phi)

# Шаг 7. Шифрование бинарным методом: y = x^e mod n
print("Шаг 7. Двоичная запись e:", bin(e)[2:])
encrypted = []
for x in numbers:
    y = binary_pow(x, e, n)
    encrypted.append(y)

print("Зашифрованные блоки:")
for y in encrypted:
    print(y)

# Шаг 8. Расшифрование бинарным методом: x = y^d mod n
decrypted_numbers = []
decrypted_letters = ""
for y in encrypted:
    x = binary_pow(y, d, n)
    decrypted_numbers.append(x)
    decrypted_letters = decrypted_letters + alphabet[x - 1]

print("Шаг 8. Расшифрованные числа:", decrypted_numbers)
print("Шаг 8. Расшифрованные буквы:", decrypted_letters)


print()
print("=== ЗАДАЧА 2* ===")

# Для задачи 2* дано e2 = 65537 и шифртекст c_star
e2 = 65537
c_star = 81015468774710401505474764674969768278417928970834057943570541085234267868314775151235181936031448986691652369851452089887330392867425916431157456795147262310603424969615240368918929590094963618483076685198719367972860240941926955385496123791675474888261237326703066483355807000466632692892249587481421002849

# Шаги 5 и 6 для e2 = 65537
nod2, d2, remainders2 = euclid_find_d(e2, phi)
print("Остатки алгоритма Евклида:", remainders2)
print("НОД(e2, phi) =", nod2)
print("Закрытый ключ d2 =", d2)
print("Проверка (e2 * d2) mod phi =", (e2 * d2) % phi)

# Шаг 8. Расшифрование шифртекста c_star бинарным методом
m_star = binary_pow(c_star, d2, n)
print("Расшифрованное число (ответ):", m_star)
