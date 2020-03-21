def min_number(item):
    max = item[0]


    for i in item:
        if i< max:
            max =i

    return print("the minimum number of the list",max)

a = [1,2,3,4,5,.99,.9999]

min_number(a)