
import pytest
from src.math_lib import calculate_mean, calculate_std

def test_mean():
    assert calculate_mean([1, 2, 3, 4, 5]) == 3.0

def test_std():
    # Standard deviation of [1,2,3] is approx 0.816
    assert abs(calculate_std([1, 2, 3]) - 0.81649658) < 0.0001
