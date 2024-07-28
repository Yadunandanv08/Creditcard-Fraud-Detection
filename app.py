import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

st.title("Credit Card Fraud Detection Model")
input_df= st.text_input("Enter Features")
input_df_splited = input_df.split(",")

submit = st.button("Submit")

if submit:
    features = np.asarray(input_df_splited, dtype=np.float64)
    prediction = loaded_model.predict(features.reshape(1, -1))

    if prediction[0] == 0:
        st.write("Legitimate Transaction")

    else:    
        st.write("Fraudulent Transaction")
    
