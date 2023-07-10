from doctest import testmod
"""This code implements floyd's algorithm that its goal is to find the shoetest 
path between two vertices it gets the number of the vertices and weight of edges
between two graphs with matrix and print the shortest distance between 
two vertices"""
class Floyd:
    """this class gets graph g as initial number and returns the shortest way
    between two vertices that we can make infinite object fram this class
    >>> 0,1,100,1,5
    >>> 9,0,3,2,100
    >>> 100,100,0,4,100
    >>> 100,100,2,0,3
    >>> 3,100,100,100,0
    0,1,3,1,4
    8,0,3,2,5
    10,11,4,0,7
    6,7,2,0,3
    3,4,6,4,0
    param dist: a two_dimential list of the shortest distance between two 
    vertices in graph g .first of all, all amounts in this gragh adjusted into 
    infinite then updated the distances of the shortest route between both 
    vertices with Floyd algorithm
    """
    testmod()
    def __init__(self,g):
        self.g = g
        self.n = len(g)
#inf:بی نهایت که ان را 100 فرض میکنیم
    def floyd_algo(self):
        dist = [[float("inf")]*self.n for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                dist[i][j] = self. g[i][j]
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        return dist

"""
param g : a list that get numbers as a matrix
param n : the number of vertices that get from user
param r : gets a row of matrix which takes the direct distances between two 
graphs,which is the edge weight,from the user
param my_floyd : make a object from Floyd class
param my_answer: call the floyd_algo function in Floyd class to calculate the
shortest distance between two vertices and gets dist that was returned from 
the floyd_algo method of Floyd class 
"""
g = []
n = int(input("Enter the number of vertices:"))
for i in range(n):
    r = list(map(int, input("Enter the adjacency matrix:\n").split(",")))
    g.append(r)
my_floyd = Floyd(g)
my_answer = my_floyd.floyd_algo()
print("The shortest distance from both vertices:")
for i in range(n):
    for j in range(n):
        if my_answer[i][j] == 100:
            print("inf", end=" ") 
            continue
        print(my_answer[i][j],end=" ")
    print()
    



        