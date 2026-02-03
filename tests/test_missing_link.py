import pytest
import pandas as pd
import numpy as np
from app.services.validator import check_missing_link

def test_check_missing_link_nan_handling():
    df = pd.DataFrame({
        "link": [
            "http://valid-link.com", 
            None, 
            np.nan, 
            "", 
            "   "  # whitespace might be considered "missing" depending on logic, but currently explicit empty string or nan
        ],
        "name": ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    })
    
    results = check_missing_link(df)
    
    # We expect errors for None, np.nan, and ""
    # "   " is technically not empty string, so current logic might pass it if not stripped. 
    # Based on the fix: if pd.isna(row.get('link')) or row.get('link') == "":
    
    error_rows = [r.row for r in results]
    assert 1 in error_rows  # None
    assert 2 in error_rows  # np.nan
    assert 3 in error_rows  # ""
    assert 0 not in error_rows # valid link
