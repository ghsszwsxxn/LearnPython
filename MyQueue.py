# class Queue:
#     def __init__(self):
#         self.length = 5
#         self.data = [0] * self.length  ##初始化长度为10，每个值为0的数组
#         self.front = 0
#         self.rear = 0
#         self.t = 0
#
#     def empty(self):
#         return self.front == self.rear
#
#     def full(self):
#         return (self.rear + 1) % self.length == self.front
#
#     def put(self, value):
#         if self.full():
#             return
#         self.data[self.rear] = value
#         self.rear = (self.rear + 1) % self.length
#
#     def pop(self):
#         if self.empty():
#             return None
#         value = self.data[self.front]
#         self.front = (self.front + 1) % self.length
#         return value
#
#     def size(self):
#         if self.front <= self.rear:
#             return self.rear - self.front
#         if self.front > self.rear:
#             return self.length - self.front + self.rear
#
#     def print_all(self):
#         self.__print(self.front)
#
#     def __print(self, t):
#         if t == self.rear:
#             return
#         else:
#             print(self.data[t], end=" ")
#             t = (t + 1) % self.length
#             self.__print(t)
#
#
# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.print_all()
# print("")
# q.pop()
# q.put(5)
# q.print_all()
