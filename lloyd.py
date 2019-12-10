
import sys
from random import sample,seed
seed(1)
import numpy as np 
from math import inf
from collections import Counter

################### Distance ##################### 
def dist(p1,p2):
    distamce = 0
    if len(p1)==len(p2):
        for i in range(len(p1)):
           distamce += (p1[i]-p2[i])**2
        return distamce

# lloyd method : get the inital center points
def initial(data, k):
    return sorted(sample(data.tolist(), k))

################### Clustering ##################### 
def clustering(data, initial_points):
    cluster_labels = []
    for i in range(len(data)):
        point_1 = data[i]
        dis = inf
        label = None
        for j in range(len(initial_points)):
            point_2 = initial_points[j]
            distance = dist(point_2, point_1)
            if distance<dis:
                dis = distance
                cluster_label = j
        cluster_labels.append(cluster_label)
    return cluster_labels

def recenter(data, centroids):
    centers = {}
    centers_new = []
    counter = Counter(centroids)

    # accumulate clustered points
    for i in range(len(data)):
        point = data[i].copy()
        if centroids[i] not in centers:
            centers[centroids[i]]=point
        else:
            centers[centroids[i]]+=point
    
    # sort the new center 
    for i in centers:
        new_center = centers[i]/counter[i]
        centers_new.append(new_center.tolist())
    return sorted(centers_new)  

################### SSE ##################### 
def sse(data, labels):
    centers = recenter(data, labels)
    sse_error = 0
    for i in range(len(data)):
        point = data[i]
        label = labels[i]
        center = centers[label]
        sse_error += dist(center, point)
    return sse_error   

################### K-Means ##################### 
def kmeans(data, k , r):
    min_error = inf
    output_labels = None
    
    for i in range(r):
        initial_points = initial(data, k)
        clustered_points = clustering(data, initial_points)
        new_center = recenter(data, clustered_points)
        old_center = initial_points 
    
        # check the new center
        while old_center != new_center:
            old_center = new_center
            labels = clustering(data, old_center)
            new_center = recenter(data, labels)
          
        error = sse(data, labels)
        if min_error > error:
            min_error = error
            output_labels = labels
    print(round(min_error,4))
    return output_labels    
       
################## Main Program ##################
if __name__ == "__main__":
    input_file = str(sys.argv[1])
    k = int(sys.argv[2])
    r = int(sys.argv[3])
    output_file = str(sys.argv[4])
    
    input_data = np.loadtxt(input_file, delimiter=',')
    output_labels = kmeans(input_data, k , r)
    np.savetxt(output_file, output_labels)

    
    
    