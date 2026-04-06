"""Unit tests for calculator module."""
import sys
import os

# Добавляем корневую папку проекта в путь поиска модулей
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import add, subtract, multiply, divide

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 2) == 3
    assert subtract(10, 12) == -2

def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    """Test division function."""
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0

def test_divide_by_zero():
    """Test that division by zero raises ValueError."""
    import pytest
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)