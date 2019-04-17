class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self,values=None):
        self.root = None
        if values is not None:
            for value in values:
                self.add(value)

    def add(self,value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            InsertPoint = self.findInsertPoint(self.root,node)
            if node.value > InsertPoint.value:
                InsertPoint.right = node
            if node.value < InsertPoint.value:
                InsertPoint.left = node

    def findInsertPoint(self,p,target):
        '''
        查找插入点。
        :param p:  当前比较节点
        :param target:  待插入节点
        :return:  插入点。如果该值已存在，则返回None
        '''
        ##递归终止条件
        if p.value == target.value:
            return None
        if target.value < p.value and p.left is None:
            return p
        if target.value > p.value and p.right is None:
            return p
        ##递归
        if target.value < p.value:
            return self.findInsertPoint(p.left,target)
        if target.value > p.value:
            return self.findInsertPoint(p.right,target)

    def pprint(self,node):
        '''
        按照前序遍历打印出二叉排序树。
        :return:
        '''
        if node is None:
            return
        print(node.value,end=" ")
        self.pprint(node.left)
        self.pprint(node.right)

    def mprint(self,node):
        '''
        按照中序遍历打印出二叉排序树。
        :return:
        '''
        if node is None:
            return
        self.mprint(node.left)
        print(node.value,end=" ")
        self.mprint(node.right)

    def bprint(self,node):
        '''
        按照后序遍历打印出二叉排序树。
        :return:
        '''
        if node is None:
            return
        self.bprint(node.left)
        self.bprint(node.right)
        print(node.value,end=" ")


tree = Tree([10,5,2,6,15,12,14,13])
print("\n前序遍历")
tree.pprint(tree.root)
print("\n中序遍历")
tree.mprint(tree.root)
print("\n后序遍历")
tree.bprint(tree.root)