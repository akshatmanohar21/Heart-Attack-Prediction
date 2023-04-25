import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('final.pkl', 'rb'))

st.title('Will the person get a heart attack or not')

age= st.slider("age")
sex= st.slider("sex")
cp= st.slider("Chest Pain")
fbs= st.slider("fasting blood sugar")
restecg=st.slider("Resting electrocardiographic results")
thalachh=st.slider("Maximum heart rate achieved")
exng=st.slider("Exercise induced angina")
oldpeak=st.slider("Previous peak")
caa=st.slider("Number of major vessels")
thall=st.slider("Thal rate")







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