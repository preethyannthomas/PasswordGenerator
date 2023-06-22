import random
letters =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+']
print("Welcome to Password Generator")
let = input("How many letters you want in your password ? \n")
symb = input("How many symbols you want in your password ? \n")
num = input("How many numbers you want in your password ? \n")
res = ''
for i in range(int(let)):
    res = res + random.choice(letters)
for i in range(int(symb)):
    res = res + random.choice(symbols)
for i in range(int(num)):
    res = res + random.choice(numbers)
res = list(res)
random.shuffle(res)
print(''.join(res))