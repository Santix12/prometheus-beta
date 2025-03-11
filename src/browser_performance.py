"""
Module for logging browser rendering performance metrics.

This module provides functionality to capture and log key performance 
metrics related to browser rendering.
"""

import json
import logging
import time
from typing import Dict, Any, Optional

def log_browser_performance_metrics(
    metrics: Optional[Dict[str, Any]] = None, 
    log_level: int = logging.INFO
) -> Dict[str, Any]:
    """
    Log browser rendering performance metrics.

    This function captures key performance metrics and logs them with optional
    additional custom metrics. It uses the standard logging module to record 
    the metrics.

    Args:
        metrics (Optional[Dict[str, Any]], optional): 
            Additional custom metrics to include. Defaults to None.
        log_level (int, optional): 
            Logging level for the metrics. Defaults to logging.INFO.

    Returns:
        Dict[str, Any]: A dictionary containing all captured performance metrics.

    Raises:
        ValueError: If metrics provided are not a dictionary.
    """
    # Validate input metrics
    if metrics is not None and not isinstance(metrics, dict):
        raise ValueError("Metrics must be a dictionary or None")

    # Prepare the performance metrics dictionary
    performance_data = {
        "timestamp": time.time(),
        "process_time": time.process_time(),
        "monotonic_time": time.monotonic(),
    }

    # Add any custom metrics, giving them priority in case of key conflicts
    if metrics:
        performance_data.update(metrics)

    # Convert to JSON for logging
    log_message = json.dumps(performance_data)

    # Log the performance metrics
    logger = logging.getLogger(__name__)
    logger.log(log_level, log_message)

    return performance_data