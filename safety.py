LIMITS = {
    "chemical_plant": {
        "temperature": (60, 80), 
        "gas": (25, 50),
        "smoke": (5, 15), 
        "pressure": (8, 10),
    },
    "boiler_room": {
        "temperature": (90, 120), 
        "gas": (20, 40),
        "smoke": (5, 12), 
        "pressure": (10, 15),
    },
}

def classify(env, temperature, gas, smoke, pressure):
    readings = {
        "temperature": temperature, 
        "gas": gas,
        "smoke": smoke, 
        "pressure": pressure
    }
    
    for name, value in readings.items():
        if value < 0:
            raise ValueError(f"{name} cannot be negative")
            
    status = "SAFE"
    for name, value in readings.items():
        warn, emergency = LIMITS[env][name]
        if value >= emergency:
            return "EMERGENCY"
        if value >= warn:
            status = "WARNING"
            
    return status  