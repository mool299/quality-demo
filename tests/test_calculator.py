"""Unit tests for calculator module."""
import sys
import os

# Добавляем корневую папку проекта в путь поиска модулей
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import add, subtract

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5

def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 2) == 3
