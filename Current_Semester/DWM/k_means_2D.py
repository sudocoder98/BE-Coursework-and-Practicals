# K-Means for 2D Data in Python

import random
# Define Math function
def sq(n):
	return n**2
def sqrt(n):
	return n**0.5
# Accept Data
print("Separate each pair of coordinates with a comma (,) like this: 2 3, 4 10")
data = [tuple([int(y) for y in x.strip().split()]) for x in raw_input("Enter the data points: ").split(',')]
# Input
# 2 10 , 2 5 , 8 4 , 5 8 ,7 5 , 6 4 , 1 2 , 4 9
# 2 10 , 5 8 , 1 2
# centroids = [tuple([int(y) for y in x.strip().split()]) for x in raw_input("Enter the centroid points: ").split(',')]
# k = len(centroids)
centroids = [ ]
k = input("Enter the number of clusters: ")
min_x = min(data)[0]
min_y = min(data, key = lambda tup: tup[1])[0]
max_x = max(data)[0]
max_y = max(data, key = lambda tup: tup[1])[0]
for i in xrange(k):
	centroids.append((random.randint(min_x,max_x),random.randint(min_y,max_y)))

# Define K-Means functions
def clustering(data, centroids, k):
	# Initialising clusters
	clusters = []
	for i in xrange(k):
		clusters.append([])
	# Clustering
	for (dx,dy) in data:
		distance = []
		for (cx,cy) in centroids:
			distance.append(sqrt(sq(cx-dx)+sq(cy-dy)))
		clusters[distance.index(min(distance))].append((dx,dy))
	return clusters

def calcMean(clusters, k):
	means = [ ]
	for cluster in clusters:
		sumx = 0
		sumy = 0
		for (dx,dy) in cluster:
			sumx += dx
			sumy += dy
		if len(cluster) != 0:
			means.append((float(sumx)/len(cluster),float(sumy)/len(cluster)))
	return means

def updateCentroids(centroids, means, k):
	stop = 1
	for i in xrange(k):
		if i<len(means):
			dx,dy = means[i]
		else:
			dx,dy = 0,0
		cx, cy = centroids[i]
		if dx != cx or dy != cy:
			stop = 0
		# Replace old Centroids with new Means
		centroids[i] = (dx,dy) # means[i]
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