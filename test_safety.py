import pytest
from safety import classify

@pytest.mark.parametrize("env, t, g, s, p, expected", [
    ("chemical_plant", 30, 5, 1, 4, "SAFE"),
    ("chemical_plant", 60, 5, 1, 4, "WARNING"),      # boundary: exactly warning limit
    ("chemical_plant", 30, 55, 1, 4, "EMERGENCY"),
    ("chemical_plant", 60, 5, 5, 4, "EMERGENCY"),    # fire rule: temp + smoke both warning
    ("chemical_plant", 30, 5, 5, 4, "WARNING"),      # smoke only, no fire rule
    ("boiler_room",    80, 5, 1, 6, "SAFE"),
    ("boiler_room",    100, 5, 1, 6, "WARNING"),
    ("boiler_room",    125, 5, 1, 6, "EMERGENCY"),
])
def test_classify(env, t, g, s, p, expected):
    assert classify(env, t, g, s, p) == expected

@pytest.mark.parametrize("env", ["chemical_plant", "boiler_room"])
def test_negative_reading_rejected(env):
    with pytest.raises(ValueError):
        classify(env, 30, -5, 1, 4)