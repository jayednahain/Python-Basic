def char_frequency(value):
    dict={}
    for n in value:
        keys = dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n] = 1
    return print("the frequency is: ",dict)

a="www.google.com"

char_frequency(a)
