import streamlit as st
import pickle

with open("Diabetes_model.pkl", 'rb') as model_file:
    diabetes = pickle.load(model_file)

# Set page configurations
st.set_page_config(
    page_title="Griya;s First ML Web App",
    page_icon=":clipboard:",
    layout="wide",
)

def predict_diabetes_risk(age, BMI, FPG, FFPG, SBP, DBP, family_history, smoking, drinking, ALT):
    try:
        # Convert input values to appropriate types
        age = int(age)
        BMI = float(BMI)
        FPG = float(FPG)
        FFPG = float(FFPG)
        SBP = float(SBP)
        DBP = float(DBP)
        family_history = int(family_history)
        smoking = float(smoking)
        drinking = float(drinking)
        ALT = int(ALT)

        input_values = [age, BMI, FPG, FFPG, SBP, DBP, family_history, smoking, drinking, ALT]
        # Replace the next line with your prediction function/method
        prediction = diabetes.predict([input_values])

        return prediction[0]  # Return the first element as a scalar
    except ValueError as e:
        return "Invalid input. Please provide valid numeric values for all input fields."

def main():
    st.title("Griya's First ML Web App")

    # Sidebar for navigation
    selected = st.sidebar.selectbox(
        "AROGYA VICHARANA",
        ['Diabetes Prediction'],
    )

    if selected == "Diabetes Prediction":
        st.header("Diabetes Prediction")
        
        # Create three columns
        col1, col2, col3 = st.columns(3)

        # Input elements for col1
        age = col1.number_input("Age", min_value=0, max_value=100, key="age")
        BMI = col1.number_input("BMI", min_value=10.0, max_value=40.0, key="BMI", placeholder="Type Here",help="Body Mass Index")
        FPG = col1.number_input("FPG", min_value=0.0, max_value=200.0, key="FPG", placeholder="Type Here",help="Fasting Plasma Glucose")
        FFPG = col2.number_input("FFPG", min_value=0.0, max_value=200.0, key="FFPG", placeholder="Type Here",help="Fasting and Postprandial Plasma Glucose")
        SBP = col2.number_input("SBP", min_value=80, max_value=180, key="SBP", placeholder="Type Here",help="Systolic Blood Pressure",)
        DBP = col2.number_input("DBP", min_value=50, max_value=120, key="DBP", placeholder="Type Here",help="Diastolic Blood Pressure")

        # Input elements for col2
        family_history = col2.number_input("Family History", min_value=0.0, max_value=5.0, key="family_history", placeholder="Type Here")
        smoking = col3.number_input("Smoking", min_value=0.0, max_value=7.0, key="smoking", placeholder="Type Here")
        drinking = col3.number_input("Drinking", min_value=0.0, max_value=7.0, key="drinking", placeholder="Type Here")
        ALT = col3.number_input("ALT", min_value=0.0, max_value=100.0, key="ALT", placeholder="Type Here",help="Alanine Transaminase")


        result = ""
        if st.button("Predict"):
            result = predict_diabetes_risk(age, BMI, FPG, FFPG, SBP, DBP, family_history, smoking, drinking, ALT)

        if result == 0:
            st.success('No Diabetes, you are safe')
        elif result == 1:
            st.error('Yes, you have Diabetes. Please consult a doctor')
        else:
            st.warning('Enter valid input values')

if __name__ == '__main__':
     main()