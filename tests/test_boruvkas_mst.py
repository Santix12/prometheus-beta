import pytest
from src.boruvkas_mst import boruvkas_mst, DisjointSet

def test_disjoint_set():
    """Test Disjoint Set data structure functionality."""
    ds = DisjointSet(5)
    
    # Initial state
    assert ds.find(0) != ds.find(1)
    assert ds.find(2) == 2
    
    # Union operation
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Multiple unions
    ds.union(2, 3)
    ds.union(3, 4)
    assert ds.find(2) == ds.find(3)
    assert ds.find(2) == ds.find(4)
    
    # Ensure same set elements are not re-unioned
    assert not ds.union(0, 1)

def test_boruvkas_mst_basic():
    """Test Boruvka's algorithm with a simple connected graph."""
    # Vertices are 0-indexed
    vertices = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst = boruvkas_mst(vertices, edges)
    
    # Expected edges in MST (minimum total weight)
    expected_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
    
    # Validate MST
    assert len(mst) == vertices - 1
    assert sorted(mst, key=lambda x: x[2]) == sorted(expected_mst, key=lambda x: x[2])

def test_boruvkas_mst_single_vertex():
    """Test MST with single vertex."""
    vertices = 1
    edges = []
    
    mst = boruvkas_mst(vertices, edges)
    assert mst == []

def test_boruvkas_mst_error_handling():
    """Test error handling for invalid inputs."""
    # Invalid number of vertices
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvkas_mst(0, [(0, 1, 5)])
    
    # Disconnected graph
    with pytest.raises(ValueError, match="Graph is not connected"):
        boruvkas_mst(3, [(0, 1, 5)])

def test_boruvkas_mst_complex_graph():
    """Test Boruvka's algorithm with a more complex graph."""
    vertices = 6
    edges = [
        (0, 1, 1),
        (0, 2, 3),
        (1, 2, 4),
        (1, 3, 2),
        (2, 3, 5),
        (2, 4, 6),
        (3, 4, 7),
        (3, 5, 8),
        (4, 5, 9)
    ]
    
    mst = boruvkas_mst(vertices, edges)
    
    # Verify properties of MST
    assert len(mst) == vertices - 1
    assert sum(edge[2] for edge in mst) == 13  # Total weight of MST