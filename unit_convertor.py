import streamlit as st
import pint

# Initialize a unit registry
ureg = pint.UnitRegistry()

# Function to perform unit conversion
def convert_units(value, from_unit, to_unit):
    try:
        # Create the quantity object with the given value and unit
        quantity = value * ureg(from_unit)
        # Convert it to the desired unit
        converted_value = quantity.to(to_unit)
        return converted_value
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit app title
st.title("Google Unit Converter")

# Select units for conversion from a predefined list of units
units = [
    'meter', 'kilometer', 'mile', 'centimeter', 'millimeter', 'yard', 'foot', 'inch',  # Length units
    'gram', 'kilogram', 'pound', 'ounce',  # Mass units
    'second', 'minute', 'hour', 'day', 'week', 'month', 'year',  # Time units
    'celsius', 'fahrenheit', 'kelvin',  # Temperature units
    'liter', 'milliliter', 'gallon', 'quart', 'pint',  # Volume units
    'joule', 'calorie', 'watt',  # Energy units
    'pascal', 'bar', 'atm',  # Pressure units
    'watt', 'kilowatt', 'horsepower',  # Power units
]

# Input fields for the value, from unit, and to unit
value = st.number_input("Enter the value:", value=1.0, step=0.01)
from_unit = st.selectbox("From Unit:", units)
to_unit = st.selectbox("To Unit:", units)

# Convert button to trigger the conversion
if st.button("Convert"):
    # Perform the unit conversion
    result = convert_units(value, from_unit, to_unit)
    
    if result:
        st.write(f"{value} {from_unit} is equal to {result.magnitude:.4f} {to_unit}")

