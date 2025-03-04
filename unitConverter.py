import streamlit as st

st.title("Unit Converter App")
st.markdown("### Converts Various Units Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("Choose a category", [
    "Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy",
    "Length", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"
])

length_units = ["Kilometre", "Metre", "Centimetre", "Millimetre", "Micrometre", "Nanometre", "Mile", "Yard", "Foot", "Inch", "Nautical mile"]

def convert_units(category, value, from_unit, to_unit):
    if category == "Length":
        conversions = {
            "Kilometre": 1000,
            "Metre": 1,
            "Centimetre": 0.01,
            "Millimetre": 0.001,
            "Micrometre": 1e-6,
            "Nanometre": 1e-9,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254,
            "Nautical mile": 1852
        }
        return value * (conversions[from_unit] / conversions[to_unit])
    return None

if category == "Length":
    from_unit = st.selectbox("Select From Unit", length_units)
    to_unit = st.selectbox("Select To Unit", length_units)
    value = st.number_input("Enter the value to convert", min_value=0.0, format="%.6f")
    if st.button("Convert"):
        result = convert_units(category, value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
else:
    st.write("Unit conversions for other categories will be added soon.")
