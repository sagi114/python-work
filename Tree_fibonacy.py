class Node:
    #all parameter of node in tree
    def __init__(self,childhood,maturity,oldness,day=1,hight=0):
        self.hight=hight
        self.day=day
        self.childhood=childhood
        self.maturity=maturity
        self.oldness=oldness
        self.right=None
        self.left=None
        self.start_childhood=1
        self.start_maturity=childhood+1
        self.start_old=self.start_maturity+maturity
        self.end_life=self.start_old+oldness
    def add_a_new_generation(self):
        if self.right==None:
            if self.day>=self.start_childhood and self.day<self.start_maturity:
                self.right=Node(self.childhood,self.maturity,self.oldness,self.day+1,self.hight+1)
            if self.day==0 or self.day>=self.start_old and self.day<self.end_life:
                self.right = Node(self.childhood, self.maturity, self.oldness, self.day + 1,self.hight+1)
            elif self.day>=self.start_maturity and self.day<self.start_old:
                self.right = Node(self.childhood, self.maturity, self.oldness, self.day + 1,self.hight+1)
                self.left = Node(self.childhood, self.maturity, self.oldness,1,self.hight+1)
        else:
            self.right.add_a_new_generation()
            if self.left != None:
                self.left.add_a_new_generation()
        self.day+=1
    def recorsia_func(self,n):
        right=0
        left=0
        if n==self.hight:
            return 1
        if self.right!=None:
            right=self.right.recorsia_func(n)
        if self.left!=None:
            left=self.left.recorsia_func(n)
        return right+left
    def get_alive_rabbits(self,n):
        if n==0:
            return 0
        return self.recorsia_func(n)
def Alive(l):
    try:
        tree_node=Node(l[1],l[2],l[3],0)
        for i in range(l[0]+1):
            tree_node.add_a_new_generation()
        return tree_node.get_alive_rabbits(l[0])
    except Exception:
        print('The input is not correct')
        pass
#"""""
if __name__ == '__main__':
    print(Alive([10,1,5,1]))
    print(Alive([0, 1, 5, 1]))
    #"""""









