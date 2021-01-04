import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

#reading in data from excel
dataset = pd.read_csv('training.csv')
trainingDataSet= []
for i in range(0,4339):
	trainingDataSet.append([(dataset.values[i,j]) for j in range(1, 6)])

#------------------------------------Question 1------------------------------------
#Compute the SSE for each iteration 

#List of Sum of Squared Errors
SSE = []
resultClustering = []
#First Run of KMeans Algorithm and store the result
kmeans = KMeans( n_init = 1, max_iter = 1, n_clusters = 10, init = 'random', random_state = 0)
kmeans.fit(trainingDataSet)
#appending it to the list for the first cluster to the resultClustering list
resultClustering.append(kmeans.cluster_centers_)
#appending the first SSE to the SSE list
SSE.append( kmeans.inertia_ )

#compute the above code once again using the result from  first iteration and passed in as selected cluster
for index in range(2,101):
	#computing the KMeans Clustering for the rest of 99 times
	kmeans = KMeans(init = resultClustering[index-2] ,n_init = 1, max_iter = 1, n_clusters = 10, random_state=0)
	#Fitting the trainDataSet
	kmeans.fit(trainingDataSet)
	#appending it to the resultClustering list
	resultClustering.append( kmeans.cluster_centers_ )
	#appending it to the SSE list
	SSE.append( kmeans.inertia_ )
#KMEANS converge at iteration = 27
x = []
for i in range(1,101):
	x.append(i)
#Marking the convergence K-iteration
plt.plot(x[26],SSE[26], color = 'red', marker = "X")
#Plot the Graph of K-Iteration vs SSE
plt.plot(x,SSE, linewidth=1)
plt.xlabel('Iteration-K')
plt.ylabel('Sum of Squared Errors (SSE)')
plt.title('Correltation of Sum of Squared Errors and Iteration-K')
plt.show()

#------------------------------------Question 2------------------------------------
#Computing the SSE for each value of K_cluster and return the list and the minimum SSE in each run
#of selecting different centroid seeds
def SSEComputation(k_cluster):
	listSSE= []
	for index in range(1,11):
		kmeans = KMeans( n_init = 1, max_iter = 100, n_clusters = k_cluster)
		kmeans.fit(trainingDataSet)
		listSSE.append(kmeans.inertia_)
	#returning the list of SSE after each run and the minimum SSE among this list	
	return listSSE, min(listSSE)
#Computing for various clusters k: 2, 5, 10, 20	
K2ClusterList, K2min = SSEComputation(2)
#output the entire list for K=2
print("------------------Cluster K = 2------------------")
print(K2ClusterList)
print(K2min)
K5ClusterList, K5min = SSEComputation(5)
#output the entire list for K=5
print("------------------Cluster K = 5------------------")
print(K5ClusterList)
print(K5min)
K10ClusterList, K10min = SSEComputation(10)
#output the entire list for K=10
print("------------------Cluster K = 10------------------")
print(K10ClusterList)
K20ClusterList, K20min = SSEComputation(20)
#output the entire list for K=20
print("------------------Cluster K = 20------------------")
print(K20ClusterList)

X = [ 2, 5, 10, 20]
Y = [ K2min, K5min, K10min, K20min]
#ploting the curve for SSE and various K-Cluster
plt.plot(X,Y, linewidth=1, color ='red')
plt.xlabel('K-Cluster')
plt.ylabel('Sum of Squared Errors (SSE)')
plt.title('Correltation of Sum of Squared Errors For Various K-Cluster', pad = 20)
plt.show()

#------------------------------------Question 3------------------------------------
#Write into file for computing in Excel later
def writeFile(classLabels, filename):
	file = open(filename+".txt", "a")
	for label in classLabels:
		file.write(str(label))
		file.write("\n")
	file.close()

#Cluster 10
kmeans = KMeans( n_init = 10, max_iter = 100, n_clusters = 10).fit(trainingDataSet)
#writing into files
writeFile(kmeans.labels_, "Cluster10")

#Cluster 20
kmeans = KMeans( n_init = 10, max_iter = 100, n_clusters = 20).fit(trainingDataSet)
#writing into files
writeFile(kmeans.labels_, "Cluster20")

#Cluster 30
kmeans = KMeans( n_init = 10, max_iter = 100, n_clusters = 30).fit(trainingDataSet)
#writing into files
writeFile(kmeans.labels_, "Cluster30")

#Cluster 30
kmeans = KMeans( n_init = 10, max_iter = 100, n_clusters = 50).fit(trainingDataSet)
#writing into files
writeFile(kmeans.labels_, "Cluster50")
