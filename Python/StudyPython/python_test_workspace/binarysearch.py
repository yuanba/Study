def binary_s(seq,num,lower,upper):
    middle = (lower + upper) // 2
    if upper == lower:
        assert num == seq[lower]
        return lower
    else:
        if num > seq[middle]:
            return binary_s(seq,num,middle + 1,upper)
        else:return binary_s(seq,num,lower,middle)

a = [13434,645657,646435436,5464,34,435,5634]
a.sort()
for i in a:
    print(binary_s(a,i,0,6))
