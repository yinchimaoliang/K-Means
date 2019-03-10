import numpy as np
import matplotlib.pyplot as plt

#确定点的个数
NUMBER = 50
#确定聚类数
K = 3


class Main():
    def getData(self): #生成随机数作为数据集
        self.data = np.random.rand(NUMBER,2)

    def getDist(self,dataA,dataB):#计算距离
         return np.sqrt((dataA[0] - dataB[0]) ** 2 + (dataA[1] - dataB[1]) ** 2)

    def getCenter(self,k):#根据k确定相应聚类
        centers = np.zeros((k,2))

        for i in range(k):
            index = int(np.random.uniform(0, NUMBER))  #在0~NUMBER中生成一个随机数作为索引
            centers[i] = self.data[index]
        return centers

    def KMeans(self,k):
        clusterAssment = np.zeros((NUMBER, 2))  # 用于存放该样本属于哪类及质心距离
        centers = self.getCenter(k)
        flag = 1#是否收敛
        mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
        plt.ion()
        iter_num = 0
        while True:
            flag = 0
            for i in range(NUMBER):#计算最近距离以及最近质心
                minDist = self.getDist(self.data[i],centers[0])
                minIndex = 0
                for j in range(1,k):

                    dist = self.getDist(self.data[i],centers[j])
                    if dist < minDist:
                        minDist = dist
                        minIndex = j

                if clusterAssment[i][0] != minIndex: #如果有变化，则还未收敛
                    flag = 1
                    clusterAssment[i] = minIndex, minDist ** 2
            if not flag:#聚类没有变化时算法收敛，停止迭代
                break
            print("第%d次迭代"%iter_num)
            print("centers")
            print(centers)
            #更新质心
            self.show(clusterAssment,k)
            for j in range(k):
                pointsCluster = []
                #计算每个聚类包括的点
                for m in range(NUMBER):
                    if clusterAssment[m][0] == j:
                        pointsCluster.append([self.data[m][0],self.data[m][1]])
                print("第%d个聚类"%j,end = ":")
                print(pointsCluster)
                #计算每个聚类点的平均坐标
                x_sum = 0
                y_sum = 0
                for i in pointsCluster:
                    x_sum += i[0]
                    y_sum += i[1]
                if len(pointsCluster):
                    centers[j][0] = x_sum / len(pointsCluster)
                    centers[j][1] = y_sum / len(pointsCluster)
            iter_num += 1


        plt.ioff()
        plt.show()
        return centers,clusterAssment


    def show(self,clusterAssment,k):#可视化操作
        mark = ['or', 'ob', 'og', 'ok', 'dr', '+r', 'sr', '^r', '<r', 'pr']
        if k > len(mark):
            print("k值过大，无法显示")
        for i in range(NUMBER):
            plt.plot(self.data[i][0],self.data[i][1],mark[int(clusterAssment[i][0])])
        plt.pause(0.5)


if __name__ == "__main__":
    t = Main()
    t.getData()
    t.KMeans(K)