import random
import string

def generate_password(length,uppercase,lowercase,numbers,symbols):
    ch=''
    if uppercase:
        ch += string.ascii_uppercase
    if lowercase:
        ch += string.ascii_lowercase
    if numbers:
        ch += string.digits
    if symbols:
        ch += string.punctuation
    if not ch:
        print('character not found')

    password= ''.join(random.choice(ch) for _ in range(length))
    return password
    

length=int(input("Enter password length: "))
uppercase=input("Include Uppercase yes/no:").lower() == 'yes'
lowercase=input("Include lowercase yes/no:").lower() == 'yes'
numbers=input("Include numbers yes/no:").lower() == 'yes'
symbols=input("Include symbols yes/no:").lower() == 'yes'
final=generate_password(length,uppercase,lowercase,numbers,symbols)
print("generated password: ",final)