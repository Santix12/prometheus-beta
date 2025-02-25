from typing import List, Tuple, Dict

class DisjointSet:
    """
    Disjoint Set data structure for tracking connected components
    using path compression and union by rank.
    """
    def __init__(self, vertices: int):
        """
        Initialize disjoint set with given number of vertices.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item: int) -> int:
        """
        Find the root of a set with path compression.
        
        Args:
            item (int): Vertex to find the root for
        
        Returns:
            int: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: int, y: int) -> bool:
        """
        Union two sets by rank.
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        
        Returns:
            bool: True if union was successful, False if already in same set
        """
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        # Union by rank
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        
        return True

def boruvkas_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Boruvka's algorithm to find the Minimum Spanning Tree.
    
    Args:
        vertices (int): Number of vertices in the graph
        edges (List[Tuple[int, int, int]]): List of edges, where each edge is 
                                            (source, destination, weight)
    
    Returns:
        List[Tuple[int, int, int]]: List of edges in the Minimum Spanning Tree
    
    Raises:
        ValueError: If the graph is not connected or input is invalid
    """
    # Input validation
    if vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        return []

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Create disjoint set
    disjoint_set = DisjointSet(vertices)
    
    # Result MST
    mst = []
    
    # Track number of components
    components = vertices
    
    while components > 1:
        # Track cheapest edge for each component
        cheapest = [None] * vertices
        
        # Find cheapest edge connecting each component
        for edge in edges:
            u, v, weight = edge
            u_root = disjoint_set.find(u)
            v_root = disjoint_set.find(v)
            
            # Skip if same component
            if u_root == v_root:
                continue
            
            # Update cheapest edge if needed
            if (cheapest[u_root] is None or 
                weight < cheapest[u_root][2]):
                cheapest[u_root] = edge
            
            if (cheapest[v_root] is None or 
                weight < cheapest[v_root][2]):
                cheapest[v_root] = edge
        
        # Add cheapest edges that connect different components
        for cheap_edge in cheapest:
            if cheap_edge is None:
                continue
            
            u, v, weight = cheap_edge
            
            # Try to union the components
            if disjoint_set.union(u, v):
                mst.append(cheap_edge)
                components -= 1
        
        # If no edges were added, graph is not connected
        if not mst:
            raise ValueError("Graph is not connected")
    
    return mst