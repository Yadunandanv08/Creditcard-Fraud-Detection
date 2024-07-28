import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import streamlit as st

#loading dataset
credit_data = pd.read_csv('creditcard.csv')


#separating data for analysis
legit = credit_data[credit_data.Class == 0]
fraud = credit_data[credit_data.Class == 1]


legit_sample = legit.sample(n=492)
new_dataset = pd.concat([legit_sample, fraud], axis=0)


x=new_dataset.drop(columns='Class', axis=1)
y=new_dataset['Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=2)

model = LogisticRegression(solver='liblinear')

#training the model

model.fit(x_train, y_train)
     
LogisticRegression(solver='liblinear')

#evaluation

x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)
training_data_precision = precision_score(x_train_prediction, y_train)
training_data_recall = recall_score(x_train_prediction, y_train)
training_data_f1 = f1_score(x_train_prediction, y_train)
     
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)
test_data_precision = precision_score(y_test, x_test_prediction)
test_data_recall = recall_score(x_test_prediction, y_test)
test_data_f1 = f1_score(x_test_prediction, y_test)


#streamlit app

st.title("Credit Card Fraud Detection Model")
input_df= st.text_input("Enter Features")
input_df_splited = input_df.split(",")

submit = st.button("Submit")

if submit:
    features = np.asarray(input_df_splited, dtype=np.float64)
    prediction = model.predict(features.reshape(1, -1))

    if prediction[0] == 0:
        st.write("Legitimate Transaction")

    else:    
        st.write("Fraudulent Transaction")
    


