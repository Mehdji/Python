input_list = [9,5,23,0,99] 

def swap_value(a ,b):


    a = a + b
    b = a - b
    a = a - b
    return a,b

for i in input_list:
    for j in input_list:
        if i > j:
            swap_value(i,j)
            print(j,i) 
        else:
            pass
print(input_list)
