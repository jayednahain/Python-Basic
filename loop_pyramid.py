num = int(input("enter colums number: "))

for column in range (0,num):
    for row in range (0,num-column-1):
        print(end="/")
    for row in range(0,column+1):
        print("*",end=" ")
    print()