def sum_dig_pow(a, b):
    sum_list = []
    for x in range (a, b+1):
        c = list(str(x))
        d = int(c[0])
        for i in range(2, len(c)+1):
            d += int(c[i-1])**i
        if d == x:
            sum_list.append(x)
    return sum_list
