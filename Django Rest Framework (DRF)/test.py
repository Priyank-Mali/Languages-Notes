import string
import random

character = string.ascii_letters + string.digits

password = ""

for i in range(8):
    password = password + character[random.randrange(len(character))]

print(password)