import pandas as pd
import streamlit as st
import numpy as np

from model import ensemble_model

st.title("🔧 Machine Failure Risk Prediction")
st.write("Please enter the machine sensor data below:")

# Tạo 2 cột
col1, col2 = st.columns(2)

with col1:
    temperature = st.text_input("Temperature (°C)", value="25.0")
    vibration = st.text_input("Vibration (Hz)", value="49.0")

with col2:
    humidity = st.text_input("Humidity (%)", value="50.0")
    power_usage = st.text_input("Power Usage (kW)", value="15.0")

# Chuyển đổi và kiểm tra giá trị
def safe_float(input_str, field_name):
    try:
        return float(input_str)
    except (ValueError, TypeError):
        st.error(f"Invalid input for {field_name}: '{input_str}' is not a number.")
        return None

if st.button("Predict"):
    temp = safe_float(temperature, "Temperature")
    hum = safe_float(humidity, "Humidity")
    vib = safe_float(vibration, "Vibration")
    pw = safe_float(power_usage, "Power Usage")

    if all(v is not None for v in [temp, hum, vib, pw]):
        # Chuyển thành list theo thứ tự [temp, vibrate, pw_use, humid]
        input_array = [[temp, vib, pw, hum]]  # shape (1, 4)

        # Gọi model ensemble ở đây
        try:
            result = ensemble_model(input_array)
            prediction = result[0]
            result_map = {0: "✅ Normal", 1: "⚠️ Failure Risk"}
            if prediction == 0:
                st.markdown(
                    """
                    <div style="background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; border: 1px solid #c3e6cb; font-size: 18px;">
                    ✅ <strong>Prediction:</strong> Normal
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div style="background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; border: 1px solid #f5c6cb; font-size: 18px;">
                    ⚠️ <strong>Prediction:</strong> Failure Risk
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        except Exception as e:
            st.error(f"Error during prediction: {e}")