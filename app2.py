import streamlit as st 
import pandas as pd 
import joblib 

pipeline = joblib.load('best_diabaties_pipeline.pkl')


st.title('DIABETES PREDICTION APP') 


Pregnancies = st.number_input ('Enter the Pregnancies' , min_value =0, max_value = 20 ,value = 0 )
Glucose = st.number_input('Enter Glucose Level' , min_value = 0 , max_value = 300 , value = 120)
BloodPressure = st.number_input ( 'Enter BP Level', min_value = 0 , max_value = 200 , value =120 )
SkinThickness = st.number_input ( 'skin thickness' , min_value= 0 , max_value = 100 , value = 20 ) 
Insulin	= st.number_input ('insulin', min_value=0 , max_value = 900 , value = 80)
BMI = st.number_input ( ' BMI ' , min_value = 0 ,max_value = 100 , value = 25 ) 
DiabetesPedigreeFunction = st.number_input ( 'DiabetesPedigreeFunction' , min_value = 0.0 , max_value =3.0 , value = 0.5 )
Age = st.number_input ('Age' , min_value = 0 , max_value = 120, value = 30 )
Outcome = st.number_input ('Outcome', min_value  = 0 , max_value = 120 , value = 30 ) 




# Predict button
if st.button("Predict"):
    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'Pregnancies':[Pregnancies],
        'Glucose':[Glucose],
        'BloodPressure':[BloodPressure],
        'SkinThickness':[SkinThickness],
        'Insulin':[Insulin],
        'BMI':[BMI],
        'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],
        'Age':[Age]
    })
    
    # Predict using the pipeline
    prediction = pipeline.predict(input_data)[0]
    
    # Show result
    if prediction == 1:
        st.error("The patient is likely Diabetic")
    else:
        st.success("The patient is not Diabetic")
        