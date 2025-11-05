"""
test_basics.py

This script demonstrates how to test simple functions using pytest.

What is pytest?
-----------------
pytest is a Python testing framework that automatically detects and runs test files.
It reports which functions work correctly and which do not.

Why we test:
------------
Testing helps ensure that our functions behave as expected — 
an essential part of data literacy and trustworthy analysis.
Just as we should question data sources, we should verify that our code produces reliable results.

Usage:
------
Run the tests from your terminal with:
    pytest -v (or pytest 01_Fundamentals\test_basics.py)

Pytest automatically looks for all files named test_*.py
and runs all functions starting with test_.
"""
import sys
from pathlib import Path

# Dynamically resolve the absolute path to the Modules folder
module_path = Path(__file__).resolve().parents[1] / "Modules"
sys.path.append(str(module_path))

# Import the functions to test
from basics import add, multiply, divide # type: ignore


# --- Test functions ---

def test_add():
    """Test the add() function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    """Test the multiply() function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6


def test_divide():
    """Test the divide() function, including division by zero."""
    assert divide(6, 3) == 2
    # Check that dividing by zero raises a ValueError
    import pytest
    with pytest.raises(ValueError):
        divide(1, 0)
