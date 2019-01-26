# Agglomerative (Hierarchical) Clustering in Python

# Assumptions:
# 	1. Data entered as lower triangular matrix
# 	2. Distance between two points = d, such that -999<d<999
# 	3. Distance of point to itself specified as 0; i.e., matrix[i][i]=0

# Locate Minimum value and indices of first occurance in given matrix
# Append Minimum value to dendogram and return indices
def minimum(matrix):
	min_value = 999
	row = col = -1
	for point in matrix:
		length = len(point)
		# Skip first point row, i.e. matrix[0] = [ 0 ]
		if length > 1:
			# Find point closest to 'point'
			closest = min(distance for distance in point[:length-1]) # To reject coincidental points in data: if p > 0)
			if closest < min_value:
				min_value=closest
				row=matrix.index(point)
				column=point.index(closest)
	return (min_value,row,column)

# Locate Maximum value and indices of first occurance in given matrix
# Append Maximum value to dendogram and return indices
def maximum(matrix):
	max_value = -999
	row = col = -1
	for point in matrix:
		length = len(point)
		# Skip first point row, i.e. matrix[0] = [ 1 ]
		if length > 1:
			# Find point most similar to 'point'
			similar = max(distance for distance in point[:length-1]) # To reject coincidental points in data: if p < 1)
			if similar > max_value:
				max_value=similar
				row=matrix.index(point)
				column=point.index(similar)
	return (max_value,row,column)

def single(matrix,m_type,point_labels):
	print("Single Linkage --- ")
	dendogram = []
	# Dissimilarity matrix
	if m_type == 0:
		while len(matrix) > 1:
			# Find closest points in Matrix
			distance, point1, point2=minimum(matrix)
			# Identify the points that appear earlier (low) and later (high) in the point_labels
			if point1 < point2:
				low=point1
				high=point2
			else:
				low = point2
				high = point1

			# Append values to Dendogram
			dendogram.append((distance,(point_labels[low],point_labels[high])))
			# Update Labels
			point_labels[low] += point_labels[high]
			del point_labels[high]
			print("Labels: ",point_labels)
			# Generate new matrix: Row-wise traversal
			for i in xrange(len(matrix)):
				# Points before earlier point -- if i < low:
					# No change -- matrix[i]=matrix[i]
				# Earlier point row
				if i == low:
					# Compare earlier point and later point values and make selection
					for j in xrange(i):
						matrix[i][j]=min([matrix[low][j],matrix[high][j]])
				# Points between earlier point and later point
				elif i > low and i < high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=min([matrix[i][low],matrix[high][i]])
				# Points after later point
				elif i > high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=min([matrix[i][low],matrix[i][high]])
					# Shift all values beyond matrix[i][high] leftwards
					j=high
					while j < i:
						matrix[i][j]=matrix[i][j+1]
						j += 1
					# Delete last (duplicate: 0 '0') value in row
					del matrix[i][len(matrix[i])-1]
			# Delete row for later point
			del matrix[high]

	# Similarity Matrix
	if m_type == 1:
		while len(matrix) > 1:
			# Find most similar points in Matrix
			distance, point1, point2=maximum(matrix)
			# Identify the points that appear earlier (low) and later (high) in the point_labels
			if point1 < point2:
				low=point1
				high=point2
			else:
				low = point2
				high = point1

			# Append values to Dendogram
			dendogram.append((distance,(point_labels[low],point_labels[high])))
			# Update Labels
			point_labels[low] += point_labels[high]
			del point_labels[high]
			print("Labels: ",point_labels)
			# Generate new matrix: Row-wise traversal
			for i in xrange(len(matrix)):
				# Earlier point row
				if i == low:
					# Compare earlier point and later point values and make selection
					for j in xrange(i):
						matrix[i][j]=max([matrix[low][j],matrix[high][j]])
				# Points between earlier point and later point
				elif i > low and i < high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=max([matrix[i][low],matrix[high][i]])
				# Points after later point
				elif i > high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=max([matrix[i][low],matrix[i][high]])
					# Shift all values beyong matrix[i][high] leftwards
					j=high
					while j < i:
						matrix[i][j]=matrix[i][j+1]
						j += 1
					# Delete last (duplicate: 0 '0') value in row
					del matrix[i][len(matrix[i])-1]
			# Delete row for later point
			del matrix[high]
	print("Dendogram: ",dendogram)

