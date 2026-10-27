import pytest
from app import calculate_average

def test_average_ok():
    assert calculate_average([10, 20, 30]) == 20

def test_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
