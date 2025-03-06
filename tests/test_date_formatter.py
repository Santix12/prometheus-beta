import re
from datetime import date
import pytest
from src.date_formatter import get_current_date_formatted

def test_get_current_date_formatted():
    """
    Test that the function returns a date in the correct format.
    """
    # Get the formatted date
    formatted_date = get_current_date_formatted()
    
    # Check that the return value is a string
    assert isinstance(formatted_date, str), "Return value should be a string"
    
    # Check that the date matches YYYY-MM-DD format using regex
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', formatted_date), \
        "Date should be in YYYY-MM-DD format"
    
    # Verify the date matches today's date
    today = date.today().strftime('%Y-%m-%d')
    assert formatted_date == today, "Returned date should match today's date"

def test_date_format_consistency():
    """
    Verify that multiple calls return consistent format.
    """
    date1 = get_current_date_formatted()
    date2 = get_current_date_formatted()
    
    assert date1 == date2, "Multiple calls should return the same date"