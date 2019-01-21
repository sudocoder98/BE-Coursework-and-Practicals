# K-Nearest Neighbours for 2D Data in Python

# Define Math function
def sq(n):
	return n**2
def sqrt(n):
	return n**0.5

# Accept Data
classifiers = [[x,0] for x in input("Enter the list of classifiers separated by spaces: ").split()]
historic_data = [tuple([y for y in x.strip().split()]) for x in input("Enter the data points and their classification: ").split(',')]
test = tuple(int(x) for x in input("Enter the test coordinates: ").split())
k = int(input("Enter the size of the cluster: "))

# Caluculate distance between test point and historic data points
distance = [ ]
for data in historic_data:
	distance.append(sqrt(sq(int(data[0])-test[0])+sq(int(data[1])-test[1])))

# Select k points with minimum distances into cluster
cluster = [ ]
for i in range(k):
	cluster.append(historic_data[distance.index(min(distance))])
	distance[distance.index(min(distance))]=9999

# Find the maximum occuring classifier in the cluster
max = [ "", 0 ]
for data in cluster:
	for classifier in classifiers:
		if data[2] == classifier[0]:
			classifier[1] = int(classifier[1]) + 1
			if classifier[1]>max[1]:
				max = classifier

print("Classification: ",max[0])