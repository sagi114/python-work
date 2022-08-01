def get_if_win(size,k):
    [1,k]
    count=0
    while True:
        if size-1-k>0:
            size-=(1+k)
            count+=2
        elif size-1-k==0:
            size-=(1+k)
            count+=2
            break
        else:
            count+=1
            break

    return count

def mynim(l):
    if type(l)!=type([]) or len(l)!=3:
        print("The input is not correct")
        return
    for i in l:
        if type(i)!=type(int()):
            print("The input is not correct")
            return
    n=l[0]
    m=l[1]
    k=l[2]
    b_n=get_if_win(n,k)
    b_m = get_if_win(m, k)
    if (b_n+b_m)%2==1:
        return True
    else:
        return False

if __name__ == '__main__':
    print(mynim([5.7, 5, 3]))  # dani
    print(mynim([5, 5, 3]))  # dani
"""""
if __name__ == '__main__':
    print(mynim([5, 5, 3]))  # dani
    print(mynim([5, 4, 3]))  # dana
    print(mynim([5, 4, 4]))  # dana
    print(mynim([24, 220, 4]))  # dani
    print(mynim([11, 14, 9]))  # dani
    print(mynim([15, 42, 7]))  # dana
    print(mynim([2, 1, 1]))  # dana
    print(mynim([10, 1, 5]))  # dana
    print(mynim([1,4,2]))  # dani
    print('*********')
    print(mynim(8))
    print(mynim([1, 4]))
    """""