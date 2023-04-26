import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('final.pkl', 'rb'))

st.title('Will the person get a heart attack or not')

age= st.slider("age", 29,77)
sex= st.slider("sex", 0,1)
cp= st.slider("Chest Pain", 0,3)
fbs= st.slider("fasting blood sugar", 0,1)
restecg=st.slider("Resting electrocardiographic results", 0,2)
thalachh=st.slider("Maximum heart rate achieved", 71,202)
exng=st.slider("Exercise induced angina", 0,1)
oldpeak=st.slider("Previous peak", 0,2)
caa=st.slider("Number of major vessels", 0,4)
thall=st.slider("Thal rate", 0,3)







def predict():
    float_features = [float(x) for x in [age , sex, cp, fbs, restecg, thalachh, exng, oldpeak, caa, thall]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)


    if(int(label)==1):
        st.success('The person will get a heart attack ')
    else:
        st.success('The person will not get a heart attack ')

trigger = st.button('Predict', on_click=predict)
