# K-Means for 1D Data in Python

import random
# Accept data
print("Separate each data point with a space ' ' like this: 2 3 4 10")
data = [int(x) for x in raw_input("Enter the data points: ").split()]
data.sort()
# Input: 
# 2 4 10 12 3 20 30 11 25
# 2 4
# centroids = [int(x) for x in raw_input("Enter the centroids: ").split()]
# k = len(centroids)
centroids = [ ]
k = input("Enter the number of clusters: ")
for i in xrange(k):
	centroids.append(random.randint(data[0], data[k-1]))

# Define K-Means functions
def clustering(data, centroids, k):
	# Initialising clusters
	clusters = []
	for i in xrange(k):
		clusters.append([])
	# Clustering
	for dataPoint in data:
		distance = []
		for centroid in centroids:
			distance.append((abs(dataPoint-centroid)))
		# print(distance)
		clusters[distance.index(min(distance))].append(dataPoint)
	return clusters

def calcMean(clusters, k):
	means = [ ]
	for cluster in clusters:
		total = 0
		for dataPoint in cluster:
			total += dataPoint
		if len(cluster) != 0:
			means.append(float(total)/len(cluster))
	return means

def updateCentroids(centroids, means, k):
	stop = 1
	for i in xrange(k):
		print(means[i], centroids[i])
		if means[i] != centroids[i]:
			stop = 0
		# Replace old Centroids with new Means
		centroids[i] = means [i]
	return stop

# Define control variables
stop = 0
iteration = 0

# K-Means Loop
while stop != 1:
	iteration += 1
	print("Iteration: ",iteration)
	# Cluster the data
	clusters = clustering(data, centroids, k)
	print("Clusters: ",clusters)

	# Calculate Means
	means = calcMean(clusters, k)
	print("Means: ",means)

	#Compare old Centroids with new Means
	stop = updateCentroids(centroids, means, k)

print("Final Clusters: ", clusters)