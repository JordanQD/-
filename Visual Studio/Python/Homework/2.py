'''
二叉树问题
(1)设计一个二叉树类，构造一颗二叉树存储下面的数据;并用宽度优先搜素搜索节点3
(2)改进该二叉树类:让其具有插入元素排序功能，插入元素方法名称为add;且设计一个查找方法find。并设计实验验证编程设计是正确。
'''

class Node:
	#定义结点结构
	def __init__(self, data):
		self.left = None
		self.data = data
		self.right = None
        
    #插入新结点
	def insertTree(self, data):
		#将新结点与父节点比较
		#当父节点非空
		if self.data:	
			#当新结点较小时，将其放在左儿子上
			if data < self.data:
				#当左儿子非空时，使用递归，继续查找左儿子的左儿子
				if self.left:
					self.left.insertTree(data)
				#当左儿子为空时，将结点插入在左儿子上
				else:
					self.left = Node(data)
			#当新结点较大时，将其放在右儿子上
			elif data > self.data:
				#当右儿子非空时，使用递归，继续查找右儿子的右儿子
				if self.right:
					self.right.insertTree(data)
				#当右儿子为空时，将结点插入在右儿子上
				else:
					self.right = Node(data)
			#当结点值相等时，跳过（无data = self.data）
		#当父节点为空
		else:
			self.data = data

	#中序遍历并使用递归：左儿子→父节点→右儿子
	def printTree(self):
		if self.left:
			self.left.printTree()
		print(self.data)
		if self.right:
			self.right.printTree()

	#查找
	def serachTree(self, data):
		#如果结点非空
		if self.data:
			#如果查找值与结点内的值相同，则返回true
			if data == self.data:
				return True
			#如果查找值比结点内小
			elif data < self.data:
				#如果左儿子非空
				if self.left:
					#调用递归，将左儿子设置为头结点，继续查找
					return self.left.serachTree(data)
				#如果左儿子为空，则返回false
				else:
					return False
			#如果查找值比结点内大
			else:
				#如果右儿子非空
				if self.right:
					#调用递归，将右儿子设置为头结点，继续查找
					return self.right.serachTree(data)
				#如果右儿子为空，则返回false
				else:
					return False
		#如果头结点为空，则返回false
		else:
			return False