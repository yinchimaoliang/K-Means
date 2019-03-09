import numpy as np
import matplotlib.pyplot as plt


NUMBER = 10






class Main():
    def getData(self): #生成随机数作为数据集
        self.data = [[1.1,1.1],[1.2,1.2],[1.2,1.3],[1.0,1.6],[1.7,0.9],[101,101],[102,102],[103,103],[104,104],[105,105]]
        # self.data = np.random.rand(NUMBER,2) * 10
        # print(self.data)

    def getDist(self,dataA,dataB):#计算距离
         return np.sqrt((dataA[0] - dataB[0]) ** 2 + (dataA[1] - dataB[1]) ** 2)
        # return 1
    def getCenter(self,k):#根据k确定相应聚类
        centers = np.zeros((k,2))
        # print("centers")

        for i in range(k):
            index = int(np.random.uniform(0, NUMBER))  #在0~NUMBER中生成一个随机数作为索引
            centers[i] = self.data[index]
        # print(centers)
        return centers

    def KMeans(self,k):
        clusterAssment = np.zeros((NUMBER, 2))  # 用于存放该样本属于哪类及质心距离
        # print(clusterAssment)
        centers = self.getCenter(k)
        # print(centers)
        flag = 1#是否收敛
        while flag:
            flag = 0
            for i in range(NUMBER):#计算最近距离以及最近质心
                minDist = self.getDist(self.data[i],centers[0])
                minIndex = 0
                for j in range(1,k):

                    dist = self.getDist(self.data[i],centers[j])
                    # print(self.data[i], centers[j],dist)
                    if dist < minDist:
                        minDist = dist
                        minIndex = j

                if clusterAssment[i][0] != minIndex: #如果有变化，则还未收敛
                    # print(clusterAssment[i][0],minIndex)
                    flag = 1
                    clusterAssment[i] = minIndex, minDist ** 2

        # print(clusterAssment)
            #更新质心
            for j in range(k):
                pointsCluster = []
                for m in range(NUMBER):
                    # print(clusterAssment[k][0])
                    if clusterAssment[m][0] == j:
                        pointsCluster.append([self.data[m][0],self.data[m][1]])
                x_sum = 0
                y_sum = 0
                for i in pointsCluster:
                    x_sum += i[0]
                    y_sum += i[1]
                # x = sum(pointsCluster[:,0]) / NUMBER
                # y = sum(pointsCluster[:,1]) / NUMBER
                if len(pointsCluster):
                    centers[j][0] = x_sum / len(pointsCluster)
                    centers[j][1] = y_sum / len(pointsCluster)
                # print(centers[j],"sdfsdf")
                # print(pointsCluster)
                # print(pointsCluster)

            print("centers")
            print(centers)
        return centers,clusterAssment





if __name__ == "__main__":
    t = Main()
    t.getData()
    t.KMeans(2)