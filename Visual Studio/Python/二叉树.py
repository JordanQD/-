#第一步：创建一个节点类，其中包含左右两个子树与节点的值：
class Node(object):
    def __init__(self,item):
       self.elem=item #创建节点值
       self.left=None #创建左子树
       self.right=None #创建右子树

#第二步：创建一个二叉树类，创建一个根节点：
class Tree(object):
    def __init__(self):#root定义的根节点
       self.root=None

    #在二叉树类中定义一个增加的方法，这里利用的队列来进行二叉树的添加，具体操作是：先把节点放入队列中，然后取出节点，再判断是否有左右子树，没有左右子树就添加左右子树；再取出节点再判断,再增加：
    def add(self,item):
        node=Node(item)#将Node类实例化参数node
        print("adding number:", item)
        if self.root is None:
            self.root=node
            return

        queue=[self.root]#创建一个队列，将根节点放入队列中
        while queue:
            cur_node=queue.pop(0)#向队列queue中取出第一个节点进行判断
            print(cur_node.elem)

            if cur_node.left is None:
                cur_node.left=node  
                print("end left")
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right=node
                print("end right")
                return
            else:
                queue.append(cur_node.right)

'''
使用此二叉树类，调用add方法，把1-10的十个数字加到二叉树中。
同时，修改add方法，输出加入过程中，访问元素的顺序。
创建排序二叉树：左<右，父<子
'''

T = Tree()
for i in range (1, 10):
    T.add(i)