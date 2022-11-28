from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# 生成（150,2）的数据集
centers = [[1, 1], [-1, -1], [1, 1]]
#centers = [[1, 1,0], [-1, -1,1], [1, 1,-1]]

Xn, labels_true = make_blobs(n_samples=150, centers=centers, cluster_std=0.5, random_state=0)
# 在图上画出数据
#plt.scatter(Xn[:, 0], Xn[:, 1], s=80)
if Xn.shape[1]==2:
    plt.scatter(Xn[:, 0], Xn[:, 1], c = 'r', marker = '^') 
else:
    ax = plt.figure().add_subplot(111, projection = '3d')
    #基于ax变量绘制三维图
    #xs表示x方向的变量
    #ys表示y方向的变量
    #zs表示z方向的变量，这三个方向上的变量都可以用list的形式表示
    #m表示点的形式，o是圆形的点，^是三角形（marker)
    #c表示颜色（color for short）
    ax.scatter(Xn[:, 0], Xn[:, 1], Xn[:, 2], c = 'r', marker = '^') #点为红色三角形

    #设置坐标轴
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')


plt.show()

# KMeans聚类
model = KMeans(n_clusters=3)
y_pred = model.fit_predict(Xn)
print(type(y_pred))
print(y_pred)
print(y_pred.shape)
print(y_pred.size)