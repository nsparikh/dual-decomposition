import random
from tree import *

'''
Minimizes the energy in the pairwise graph and returns the energy value.
Takes the following inputs:
	- graph represented as a 2D matrix 
	- vector containing number of possible states for each node
	- unary vector, which is real-valued and has length n (where n
	  is the sum of the number of possible states per node). This vector
	  contains all the unary potential function values.
	- sparse pairwise matrix, which is real-valued and size nxn. This
	  matrix contains all the pairwise potential function values.
'''
def solver(graph, num_possible_states, unary, pairwise):
	num_nodes = len(num_possible_states)

	# Basic approach
	# 1) Divide problem into sub-problems such that each sub-problem
	#	 is tree-structured
	# 2) Solving sub-problems is easier with max-product algorithm
	#	 to estimate an exact optimal solution x_bar for each tree
	# 3) Master updates MRF parameters of all slave MRFs based on 
	#	 optimal solutions x_bar for each T from previous iteration

	subtrees = build_subtrees(graph)
	


'''
Helper function to build subtrees from the graph
Returns a list of lists of trees containing each node in the graph
'''
def build_subtrees(graph):
	pass



'''
Helper function to solve one sub-problem (e.g. one sub-tree that contains 
	the current node p). 
Returns the optimal solution vector x_bar where x_bar[i]=1 if label_i is 
	assigned to the current node p, and 0 otherwise.
Takes the following inputs:
	- subtree T
	- unary potential values theta_p_T
	- pairwise potential values theta_pq_T
'''
def solve_subtree(subtree, theta_p_T, theta_pq_T):
	pass

'''
Runs the solver by generating a random graph with random potentials,
finds the assignment with the lowest possible energy, and prints out
this energy value.
'''
def tester():
	NUM_NODES = 5 # Total number of nodes in the graph
	NUM_EDGES = 5 # Total number of edges in the graph
	MAX_POSSIBLE_STATES = 3 # Max number of possible states for any node
	MAX_ENERGY = 100 # Max energy value

	# Generate random graph matrix
	# graph[x][y] = 1 if there is an edge between x and y, 0 otherwise
	graph = build_graph(NUM_NODES, NUM_EDGES)

	# Generate vector containing number of possible states for each node
	num_possible_states = [random.randint(1, MAX_POSSIBLE_STATES) for i in range(NUM_NODES)]
	n = sum(num_possible_states)

	# Generate random unary potential values
	unary = [random.randint(0, MAX_ENERGY) for i in range(n)]

	# Generate sparse random pairwise potential values
	# Assigns a random energy value in range (0, MAX_ENERGY) to a given
	# 	pair (i, j) with probability 0.25
	pairwise = ([[random.randint(0, MAX_ENERGY) 
		if random.random() < 0.25 else float("inf")
		for i in range(n)]
		for j in range(n)])

	# Call solver on randomly generated data
	print solver(graph, num_possible_states, unary, pairwise)

'''
Helper method to build a random graph with num_nodes nodes and num_edges edges.
Represents the graph as a 2D matrix where graph[i][j] = 1 and graph[j][i] = 1
if there is an edge between nodes i and j.
'''
def build_graph(num_nodes, num_edges):
	graph = [[0 for i in range(num_nodes)] for j in range(num_nodes)]
	for i in range(num_edges):
		# Find a random pair of nodes that has no edge
		while True:
			n1 = random.randint(0, num_nodes-1)
			n2 = random.randint(0, num_nodes-1)
			while n1 == n2:
				n2 = random.randint(0, num_nodes-1)
			if graph[n1][n2] == 0:
				graph[n1][n2] = 1
				graph[n2][n1] = 1
				break
	return graph


tester()

