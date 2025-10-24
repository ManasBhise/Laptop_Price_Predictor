import streamlit as st
import pickle
import numpy as np

# Load model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# App title
st.title("💻 Laptop Price Predictor")

# Inputs
company = st.selectbox('Brand', df['Company'].unique())
type = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input('Weight of the laptop')
touchscreen = st.selectbox("Touchscreen", ['No', 'Yes'])
ips = st.selectbox("IPS", ['No', 'Yes'])
screen_size = st.number_input('Screen Size (in inches)')
resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080', '1366x768', '1600x900', '3840x2160',
     '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440']
)
cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())
os = st.selectbox('Operating System', df['os'].unique())

# Prediction
if st.button("Predict Price"):
    # Convert categorical to numeric
    touchscreen = 1 if touchscreen == "Yes" else 0
    ips = 1 if ips == "Yes" else 0

    # Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / float(screen_size)

    # Prepare input
    query = np.array([[company, type, ram, float(weight),
                       touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]])

    # Prediction
    predicted_price = int(np.exp(pipe.predict(query)[0]))
    st.success(f"The predicted price of this configuration is ₹{predicted_price:,}")
