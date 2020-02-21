sum =  0 ;
add = 10;

for x in range(1,add):
    print("this is the current sum ",sum)
    print("how much woul you like to add next ?  ",end=" ")
    direct_add= input("type 0 to exit the progaram")
    add =int(direct_add)
    sum = sum + add
    x= 1
    if add == 0:
        break


