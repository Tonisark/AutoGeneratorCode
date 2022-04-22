#v1.01
import string
import random

letters = string.ascii_letters
digits = string.digits
#Symbols = string.punctuation
chars = letters + digits #+ Symbols 
min_length = 8
max_length = 16
password = "".join(random.choice(chars)
for x in range(random.randint(min_length,max_length)))
print(password)
input()

