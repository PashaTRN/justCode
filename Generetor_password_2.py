import random
import string

def generate_password(length):
    chars_1 = [i for i in string.ascii_uppercase if i not in 'IO']
    chars_2 = [i for i in string.ascii_lowercase if i not in 'lo']
    chars_3 = list(string.digits[2:])
    result = chars_3 + chars_2 + chars_1
    password = [random.choice(i) for i in (chars_3, chars_2, chars_1)]
    return ''.join(password) + ''.join(random.sample(result, length - 3))

def generate_passwords(count, length):
    return [generate_password(length) for i in range(count)]

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')
