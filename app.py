import streamlit as st
import pickle
import numpy as np
from streamlit_lottie import st_lottie
import requests

model=pickle.load(open('model.pkl','rb'))
st.set_page_config(page_title="Predict Hiring")
def main():
    st.title("Recruitment Revolution-Using Predictive Analytics for Smarter hiring")

    if st.button("Click to enter your Resume Details"):
        st.session_state.page = 'details'
def details():
    name=st.text_input("Enter your Name:")
    age=st.number_input("Enter your Age:",1,100)
    gender=st.selectbox("Select Gender",[None,"Male","Female"])
    edu=st.selectbox("Your Education Level",[None,"Bachelor's (B.E)","Bachelor's (B.Tech)","Master's","PhD"])
    exp=st.number_input("Enter your Experience Years",0,50)  
    pcom=st.number_input("Total Companies Served",0,50)
    dist=st.number_input("Distance from Company (in Kms)",0,1000)
    InterSco=st.number_input("Enter your Interview Score",0,100)  
    SkiSco=st.number_input("Enter your Skill Score",0,100)
    PerSco=st.number_input("Enter your Personality Score",0,100)
    ReqStr=st.selectbox("Select Requirement Strategy",[None,"Aggressive","Moderate","Conservative"])

    eduD={None:0,"Bachelor's (B.E)":1,"Bachelor's (B.Tech)":2,"Master's":3,"PhD":4}
    genD={None:-1,"Male":0,"Female":1}
    ReqD={None:0,"Aggressive":1,"Moderate":2,"Conservative":3}
    EmpDet=np.asarray([age,genD[gender],eduD[edu],exp,pcom,dist,InterSco,SkiSco,PerSco,ReqD[ReqStr]])
    # EmpDet=np.array([26,1,2,0,3,26.783828,48,78,91,1])
    if st.button("Check the Result"):
        st.session_state.det=EmpDet
        st.session_state.name=name 
        st.session_state.page = 'result'

def result():
    
    prediction=model.predict(st.session_state.det)
    if(prediction==1):
        st.header("Congrats {} You are Hired".format(st.session_state.name))
        st_lottie(HirA(),height=400,width=600)
    else:
        st.header("Sorry {} You are NOT Hired".format(st.session_state.name))
        st_lottie(NhirA(),height=400,width=400)
    if st.button("Home Page"):
        st.session_state.page='home'

def animation(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def HirA():
    return animation("https://lottie.host/128a20ed-cf7a-42d6-a49e-351e3b858b19/wghm8rGXJP.json")
def NhirA():
    return animation("https://lottie.host/134035e3-64b5-4419-8e5e-f6d71a6b86e0/1bYV1UR6Bo.json")  

if 'page' not in st.session_state:
    st.session_state.page='home'
    
if st.session_state.page == 'home':
    main()
elif st.session_state.page == 'details':
    details()
elif st.session_state.page == 'result':
    result()


    