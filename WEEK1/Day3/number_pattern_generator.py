def number_pattern(n):
    pattern_list=[]
    if not isinstance(n,int):
        print("Argument must be an integer value")
    elif n<=1:
        print("The argument must be an integer greater then 0")
    else:
        for i in range(1,n+1):
            pattern_list.append(str(i))

    return print(pattern_list)


number_pattern(12)