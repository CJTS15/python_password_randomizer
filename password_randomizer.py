import random
import string

print('Welcome To Password Randomizer!')

#initializing password length
length = int(input('Enter the length of the password: '))

#initializing data
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#adding all data
combine = lowerCase + upperCase + num + symbols

#randomizing all data
temp = random.sample(combine, length)

password = "".join(temp)

#result
print(password)