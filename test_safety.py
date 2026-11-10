import pytest
from safety import classify

def test_safe_readings():
    # Chemical plant normal readings
    assert classify("chemical_plant", 30, 10, 2, 4) == "SAFE"

def test_warning_readings():
    # Temperature at warning level (60 is warn for chemical_plant)
    assert classify("chemical_plant", 60, 10, 2, 4) == "WARNING"

def test_emergency_readings():
    # Gas at emergency level (55 >= 50 emergency limit)
    assert classify("chemical_plant", 30, 55, 2, 4) == "EMERGENCY"

def test_negative_values_raise_error():
    with pytest.raises(ValueError):
        classify("chemical_plant", -10, 10, 2, 4)