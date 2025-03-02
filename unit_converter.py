import streamlit as st
import requests

# Custom CSS 
st.markdown("""
    <style>
        /* Main background with a light gradient */
        .stApp { 
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2) !important;
        }
        /* Left sidebar background with the same light gradient */
        [data-testid="stSidebar"] > div:first-child {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2) !important;
        }
        /* Top header/navbar background with the same light gradient */
        [data-testid="stHeader"] {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2) !important;
        }
        /* Top header text styling: Dark text for light background */
        h1, h2 {
            color: #2d3436;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 3px;
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
        }
        /* Conversion result message styling override */
        div[role="alert"] {
            background-color: #2d3436 !important;
            color: #ffffff !important;
            font-weight: bold;
        }
        /* Button styling */
        .stButton>button {
            background: linear-gradient(135deg, #74b9ff 0%, #a29bfe 100%);
            color: white;
            border-radius: 20px;
            padding: 12px 25px;
            font-weight: bold;
            box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.2);
            transition: 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.1);
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.3);
        }
        /* Select box styling */
        .stSelectbox>div>div {
            background: #ffffff;
            border: 3px solid #2d3436;
            border-radius: 12px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            transition: 0.3s ease;
        }
        .stSelectbox>div>div:hover {
            transform: scale(1.05);
            border-color: #636e72;
        }
        /* Sidebar collapse arrow styling for better visibility */
        [data-testid="stSidebarCollapseButton"] svg {
            fill: #2d3436 !important;
        }
        /* Responsive adjustments for extra small screens */
        @media only screen and (max-width: 600px) {
            h1, h2 {
                font-size: 1.5rem;
                letter-spacing: 1px;
                padding: 5px;
            }
            .stButton>button {
                padding: 10px 20px;
                font-size: 0.9rem;
            }
            [data-testid="stSidebar"] > div:first-child, [data-testid="stHeader"] {
                padding: 10px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit Page Title 
st.title("🔄 Unit Convertor")

# Sidebar for navigation
st.sidebar.title("🔍 Unit Categories")
unit_type = st.sidebar.selectbox("Select Category", [
    "Currency", "Length", "Weight", "Temperature"
])

# Currency Conversion
if unit_type == "Currency":
    st.header("💰 Currency Conversion")
    from_currency = st.selectbox("From Currency", ["USD", "PKR", "EUR", "GBP", "INR"])
    to_currency = st.selectbox("To Currency", ["USD", "PKR", "EUR", "GBP", "INR"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")

    if st.button("Convert"):
        try:
            api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(api_url)
            data = response.json()
            rate = data['rates'][to_currency]
            result = amount * rate
            st.success(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
        except:
            st.error("❌ Error in fetching currency rates.")

# Length Conversion
elif unit_type == "Length":
    st.header("📏 Length Conversion")
    length_units = {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.37, "Feet": 3.281}
    from_unit = st.selectbox("From Unit", list(length_units.keys()))
    to_unit = st.selectbox("To Unit", list(length_units.keys()))
    value = st.number_input("Value", min_value=0.0)

    if st.button("Convert"):
        result = value * (length_units[to_unit] / length_units[from_unit])
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

# Weight Conversion
elif unit_type == "Weight":
    st.header("⚖️ Weight Conversion")
    weight_units = {"Kilogram": 1, "Gram": 1000, "Pound": 2.205, "Ounce": 35.274}
    from_unit = st.selectbox("From Unit", list(weight_units.keys()))
    to_unit = st.selectbox("To Unit", list(weight_units.keys()))
    value = st.number_input("Value", min_value=0.0)

    if st.button("Convert"):
        result = value * (weight_units[to_unit] / weight_units[from_unit])
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

# Temperature Conversion
elif unit_type == "Temperature":
    st.header("🌡️ Temperature Conversion")
    temp_units = ["Celsius", "Fahrenheit"]
    from_unit = st.selectbox("From Unit", temp_units)
    to_unit = st.selectbox("To Unit", temp_units)
    value = st.number_input("Value", min_value=-273.15)

    if st.button("Convert"):
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        else:
            result = value
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

# Footer
st.markdown("---")
