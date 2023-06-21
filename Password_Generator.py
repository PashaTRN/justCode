import random
length = int(input())    # длина пароля
password = ''
for _ in range(length):
    num = random.randint(0, 1)
    if num == 1:
        password += chr(random.randrange(65, 91))
    else:
        password += chr(random.randrange(97, 123))
print(password)