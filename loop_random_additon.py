sum = 0

add = None


while add != 0:  
    print('the current sum is',sum)
    print("How much wold you lik e to add? ",end='')
    raw_add = input('(type 0 to end the program) =  ')
    add = int(raw_add)
    sum = sum+add
