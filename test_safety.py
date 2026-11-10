import pytest
from safety import classify

def test_safe_readings():
    assert classify("chemical_plant", 30, 10, 2, 4) == "SAFE"

def test_warning_readings():
    assert classify("chemical_plant", 60, 10, 2, 4) == "WARNING"

def test_emergency_readings():
    assert classify("chemical_plant", 30, 55, 2, 4) == "EMERGENCY"

def test_combined_warning_triggers_emergency():
    # Chemical plant: temperature warn (60), smoke warn (5) -> Should be EMERGENCY
    assert classify("chemical_plant", 60, 10, 5, 4) == "EMERGENCY"

def test_boiler_room_readings():
    # Boiler room warning level for temperature (90)
    assert classify("boiler_room", 90, 10, 2, 5) == "WARNING"

def test_negative_values_raise_error():
    with pytest.raises(ValueError):
        classify("chemical_plant", -10, 10, 2, 4)