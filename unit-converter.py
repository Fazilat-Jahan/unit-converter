import streamlit as st

def convert_units(category, value, unit_from, unit_to):
    conversions = {  
    "Time": {
        "second_minute": 1/60, "minute_second": 60,
        "second_hour": 1/3600, "hour_second": 3600,
        "second_day": 1/86400, "day_second": 86400,
        "second_week": 1/604800, "week_second": 604800,
        "second_month": 1/2629746, "month_second": 2629746,
        "second_year": 1/31556952, "year_second": 31556952,

        "minute_hour": 1/60, "hour_minute": 60,
        "minute_day": 1/1440, "day_minute": 1440,
        "minute_week": 1/10080, "week_minute": 10080,
        "minute_month": 1/43829, "month_minute": 43829,
        "minute_year": 1/525949, "year_minute": 525949,

        "hour_day": 1/24, "day_hour": 24,
        "hour_week": 1/168, "week_hour": 168,
        "hour_month": 1/730, "month_hour": 730,
        "hour_year": 1/8760, "year_hour": 8760,

        "day_week": 1/7, "week_day": 7,
        "day_month": 1/30.44, "month_day": 30.44,
        "day_year": 1/365.24, "year_day": 365.24,

        "week_month": 1/4.345, "month_week": 4.345,
        "week_year": 1/52.178, "year_week": 52.178,

        "month_year": 1/12, "year_month": 12
    },
    "Length": {
        "meter_kilometer": 0.001, "kilometer_meter": 1000,
        "meter_centimeter": 100, "centimeter_meter": 0.01,
        "meter_millimeter": 1000, "millimeter_meter": 0.001,
        "meter_mile": 0.000621371, "mile_meter": 1609.344,
        "meter_foot": 3.28084, "foot_meter": 0.3048,
        "meter_inch": 39.3701, "inch_meter": 0.0254,
        "kilometer_mile": 0.621371, "mile_kilometer": 1.60934,
        "kilometer_foot": 3280.84, "foot_kilometer": 0.0003048,
        "kilometer_inch": 39370.1, "inch_kilometer": 0.0000254,
        "mile_foot": 5280, "foot_mile": 0.000189394,
        "mile_inch": 63360, "inch_mile": 0.0000157828,
        "foot_inch": 12, "inch_foot": 0.0833333
    },
    "Weight": {
        "gram_kilogram": 0.001, "kilogram_gram": 1000,
        "gram_milligram": 1000, "milligram_gram": 0.001,
        "gram_pound": 0.00220462, "pound_gram": 453.592,
        "gram_ounce": 0.03527396, "ounce_gram": 28.3495,
        "kilogram_milligram": 1e6, "milligram_kilogram": 1e-6,
        "kilogram_pound": 2.20462, "pound_kilogram": 0.453592,
        "kilogram_ounce": 35.274, "ounce_kilogram": 0.0283495,
        "pound_ounce": 16, "ounce_pound": 0.0625,
        "pound_milligram": 453592, "milligram_pound": 2.20462e-6
    },
    "Volume": {
        "liter_milliliter": 1000, "milliliter_liter": 0.001,
        "liter_gallon": 0.264172, "gallon_liter": 3.78541,
        "liter_cubic_meter": 0.001, "cubic_meter_liter": 1000,
        "liter_cubic_feet": 0.0353147, "cubic_feet_liter": 28.3168,
        "milliliter_gallon": 0.000264172, "gallon_milliliter": 3785.41,
        "milliliter_cubic_meter": 1e-6, "cubic_meter_milliliter": 1e6,
        "milliliter_cubic_feet": 3.53147e-5, "cubic_feet_milliliter": 28316.8,
        "gallon_cubic_feet": 0.133681, "cubic_feet_gallon": 7.48052
    },
    "Area": {
        "square_meter_square_kilometer": 1e-6, "square_kilometer_square_meter": 1e6,
        "square_meter_square_centimeter": 10000, "square_centimeter_square_meter": 0.0001,
        "square_meter_square_foot": 10.7639, "square_foot_square_meter": 0.092903,
        "square_meter_square_inch": 1550, "square_inch_square_meter": 0.00064516,
        "square_kilometer_acre": 247.105, "acre_square_kilometer": 0.00404686,
        "square_kilometer_square_foot": 1.076e7, "square_foot_square_kilometer": 9.29e-8,
        "square_kilometer_square_inch": 1.55e9, "square_inch_square_kilometer": 6.45e-10,
        "acre_square_meter": 4046.86, "square_meter_acre": 0.000247105,
        "acre_square_foot": 43560, "square_foot_acre": 2.2957e-5,
        "acre_square_inch": 6.273e6, "square_inch_acre": 1.5942e-7
    },
    "Speed": {
        "meter_per_second_kilometer_per_hour": 3.6, "kilometer_per_hour_meter_per_second": 0.277778,
        "meter_per_second_mile_per_hour": 2.23694, "mile_per_hour_meter_per_second": 0.44704,
        "meter_per_second_foot_per_second": 3.28084, "foot_per_second_meter_per_second": 0.3048,
        "kilometer_per_hour_mile_per_hour": 0.621371, "mile_per_hour_kilometer_per_hour": 1.60934,
        "kilometer_per_hour_foot_per_second": 0.911344, "foot_per_second_kilometer_per_hour": 1.09728,
        "mile_per_hour_foot_per_second": 1.46667, "foot_per_second_mile_per_hour": 0.681818
    },
    "Pressure": {
        "pascal_bar": 1e-5, "bar_pascal": 1e5,
        "pascal_atmosphere": 9.86923e-6, "atmosphere_pascal": 101325,
        "pascal_psi": 0.000145038, "psi_pascal": 6894.76,
        "bar_atmosphere": 0.986923, "atmosphere_bar": 1.01325,
        "bar_psi": 14.5038, "psi_bar": 0.0689476,
        "atmosphere_psi": 14.6959, "psi_atmosphere": 0.068046
    },
    "Energy": {
        "joule_kilojoule": 0.001, "kilojoule_joule": 1000,
        "joule_calorie": 0.239006, "calorie_joule": 4.184,
        "joule_kilocalorie": 0.000239006, "kilocalorie_joule": 4184,
        "joule_watt_hour": 0.000277778, "watt_hour_joule": 3600,
        "kilojoule_calorie": 239.006, "calorie_kilojoule": 0.004184,
        "kilojoule_kilocalorie": 0.239006, "kilocalorie_kilojoule": 4.184,
        "calorie_kilocalorie": 0.001, "kilocalorie_calorie": 1000
    },

    
    }


    key = f"{unit_from}_{unit_to}"
    if key in conversions[category]:
        conversion = conversions[category][key]
        return value * conversion
    else:
        return "Conversion not available, Please select right units"


