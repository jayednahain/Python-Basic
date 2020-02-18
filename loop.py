num = 3
prime = True

for test in range(2,10):

    if num % test == 0 and num != test:
        print(num , " equals ",test, "*", num/test)
        prime = False

if prime:
    print(num,'is a prime number!')
else:
    print(num,"is not a prime number")        