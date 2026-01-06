LENGTH_FACTORS = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1.0,
    "kilometer": 1000.0,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}
WEIGHT_FACTORS = {
    "milligram": 0.001,
    "gram": 1.0,
    "kilogram": 1000.0,
    "ounce": 28.349523125,
    "pound": 453.59237,
}

def convert_length(value, from_unit, to_unit):
    meters = value * LENGTH_FACTORS[from_unit]
    return meters / LENGTH_FACTORS[to_unit]


def convert_weight(value,from_unit,to_unit):
    grams = value * WEIGHT_FACTORS[from_unit]
    return grams / WEIGHT_FACTORS[to_unit]


def convert_temperature(value, from_unit, to_unit):
    # Step 1: convert everything to celsius

    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError("Invalid temperature unit")
   
   # Step 2: convert from Celsius to target

    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return (celsius * 9 / 5) + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:
        raise ValueError("Invalid temperature unit")