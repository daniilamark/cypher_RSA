# алфавит шифрования
alphabet_e = {'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07', 'h': '08',
              'i': '09', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16',
              'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24',
              'y': '25', 'z': '26', ' ': '27', 'а': '28', 'б': '29', 'в': '30', 'г': '31', 'д': '32',
              'е': '33', 'ё': '34', 'ж': '35', 'з': '36', 'и': '37', 'й': '38', 'к': '39', 'л': '40',
              'м': '41', 'н': '42', 'о': '43', 'п': '44', 'р': '45', 'с': '46', 'т': '47', 'у': '48',
              'ф': '49', 'х': '50', 'ц': '51', 'ч': '52', 'ш': '53', 'щ': '54', 'ъ': '55', 'ы': '56',
              'ь': '57', 'э': '58', 'ю': '59', 'я': '60', ',': '61', '.': '62', '!': '63', '?': '64',
              '0': '65', '1': '66', '2': '67', '3': '68', '4': '69', '5': '70', '6': '71', '7': '72',
              '8': '73', '9': '74', ';': '75', ':': '76', '\"': '77', '\'': '78', '-': '79', '_': '80',
              '=': '81', '+': '82', '(': '83', ')': '84', '&"': '85', '%': '86', '$': '87', '#': '88',
              '№': '89', '@': '90', '`': '91', '{': '92', '}': '93', '[': '94', ']': '95', '*': '96'}


# алфавит дешифрования
alphabet_d = {n: c for c, n in alphabet_e.items()}


# Евклидовый алгоритм. Нахождение GCD двух чисел
def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)


# Генерация ключей шифрования, E и D
def generate_keys(p, q):
    # публичный ключ
    global e, d
    n = p * q

    # приватный ключ
    N0 = (p - 1) * (q - 1)

    # E - первое целое число относительно простого к N0
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break

    # D - мультипликативная обратная e % n0
    for i in range(0, N0):
        if ((e * i) % N0) == 1:
            d = i
            break

    return n, e, d


# шифрование символа
def encrypt(char, N, e):
    return str((int(char) ** e) % N).zfill(2)


# дешифрование символа
def decrypt(char, N, d):
    return str((int(char) ** d) % N).zfill(2)


# Разделение слова на символы
def split(word):
    return [char for char in word]


# Шифрование сообщения
def encrypt_message(msg, N, e):
    plaintext = msg.lower().split()
    encrypted = []

    for word in plaintext:
        # Разделение слова на символы
        chars = split(word)

        # Создание списка зашифрованных символов
        encrypted_chars = [encrypt(alphabet_e[char], N, e) for char in chars]

        # Добавление зашифрованного слова в список
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)

    # Добавление к зашифрованным словам пробелов
    encrypted = f" {encrypt(alphabet_e[' '], N, e)} ".join(encrypted)

    return encrypted


# дешифрование
def decrypt_message(msg, N, d):
    # сообщения
    encrypted = msg.split()
    decrypted = []
    plaintext = []

    for char in encrypted:
        decrypted.append(decrypt(char, N, d))

    # Сообщение расшифровки
    for char in decrypted:
        plaintext.append(alphabet_d[char])

    plaintext = "".join(plaintext)

    return plaintext
