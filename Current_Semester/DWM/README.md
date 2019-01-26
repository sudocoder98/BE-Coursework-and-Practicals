
# List of Experiments

## Experiment 1
### To perform K-Means clustering on 1D and 2D data

1. [k_means_1D.py](k_means_1D.py)
  - To allow user to input centroids comment lines 11-14 and uncomment lines 9-10  
    Input:  
    2 4 10 12 3 20 30 11 25  
    2 4  
  
  - To generate centroids comment lines 9-10 and uncomment lines 11-14  
    Input:  
    2 4 10 12 3 20 30 11 25  
    2  

2. [k_means_2D.py](k_means_2D.py)
  - To allow user to input centroids comment lines 15-22 and uncomment lines 13-14  
    Input:  
    2 10 , 2 5 , 8 4 , 5 8 ,7 5 , 6 4 , 1 2 , 4 9  
    2 10 , 5 8 , 1 2  
  - To generate centroids comment lines 9-10 and uncomment lines 11-14  
    Input:  
    2 10 , 2 5 , 8 4 , 5 8 ,7 5 , 6 4 , 1 2 , 4 9  
    3  

**Note:** 
- Both files are currently set to generate random centroids for the specified number of clusters. 
- Generating random centroids may not always result in the same number of clusters as specified.

## Experiment 2
### [To perform K-Nearest Neighbours on 2D data](knn.py)

Sample Input:  
Enter the list of classifiers separated by spaces: Good Bad  
Enter the data points and their classification: 7 7 Bad, 7 4 Bad, 3 4 Good, 1 4 Good  
Enter the test coordinates: 3 7  
Enter the size of the cluster: 3  

Output:  
Classification:  Good  

## Experiment 3
### [To perform Agglomerative (Hierarchical) Clustering](agglomerative_clustering.py)

Sample Input:  
Enter the number of points: 4  
Enter the labels for each point: A B C D  
Enter the type of matrix (0=Dissimilarity, 1=Similarity): 0  
A: 0  
B: 1 0  
C: 4 2 0  
D: 5 6 3 0  

Output:  
Single Linkage ---   
('Labels: ', ['AB', 'C', 'D'])  
('Labels: ', ['ABC', 'D'])  
('Labels: ', ['ABCD'])  
('Dendogram: ', [(1.0, ('A', 'B')), (2.0, ('AB', 'C')), (3.0, ('ABC', 'D'))])  
Complete Linkage ---   
('Labels: ', ['AB', 'C', 'D'])  
('Labels: ', ['AB', 'CD'])  
('Labels: ', ['ABCD'])  
('Dendogram: ', [(1.0, ('A', 'B')), (3.0, ('C', 'D')), (6.0, ('AB', 'CD'))])  
Aggregate Linkage ---   
('Labels: ', ['AB', 'C', 'D'])  
('Labels: ', ['ABC', 'D'])  
('Labels: ', ['ABCD'])  
('Dendogram: ', [(1.0, ('A', 'B')), (3.0, ('AB', 'C')), (4.25, ('ABC', 'D'))])  