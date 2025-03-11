"""
Tests for browser performance metrics logging functionality.
"""

import json
import logging
import time
import io
import pytest
from src.browser_performance import log_browser_performance_metrics

def test_log_browser_performance_metrics_default():
    """Test logging performance metrics with default parameters."""
    # Capture log output
    log_capture = io.StringIO()
    
    # Set up logging
    logging.basicConfig(stream=log_capture, level=logging.INFO, format='%(message)s')
    
    # Call the function
    result = log_browser_performance_metrics()
    
    # Get the log content
    log_capture.seek(0)
    log_output = log_capture.read().strip()
    
    # Assert basic structure of returned metrics
    assert isinstance(result, dict)
    assert 'timestamp' in result
    assert 'process_time' in result
    assert 'monotonic_time' in result
    
    # Verify log was created
    assert log_output, "No log output found"
    
    # Parse the logged JSON
    logged_data = json.loads(log_output)
    assert isinstance(logged_data, dict)
    assert 'timestamp' in logged_data
    assert 'process_time' in logged_data
    assert 'monotonic_time' in logged_data

def test_log_browser_performance_metrics_with_custom():
    """Test logging performance metrics with custom metrics."""
    custom_metrics = {
        "custom_metric1": 42,
        "custom_metric2": "test_value"
    }
    
    # Capture log output
    log_capture = io.StringIO()
    
    # Set up logging
    logging.basicConfig(stream=log_capture, level=logging.INFO, format='%(message)s')
    
    # Call the function with custom metrics
    result = log_browser_performance_metrics(metrics=custom_metrics)
    
    # Get the log content
    log_capture.seek(0)
    log_output = log_capture.read().strip()
    
    # Assert custom metrics are included
    assert result['custom_metric1'] == 42
    assert result['custom_metric2'] == "test_value"
    
    # Verify log was created
    assert log_output, "No log output found"
    
    # Parse the logged JSON
    logged_data = json.loads(log_output)
    assert logged_data['custom_metric1'] == 42
    assert logged_data['custom_metric2'] == "test_value"

def test_log_browser_performance_metrics_invalid_input():
    """Test error handling for invalid input."""
    with pytest.raises(ValueError, match="Metrics must be a dictionary or None"):
        log_browser_performance_metrics(metrics="not a dictionary")

def test_log_browser_performance_metrics_time_progression():
    """Test that time-related metrics are progressing correctly."""
    # First call
    result1 = log_browser_performance_metrics()
    time.sleep(0.1)  # Small delay
    result2 = log_browser_performance_metrics()
    
    # Assert timestamps are increasing
    assert result2['timestamp'] > result1['timestamp']
    assert result2['process_time'] > result1['process_time']
    assert result2['monotonic_time'] > result1['monotonic_time']