st.title("Unit Converter")
category = st.selectbox("Select Category", [ "Time", "Length", "Weight", "Volume", "Area", "Speed", "Pressure", "Energy",])

units = {
    "Length": ["meter", "kilometer", "mile", "foot"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Volume": ["liter", "milliliter", "gallon", "cubic_feet"],
    "Area": ["square_meter", "square_kilometer", "square_foot", "square_inch", "acre"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour", "foot_per_second"],
    "Pressure": ["pascal", "bar", "atmosphere", "psi"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour"],
    "Time": ["second", "minute", "hour", "day", "week", "month"],
}

value = st.number_input("Enter the value", min_value=1.0, step=1.0) 

unit_from = st.selectbox("convert from", units[category])

unit_to = st.selectbox("convert to", units[category])

if st.button("Get Result"):
    result = convert_units(category, value, unit_from, unit_to)
    # st.write(f"{value} {unit_from} is equal to {result} {unit_to}")
    st.success(f" Converted: {result} : {unit_to}")



footer = """
    <style>
        .footer {
            position: fixed;
            bottom: 10px;
            left: 20px;
            font-size: 14px;
            color: gray;
        }
    </style>
    <div class="footer">
        Built by <a href="https://www.linkedin.com/in/fazilat-jahan-web-developer/"> <b>Fazilat Jahan</b> </a>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)