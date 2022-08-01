def copy_arr(arr_to_copy):
    arr=[]
    for i in arr_to_copy:
        arr.append(i)
    return arr
def findallindex(l):
    if type(l)!=type([])or len(l)!=2:
        return
    list_e=l[0]
    element=l[1]
    arr=[]

    def reckrsia(item,index=0,array=[]):
        if(type(item)!=type([])and item!=element):
            return
        tmp=copy_arr(array)
        tmp.append(index)
        if item==element:
            arr.append(tmp)
            return
        if type(item)==type([]):
            for a in range(len(item)):
                reckrsia(item[a],a,tmp)
    reckrsia(list_e)
    for i in arr:
        i.pop(0)
    return arr
#get index of the num 2
#[[[1, 2, 3, [0, 1, 2]], 2, [1, 3]], [1, 2, 3]]
#will return [[0, 0, 1], [0, 0, 3, 2], [0, 1], [1, 1]]
"""""
if __name__ == '__main__':
    listExample = [[[1, 2, 3, [0, 1, 2]], 2, [1, 3]], [1, 2, 3]]
    elmentExample = 2
    a=findallindex([listExample, elmentExample])
    print(a)
"""""