class LNode:
    def __init__(self,elem,next_=None):
        self.elem=elem  # 存储当前元素值
        self.next=next_ # 存储下一个对象(的指针)
 
class LStack():     #基于链表技术实现的栈类，用LNode作为节点
    def __init__(self):
        self._top=None   #_top 指向 栈顶元素; 一开始栈顶指向None(也就是栈内无对象)
    def is_empty(self):
        return self._top is None
    def top(self): #获取栈顶元素
        if self.is_empty():
            print('为空栈！')
            return
        return self._top.elem
    def push(self,elem):
        p = LNode(elem,self._top)  #入栈的elem的next应该指向原来的_top(栈顶)
        self._top = p
    def pop(self):
        if self.is_empty():
            print('为空栈！')
            return
        p=self._top
        self._top=self._top.next #把栈顶更新为 出栈前栈顶的next元素(对象)
        return p.elem
if __name__ == '__main__':
    st=LStack()
    for i in range(1,10,2):
        st.push(i)
    while not st.is_empty():
       print(st.pop())