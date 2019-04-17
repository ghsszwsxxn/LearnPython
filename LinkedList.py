class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def head_insert(self, value):
        node = ListNode(value)
        node.next = self.head
        self.head = node

    def tail_insert(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
        else:
            if self.tail is None:
                t = self.head
                while t.next:
                    t = t.next
                self.tail = t
            self.tail.next = node
            self.tail = node

    def print(self):
        p = self.head
        while p:
            print(p.val, end=" ")
            p = p.next
        print("")

    def get_value(self, n):
        p = self.head
        t = 1
        while t < n:
            if p.next is not None:
                p = p.next
                t = t + 1
            else:
                return None
        return p

    def get_node(self, value):
        p = self.head
        while p is not None:
            if p.val == value:
                return p
            else:
                p = p.next
        return None

    def insert(self, index, value):
        '''
        1. 找到第index-1个节点
        2. 创建新的节点
        3. 插入
        :param index:
        :param value:
        :return:
        '''
        node = ListNode(value)
        if index == 1:
            self.head_insert(value)
        else:
            pre = self.get_value(index - 1)
            if pre is not None:
                node.next = pre.next
                pre.next = node
            else:
                raise Exception("插入位置超出链表长度")

    def delete(self, index):
        if self.head is None:
            return
        if index == 1:
            self.head = self.head.next
            return
        pre = self.get_value(index - 1)
        if pre is None:
            return
        node = pre.next
        if node is None:
            return
        pre.next = node.next


link = LinkedList()
link.head_insert(3)
link.head_insert(2)
link.head_insert(1)
link.tail_insert(4)
link.tail_insert(5)
link.tail_insert(6)

link.insert(3, 7)
link.delete(4)
link.print()
