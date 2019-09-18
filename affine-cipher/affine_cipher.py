from fractions import gcd

def coprime(a, b):
    return gcd(a, b) == 1

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
          'u', 'v', 'w', 'x', 'y', 'z']

m = len(letters)
lttr2num = {}

for i in range(m):
    lttr2num[letters[i]] = i

def encode(plain_text, a, b):
    if not coprime(a, m):
        raise ValueError("Error: a and m must be coprime.")
    result = ""
    for lttr in plain_text:
        if lttr not in letters:
            raise ValueError("Your string contains {}, which is not in the alphabet")
        x = lttr2num[lttr]
        result = "".join([result, letters[(a*x+b) % m]])
    return result


def decode(ciphered_text, a, b):
    if not coprime(a, m):
        raise ValueError("Error: a and m must be coprime.")
    result = ""
    for lttr in ciphered_text:
        if lttr not in letters:
            raise ValueError("Your string contains {}, which is not in the alphabet")
        y = lttr2num[lttr]
        x = modInverse(a, m)
        result = "".join([result, letters[x*(y-b) % m]])
    return result


print(encode("test", 5, 7))
print(decode("kqlfdjzvgytpaeticdhmrtwlykqlonubstx", 19, 13))