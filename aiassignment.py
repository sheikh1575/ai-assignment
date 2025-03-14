'''The program implements Dijkstras Algorithm to found out the shortest paths in a weighted graph using adjacency matrix. Nonzero values represent travel cost between nodes, zero indicates no direct path. The algorithm starts by identifying all nodes as unvisited and assuming their distances to infinity, except for the starting node, which is set to zero obviously. It then selects the unvisited node with the smallest known distance, marks it as visited, and updates the distances of neighboring nodes. If a shorter path is found, the distance is updated. This implementation represents a navigation system of the constable building, where nodes correspond to Door, CB42, CB32, Vending Machine (VM), and Common room. The cost for CB42 is higher (10) due to a busy corridor, while CB32 (2) follows a quieter path. The algorithm calculates the shortest routes from Door (node 0) to other locations. The dijkstra() function contains the core logic, while begin_dijkstra() runs the algorithm. The output displays the shortest distances. Dijkstra algorithm is highly efficient for graphs with non-negative edge weights and is widely used in navigation, routing, and network optimization.'''

import numpy as np 

# Adjacency matrix representing the graph
adj_matrix = np.array([ 
    # Door  CB42  CB32  VM   CR 
    [  0,    10,   2,    0,    0],  # Door to CB42(10), Door to CB32(2) 
    [  0,     1,   3,    2,    0],  # CB42 to CB42(1), CB42 to CB32(3), CB42 to VM(2)
    [  0,     2,   4,    3,    9],  # CB32 to CB42(2), CB32 to CB32(4), CB32 to VM(3), CB32 to CR(9)
    [  0,     3,   2,    6,   10],  # VM to CB42(3), VM to CB32(2), VM to VM(6), VM to CR(10)
    [  0,     2,   1,    7,    1]   # CR to CB42(2), CR to CB32(1), CR to VM(7), CR to CR(1)
]) 

# Count number of edges
num_edges = np.count_nonzero(adj_matrix)
print(f"Number of edges: {num_edges}")

start_node = 0  # Defines starting node

def dijkstra(adj_matrix, start): 
    num_nodes = len(adj_matrix)  # Determine number of nodes in graph
    distances = [float('inf')] * num_nodes  # Initialize distances to infinity
    distances[start] = 0  # Set start node distance to 0
    visited = [False] * num_nodes  # Track visited nodes
    
    for _ in range(num_nodes): 
        min_distance = float('inf')  # Track smallest distance
        min_index = -1  # Store index of node with minimum distance

        for i in range(num_nodes): 
            if not visited[i] and distances[i] < min_distance: 
                min_distance = distances[i] 
                min_index = i 
        
        if min_index == -1:
            break  # All reachable nodes are visited
        
        visited[min_index] = True  # Mark node as visited
        
        for neighbour in range(num_nodes):  
            edge_weight = adj_matrix[min_index][neighbour]
            if edge_weight > 0 and not visited[neighbour]:
                new_distance = distances[min_index] + edge_weight 
                if new_distance < distances[neighbour]: 
                    distances[neighbour] = new_distance  
    
    return distances 

# Function to run Dijkstra's algorithm and print results
def begin_dijkstra(adj_matrix, start_node): 
    shortest_distances = dijkstra(adj_matrix, start_node)  
    print(f"Shortest distances from node {start_node}: {shortest_distances}")

begin_dijkstra(adj_matrix, start_node)
