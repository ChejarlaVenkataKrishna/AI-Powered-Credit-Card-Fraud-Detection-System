import joblib
import pandas as pd
import streamlit as st

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction APP")
st.markdown("please enter the transcation details and use the predict button")
st.divider()

import time

progress = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

transcation_type = st.selectbox("Transcation Type",["PAYMENT","TRANSFER","CASH_OUT"])
amount = st.number_input("Amount",min_value = 0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value = 0.0, value = 10000.0)
newbalanceOrig= st.number_input("New Balance (Sender)", min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value = 0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance (receiver)", min_value = 0.0, value = 0.0)

if st.button("Predict"):
    with st.spinner("Analyzing transaction..."):
        time.sleep(2)
    input_data = pd.DataFrame([{
        "type" : transcation_type,
        "amount" : amount,
        "oldbalanceOrg" : oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest" : newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("🔴This transcation can be fraud")
    else:
        st.success("🟢This transcation looks like it is not fraud")
        
        placeholder = st.empty()

    # Show blinking tick
        placeholder.markdown("""<style>
        @keyframes blink {
            0% {opacity: 1;}
            50% {opacity: 0;}
            100% {opacity: 1;}
        }
        .blink {
            animation: blink 1s infinite;
            text-align: center;
        }
        </style>

        <div class="blink">
            <h1 style="color:green; font-size:80px;">✔️</h1>
            <h2 style="color:green;">Transaction is Safe</h2>
        </div>
    """, unsafe_allow_html=True)

    # Keep blinking for 5 seconds
        

    # Replace with static success message
        placeholder.markdown("""
            <div style="text-align:center;">
                <h1 style="color:green;">✔️</h1>
                <h2 style="color:green;">Transaction is Safe</h2>
            </div>
        """, unsafe_allow_html=True)
        st.snow()
                
        
