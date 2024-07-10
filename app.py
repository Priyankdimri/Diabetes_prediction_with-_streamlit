import streamlit as st  
import pandas as pd
from PIL import  Image
import pickle 

pickel_open=open("KNN.pkl","rb")
KNN=pickle.load(pickel_open)

# def predict_note(gender,age,hypertension,heart_disease,bmi,HbA1c_level,blood_glucose_level):
#     prediction=KNN.predict([[gender,age,hypertension,heart_disease,bmi,HbA1c_level,blood_glucose_level]])
#     return prediction

# def main():
#     st.title("Welcome To Diabities prediction ")
#     gender=st.text_input("gender","Type here")
#     age=st.text_input("age","Type here")
#     hypertension=st.text_input("hypertension","Type here")
#     heart_disease=st.text_input("heart_disease","Type here")
#     bmi=st.text_input("bmi","Type here")
#     HbA1c_level=st.text_input("HbA1c_level","Type here")
#     blood_glucose_level=st.text_input("blood_glucose_level","Type here")
#     result=""
#     if st.button("predict"):
#         result=predict_note(gender,age,hypertension,heart_disease,bmi,HbA1c_level,blood_glucose_level)
#     st.success(f"The Prediction is {result}")
        
    

if __name__ == '__main__':
    main()