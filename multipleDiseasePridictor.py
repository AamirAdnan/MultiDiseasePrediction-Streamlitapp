import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model


diabeties_model=pickle.load(open("C:/Users/amira/Downloads/Regression and classification problem(Supervised learning/Dibetese_pridictor Model/diabeties_model.sav",'rb'))
breast_model=pickle.load(open("C:/Users/amira/Downloads/Regression and classification problem(Supervised learning/mULTI disease predictor/breast_model.pkl",'rb'))
heart_model=pickle.load(open("C:/Users/amira/Downloads/Regression and classification problem(Supervised learning/machine learning model/heart_model.sav",'rb'))

#slidebar for navigation
with st.sidebar:
    selected=option_menu('Multiple disease Prediction System',
                        ['Diabetes Prediction',
                        'Heart Disease Prediction',
                        'Breast Cancer Prediction'],
                        icons=['Activity','Heart fill','Lungs'],default_index=1)
# diabeties prediction page
if(selected=='Diabetes Prediction'):
    #page title
    st.title('Diabeties prediction Useing ML')
    #getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    # For the prediction Part
    diabeties_dig = ''

    #button for prediction
    if st.button('Diabetes Test Result'):
        userinput = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction, Age] 
        userinput = [float(x) for x in userinput]
        diabeties_prediction = diabeties_model.predict([userinput])
        
        if(diabeties_prediction[0]==1):
            diabeties_dig='The Person is having Diabeties'
        else:
            diabeties_dig='The Person is not having Diabeties'
    st.success(diabeties_dig)
        
#--------------------------------------------------------------------------------------------------------------------------------
    

if(selected=='Heart Disease Prediction'):
    st.title("Heart disease prediction useing ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
#---------------------------------------------------------------------------------------------------------------------------------------------

if selected == 'Breast Cancer Prediction':
    st.title("Breast Cancer Prediction using ML")

    input_fields = [
        ('Radius Mean', 'radius_mean'),
        ('Texture Mean', 'texture_mean'),
        ('Perimeter Mean', 'perimeter_mean'),
        ('Area Mean', 'area_mean'),
        ('Smoothness Mean', 'smoothness_mean'),
        ('Compactness Mean', 'compactness_mean'),
        ('Concavity Mean', 'concavity_mean'),
        ('Concave Points Mean', 'concave_points_mean'),
        ('Symmetry Mean', 'symmetry_mean'),
        ('Fractal Dimension Mean', 'fractal_dimension_mean'),
        ('Radius SE', 'radius_se'),
        ('Texture SE', 'texture_se'),
        ('Perimeter SE', 'perimeter_se'),
        ('Area SE', 'area_se'),
        ('Smoothness SE', 'smoothness_se'),
        ('Compactness SE', 'compactness_se'),
        ('Concavity SE', 'concavity_se'),
        ('Concave Points SE', 'concave_points_se'),
        ('Symmetry SE', 'symmetry_se'),
        ('Fractal Dimension SE', 'fractal_dimension_se'),
        ('Radius Worst', 'radius_worst'),
        ('Texture Worst', 'texture_worst'),
        ('Perimeter Worst', 'perimeter_worst'),
        ('Area Worst', 'area_worst'),
        ('Smoothness Worst', 'smoothness_worst'),
        ('Compactness Worst', 'compactness_worst'),
        ('Concavity Worst', 'concavity_worst'),
        ('Concave Points Worst', 'concave_points_worst'),
        ('Symmetry Worst', 'symmetry_worst'),
        ('Fractal Dimension Worst', 'fractal_dimension_worst')
    ]

    # Create columns for input fields
    cols = st.columns(5)

    # Store user input values in a dictionary
    user_inputs = {}

    for i, (label, field_id) in enumerate(input_fields):
        with cols[i % 5]:
            user_inputs[field_id] = st.text_input(label, key=field_id)

    # creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        # Convert user inputs to floats and prepare for prediction
        input_values = [float(user_inputs[field_id]) for _, field_id in input_fields]

        # Perform prediction using the model
        cancer_prediction = breast_model.predict([input_values])

        if cancer_prediction[0] == 'M':
            st.success('The person is predicted to have breast cancer.')
        else:
            st.success('The person is predicted not to have breast cancer.')
