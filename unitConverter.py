import streamlit as st

def convert_units(category, value, from_unit, to_unit):
    conversion_factors = {
        "Length": {
            "Kilometre": 1000, "Metre": 1, "Centimetre": 0.01, "Millimetre": 0.001,
            "Micrometre": 1e-6, "Nanometre": 1e-9, "Mile": 1609.34, "Yard": 0.9144,
            "Foot": 0.3048, "Inch": 0.0254, "Nautical mile": 1852
        },
        "Mass": {
            "Kilogram": 1, "Gram": 0.001, "Milligram": 1e-6, "Microgram": 1e-9,
            "Pound": 0.453592, "Ounce": 0.0283495, "Ton": 1000
        },
        "Temperature": {
            "Celsius": lambda x: x, "Fahrenheit": lambda x: (x - 32) * 5/9,
            "Kelvin": lambda x: x - 273.15
        },
        "Speed": {
            "Metre per second": 1, "Kilometre per hour": 0.277778,
            "Mile per hour": 0.44704, "Foot per second": 0.3048
        }
    }
    
    if category in ["Temperature"]:
        return conversion_factors[category][to_unit](conversion_factors[category][from_unit](value))
    else:
        return value * (conversion_factors[category][from_unit] / conversion_factors[category][to_unit])

st.title("Unit Converter App")
st.markdown("### Converts Various Units Instantly")

category = st.selectbox("Choose a category", ["Length", "Mass", "Temperature", "Speed"])

units = {
    "Length": ["Kilometre", "Metre", "Centimetre", "Millimetre", "Micrometre", "Nanometre", "Mile", "Yard", "Foot", "Inch", "Nautical mile"],
    "Mass": ["Kilogram", "Gram", "Milligram", "Microgram", "Pound", "Ounce", "Ton"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Speed": ["Metre per second", "Kilometre per hour", "Mile per hour", "Foot per second"]
}

from_unit = st.selectbox("Select From Unit", units[category])
to_unit = st.selectbox("Select To Unit", units[category])
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.6f")

if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
