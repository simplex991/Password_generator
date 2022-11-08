import secrets
import string
import sys

LETTERS = string.ascii_letters #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 
NUMBERS = string.digits #0123456789
SYMBOLS = string.punctuation #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

def main():
    pwd = ''
    pwd_length = sys.argv[1]
    stuff = LETTERS + NUMBERS + SYMBOLS
    for i in range(int(pwd_length)):
        pwd += ''.join(secrets.choice(stuff))
    
    print(pwd)
    
    
if __name__ == '__main__':
    main()