def complete(matrix,m_type,point_labels):
	print("Complete Linkage --- ")
	dendogram = []
	# Dissimilarity Matrix
	if m_type == 0:
		while len(matrix) > 1:
			# Find closest points in Matrix
			distance, point1, point2=minimum(matrix)
			# Identify the points that appear earlier (low) and later (high) in the point_labels
			if point1 < point2:
				low=point1
				high=point2
			else:
				low = point2
				high = point1

			# Append values to Dendogram
			dendogram.append((distance,(point_labels[low],point_labels[high])))
			# Update Labels
			point_labels[low] += point_labels[high]
			del point_labels[high]
			print("Labels: ",point_labels)
			# Generate new matrix: Row-wise traversal
			for i in xrange(len(matrix)):
				# Earlier point row
				if i == low:
					# Compare earlier point and later point values and make selection
					for j in xrange(i):
						matrix[i][j]=max([matrix[low][j],matrix[high][j]])
				# Points between earlier point and later point
				elif i > low and i < high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=max([matrix[i][low],matrix[high][i]])
				# Points after later point
				elif i > high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=max([matrix[i][low],matrix[i][high]])
					# Shift all values beyong matrix[i][high] leftwards
					j=high
					while j < i:
						matrix[i][j]=matrix[i][j+1]
						j += 1
					# Delete last (duplicate: 0 '0') value in row
					del matrix[i][len(matrix[i])-1]
			# Delete row for later point
			del matrix[high]

	# Similarity Matrix
	if m_type == 1:
		while len(matrix) > 1:
			# Find closest points in Matrix
			distance, point1, point2=maximum(matrix)
			# Identify the points that appear earlier (low) and later (high) in the point_labels
			if point1 < point2:
				low=point1
				high=point2
			else:
				low = point2
				high = point1

			# Append values to Dendogram
			dendogram.append((distance,(point_labels[low],point_labels[high])))
			# Update Labels
			point_labels[low] += point_labels[high]
			del point_labels[high]
			print("Labels: ",point_labels)
			# Generate new matrix: Row-wise traversal
			for i in xrange(len(matrix)):
				# Earlier point row
				if i == low:
					# Compare earlier point and later point values and make selection
					for j in xrange(i):
						matrix[i][j]=min([matrix[low][j],matrix[high][j]])
				# Points between earlier point and later point
				elif i > low and i < high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=min([matrix[i][low],matrix[high][i]])
				# Points after later point
				elif i > high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=min([matrix[i][low],matrix[i][high]])
					# Shift all values beyong matrix[i][high] leftwards
					j=high
					while j < i:
						matrix[i][j]=matrix[i][j+1]
						j += 1
					# Delete last (duplicate: 0 '0') value in row
					del matrix[i][len(matrix[i])-1]
			# Delete row for later point
			del matrix[high]
	print("Dendogram: ",dendogram)

def aggregate(matrix,m_type,point_labels):
	print("Aggregate Linkage --- ")
	dendogram = []
	# Dissimilarity Matrix
	if m_type == 0:
		while len(matrix) > 1:
			# Find closest points in Matrix
			distance, point1, point2=minimum(matrix)
			# Identify the points that appear earlier (low) and later (high) in the point_labels
			if point1 < point2:
				low=point1
				high=point2
			else:
				low = point2
				high = point1

			# Append values to Dendogram
			dendogram.append((distance,(point_labels[low],point_labels[high])))
			# Update Labels
			point_labels[low] += point_labels[high]
			del point_labels[high]
			print("Labels: ",point_labels)
			# Generate new matrix: Row-wise traversal
			for i in xrange(len(matrix)):
				# Earlier point row
				if i == low:
					# Compare earlier point and later point values and make selection
					for j in xrange(i):
						matrix[i][j]=(matrix[low][j]+matrix[high][j])/2
				# Points between earlier point and later point
				elif i > low and i < high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=(matrix[low][j]+matrix[high][j])/2
				# Points after later point
				elif i > high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=(matrix[i][low]+matrix[i][high])/2
					# Shift all values beyong matrix[i][high] leftwards
					j=high
					while j < i:
						matrix[i][j]=matrix[i][j+1]
						j += 1
					# Delete last (duplicate: 0 '0') value in row
					del matrix[i][len(matrix[i])-1]
			# Delete row for later point
			del matrix[high]

	# Similarity Matrix
	if m_type == 1:
		while len(matrix) > 1:
			# Find closest points in Matrix
			distance, point1, point2=maximum(matrix)
			# Identify the points that appear earlier (low) and later (high) in the point_labels
			if point1 < point2:
				low=point1
				high=point2
			else:
				low = point2
				high = point1

			# Append values to Dendogram
			dendogram.append((distance,(point_labels[low],point_labels[high])))
			# Update Labels
			point_labels[low] += point_labels[high]
			del point_labels[high]
			print("Labels: ",point_labels)
			# Generate new matrix: Row-wise traversal
			for i in xrange(len(matrix)):
				# Earlier point row
				if i == low:
					# Compare earlier point and later point values and make selection
					for j in xrange(i):
						matrix[i][j]=(matrix[low][j]+matrix[high][j])/2
				# Points between earlier point and later point
				elif i > low and i < high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=(matrix[low][j]+matrix[high][j])/2
				# Points after later point
				elif i > high:
					# Compare earlier point and later point values and make selection
					matrix[i][low]=(matrix[i][low]+matrix[i][high])/2
					# Shift all values beyong matrix[i][high] leftwards
					j=high
					while j < i:
						matrix[i][j]=matrix[i][j+1]
						j += 1
					# Delete last (duplicate: 0 '0') value in row
					del matrix[i][len(matrix[i])-1]
			# Delete row for later point
			del matrix[high]
	print("Dendogram: ",dendogram)

# Accept Data
# Number of Points
points = int(raw_input("Enter the number of points: "))

# Label of each point as string for dendogram
# point_labels = ["1","2","3","4","5"]
point_labels = raw_input("Enter the labels for each point: ").split()

# Type of Matrix: 0-Dissimilarity, 1=Similarity
m_type = int(raw_input("Enter the type of matrix (0=Dissimilarity, 1=Similarity): "))

# Proximity Matrix: Lower Triangular with matrix[i][i]=m_type
matrix = []
for i in xrange(points):
	matrix.append([float(x) for x in raw_input("{}: ".format(point_labels[i])).split()])

# Create three copies of input matrix and point_labels
s_matrix = [p[:] for p in matrix]
c_matrix = [p[:] for p in matrix]
a_matrix = [p[:] for p in matrix]

s_point_labels = [p[:] for p in point_labels]
c_point_labels = [p[:] for p in point_labels]
a_point_labels = [p[:] for p in point_labels]

single(s_matrix,m_type,s_point_labels)
complete(c_matrix,m_type,c_point_labels)
aggregate(a_matrix,m_type,a_point_labels)