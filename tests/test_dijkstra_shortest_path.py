import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_shortest_path():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    result = dijkstra_shortest_path(graph, 'A', 'D')
    assert result['D'][0] == 6  # Shortest distance
    assert result['D'][1] == ['A', 'C', 'B', 'D']  # Shortest path

def test_all_paths_from_start():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    result = dijkstra_shortest_path(graph, 'A')
    assert len(result) == 4
    assert result['A'][0] == 0
    assert result['B'][0] == 3
    assert result['C'][0] == 2
    assert result['D'][0] == 6

def test_disconnected_node():
    graph = {
        'A': {'B': 4},
        'B': {},
        'C': {}
    }
    result = dijkstra_shortest_path(graph, 'A')
    assert result['C'][0] == float('inf')
    assert result['C'][1] == []

def test_single_node_graph():
    graph = {'A': {}}
    result = dijkstra_shortest_path(graph, 'A')
    assert result['A'][0] == 0
    assert result['A'][1] == ['A']

def test_invalid_start_node():
    graph = {'A': {'B': 1}, 'B': {}}
    with pytest.raises(ValueError, match="Start node 'C' not found in graph"):
        dijkstra_shortest_path(graph, 'C')

def test_self_referencing_node():
    graph = {
        'A': {'A': 1, 'B': 4},
        'B': {}
    }
    result = dijkstra_shortest_path(graph, 'A', 'B')
    assert result['B'][0] == 4
    assert result['B'][1] == ['A', 'B']

def test_cyclic_graph():
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'C': 1},
        'C': {'A': 1}
    }
    result = dijkstra_shortest_path(graph, 'A', 'C')
    assert result['C'][0] == 2
    assert result['C'][1] == ['A', 'B', 'C']