import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra_shortest_path(graph: Dict[str, Dict[str, int]], start: str, end: Optional[str] = None) -> Dict[str, Tuple[int, List[str]]]:
    """
    Implement Dijkstra's algorithm to find shortest paths from a start node.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Each key is a node, with a dictionary of neighboring nodes and edge weights.
        start (str): Starting node for path calculation.
        end (Optional[str], optional): Optional destination node. If provided, 
                                       algorithm stops when the end is reached.
    
    Returns:
        Dict[str, Tuple[int, List[str]]]: Dictionary with nodes as keys and 
                                          tuples of (shortest distance, path) as values.
    
    Raises:
        ValueError: If start node is not in the graph.
    """
    # Validate start node
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")
    
    # Initialize distances and paths
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [start]
    
    # Priority queue to track nodes to visit
    pq = [(0, start)]
    
    # Track visited nodes to prevent revisiting
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if node already processed
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Goal condition if end node is specified
        if end is not None and current_node == end:
            break
        
        # Check neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Update if shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(pq, (distance, neighbor))
    
    # If end specified, return only the path to end
    if end is not None:
        return {end: (distances[end], paths[end])}
    
    # Return distances and paths for all nodes
    return {node: (distances[node], paths[node]) for node in graph}