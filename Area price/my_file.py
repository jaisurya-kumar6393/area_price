import pickle
import streamlit as st
model1=pickle.load(open("areaprice.pkl","rb"))
def mydeploy():
    st.title("AreaPrice prediction")
    area=st.number_input("enter your area")
    pred=st.button("predict")
    if pred:
        x=model1.predict([[area]])
        st.write(x[0])
mydeploy()