# class Node(object):
#     """
#     节点类
#     """
#     # construct function
#     def __init__(self, value=None, next=None):
#         # public protected private
#         self.value = value
#         self.next = next
#         # %f %s
#         # print("hello %d" %self.value)
#     def __repr__(self):
#         return str(self.value)



# # def ddddddddddd(head):
# #     head
# #     a = head
# #     b = head

# #     for i in range(k):
# #         a = a.next

# #     while a.next is not None:
# #         a = a.next
# #         b = b.next

# #     return b


# if __name__ == '__main__':
#     apple = Node()
#     print(apple.value)
#     apple.value = 100
#     print(apple.value)




# class chain():
#     def __init__(self):
#         self._head = None
#         self.length = 0

#####数据结构书
class LNode():
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

# list1 = LNode(1)
# p = list1
# for i in range(2,11):
#     p.next = LNode(i)
#     p = p.next
# p = list1
# while p is not None:
#     print(p.elem)
#     p = p.next


###定义异常
class linkedListUnderflow(ValueError):
    pass

##定义链表类对象
# class LList():
#     def __init__(self):
#         self._head = None

#     def isempty(self):
#         return self._head==None

#     def prepend(self,item):
#         self._head=LNode(item,self._head)

#     def pop(self):
#         if self._head is None:
#             raise linkedlistunderflow('in pop')
#         e = self._head.elem
#         self._head = self._head.next
#         return e
#     def __repr__(self):
#         if self.isempty():
#             print('the chain table is empty')
#             return
#         nlist = ''
#         node = self._head
#         while node:
#             nlist = nlist + str(node.elem) + ' '
#             node = node.next
#         return nlist
#     # def printall(self):
#     #     p = self._head
#     #     while p is not None: 
#     #         print(p.elem,end ='')
#     #         if p.next is not None:
#     #             print(', ',end = '')
#     #         p = p.next
#     #     print(' ')

# s = LList()
# s.prepend(3)
# s.prepend(2)
# s.prepend(1)
# print(s)
# s.pop()
# s.pop()
# # s.pop()#?????
# print(s)



'''
###循环单链表
class LCList():
    def __init__(self):
        self._rear = None
    def is_empty(self):
        return self._rear is None
    def prepend(self,elem):
        p = LNode(elem)
        if self._rear==None:
            p.next = p
            self._rear=p
        else:
            p.next = self._rear.next
            self._rear.next = p
    def append(self,elem):#尾端加入
        self.prepend(elem)
        self._rear = self._rear.next
    def pop(self):#前端弹出
        if self._rear==None:
            raise linkedListUnderflow("in pop of LCList")
        p = self._rear.next
        if self._rear ==p:
            self._rear=None
        else:
            self._rear.next=p.next
        return p.elem
    def pop_last(self):
        if self._rear==None:
            raise linkedListUnderflow("in pop_last of LCList")
        p = self._rear.next
        if self._rear ==p:
            self._rear=None
        else:
            while True:                
                if p.next==self._rear:
                    e = self._rear.elem
                    p.next=self._rear.next
                    self._rear=p
                    return e
                p = p.next

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p == self._rear:
                break
            p = p.next

lcl = LCList()
for i in range(10):
    lcl.prepend(i)
lcl.printall()
lcl.pop()
lcl.printall()
lcl.append(20)
lcl.printall()
lcl.prepend(230)
lcl.printall()
lcl.pop_last()
lcl.printall()
lcl.pop_last()
lcl.printall()
'''


###双链表
class DLNode(LNode):
    def __init__(self,elem,prev=None,next_=None):
        LNode.__init__(self,elem,next_)
        self.prev=prev

class DLList():
    def __init__(self):
        self._head=None
        self._rear=None

    def prepend(self,elem):
        p = DLNode(elem,None,self._head)
        if self._head ==None:
            self._rear=p
        else:
            p.next.prev=p
            #self._head.prev=p
        self._head=p


    def append(self,elem):
        p = DLNode(elem,self._rear,None)
        if self._head == None:
            self._head=p
        else:
            p.prev.next=p
        self._rear=p
    def pop(self):
        if self._head==None:
            raise linkedListUnderflow("in pop of LCList")
        e = self._head.elem
        self._head=self._head.next
        if self._head is not None:
            self._head.prev=None
        return e

    def pop_last(self):
        if self._head==None:
            raise linkedListUnderflow("in pop of LCList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear==None:
            self._head=None
        else:
            self._rear.next=None
        return e
    def printall(self):
        if self._head ==None:
            return
        e = self._head
        while True:
            print(e.elem)
            if e.next==None:
                break
            e=e.next

dd = DLList()
for i in range(10):
    dd.prepend(i)
dd.printall()
dd.append(10)
dd.printall()











