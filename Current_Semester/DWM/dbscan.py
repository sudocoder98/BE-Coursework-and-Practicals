# Define Math function
def sq(n):
	return n**2
def sqrt(n):
	return n**0.5

# Accept Data
# Number of Points
points = int(raw_input("Enter the number of points: "))

# Label of each point as string for dendogram
# point_labels = ["1","2","3","4","5"]
point_labels = raw_input("Enter the labels for each point: ").split()

# Coordinates for each point
coordinates = [tuple([int(y) for y in x.strip().split()]) for x in raw_input("Enter the data points: ").split(',')]

# Radius of cluster
epsilon = float(raw_input("Enter the radius of cluster: "))

# Minimum Points
min_points = int(raw_input("Enter the minimum number of points in cluster: "))

# Proximity Matrix: Lower Triangular with matrix[i][i]=m_type
matrix = []
for i in xrange(points):
	matrix.append([])
	for j in xrange(i):
		matrix[i].append(sqrt(sq(coordinates[i][0]-coordinates[j][0])+sq(coordinates[i][1]-coordinates[j][1])))
	matrix[i].append(0)

# for i in xrange(points):
#	matrix.append([float(x) for x in raw_input("{}: ".format(point_labels[i])).split()])

# matrix = [[ 0 ] , [ 1 , 0 ] , [ 8 , 5 , 0 ] , [ 13 , 8 , 17 , 0 ] , [ 2 , 1 , 10 , 5 , 0 ] , [ 8 , 5 , 16 , 1 , 2 , 0 ] , [ 17 , 10 , 13 , 2 , 9 , 5 , 0 ] , [ 10 , 5 , 2 , 9 , 8 , 10 , 5 , 0 ] , [ 2 , 1 , 2 , 13 , 4 , 10 , 13 , 4 , 0 ] , [ 20 , 13 , 4 , 17 , 18 , 20 , 9 , 2 , 10 , 0 ] , [ 9 , 4 , 5 , 4 , 5 , 5 , 2 , 1 , 5 , 5 , 0 ] , [ 5 , 8 , 25 , 16 , 5 , 9 , 26 , 25 , 13 , 41 , 20 , 0 ] ]

clusters = []
point_type = []

for i in xrange(points):
	clusters.append([])
	for j in xrange(points):
		if j < i and matrix[i][j]<=epsilon:
			clusters[i].append(point_labels[j])
		elif j > i and matrix[j][i]<=epsilon:
			clusters[i].append(point_labels[j])
		elif j == i:
			clusters[i].append(point_labels[i])
	if len(clusters[i])>=min_points:
		point_type.append("Core")
	else:
		point_type.append("Noise")

for cluster in clusters:
	for point in cluster:
		if point_type[clusters.index(cluster)] =="Noise" and point_type[point_labels.index(point)] == "Core":
			point_type[clusters.index(cluster)] = "Border"

for i in xrange(points):
	print(point_labels[i],point_type[i],clusters[i])