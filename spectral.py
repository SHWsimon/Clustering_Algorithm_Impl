import numpy as np
import os
import random
import sys
from sklearn.cluster import KMeans
from numpy.random import seed
seed(1)

################### Distance ##################### 
def euclidean_distance(p1, p2):
    return np.sum((p1 - p2)**2)

def euclidDistanceMatrix(x):
    x = np.array(x)
    s = np.zeros((len(x), len(x)))
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            s[i][j] = 1.0 * euclidean_distance(x[i], x[j])
            s[j][i] = s[i][j]
    return s

################### KNN #####################
def knn(S, k, sigma):
    n = len(S)
    a = np.zeros((n, n))

    for i in range(n):
        dist_with_index = sorted(zip(S[i], range(n)), key=lambda x:x[0])
        neighbors = [dist_with_index[m][1] for m in range(k+1)] 
        for j in neighbors: 
            a[i][j] = np.exp(-S[i][j]/2/sigma/sigma)
            a[j][i] = a[i][j] 
    return a

################### Laplacian Matrix #####################
def laplacianMatrix(adjacent_Matrix):
    # Degree Matrix
    degree_Matrix = np.sum(adjacent_Matrix, axis=1)
    # aplacian Matrix: L=D-A
    laplacian_Matrix = np.diag(degree_Matrix) - adjacent_Matrix
    # normailze
    sqrt_Degree_Matrix = np.diag(1.0 / (degree_Matrix ** (0.5)))
    return np.dot(np.dot(sqrt_Degree_Matrix, laplacian_Matrix), sqrt_Degree_Matrix)

################## Main Program ##################
if __name__ == "__main__":
    input_file = str(sys.argv[1])
    k = int(sys.argv[2])
    sigma = float(sys.argv[3])
    output_file = str(sys.argv[4])
    input_data = np.loadtxt(input_file, delimiter=',')
    
    similarity = euclidDistanceMatrix(input_data)
    adjacent = knn(similarity, k, sigma)
    laplacian = laplacianMatrix(adjacent)

    Val, Vec = np.linalg.eig(laplacian)
    Val = zip(Val, range(len(Val)))
    Val = sorted(Val, key=lambda x:x[0])

    h = np.vstack([Vec[:,i] for (v, i) in Val[:500]]).T
    model = KMeans(k).fit(h)
    cluster_label = np.array(model.labels_)

    np.savetxt(output_file, cluster_label)
    print(round(model.inertia_,4))

