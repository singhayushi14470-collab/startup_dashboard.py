import streamlit as st

st.title("Startup Dashboard")
st.header("I Am learning streamlit")
st.subheader("And I Am loving family")

st.write("i am writing streamlit app")

st.markdown("""
### My favorite app
- race 2
- race 3
- race 4
""")

st.code("""
def foo(input):
   return foo**2
""")

# latex
st.latex("x^2+y^2=0")

# display element
import pandas as pd
df=pd.DataFrame({
    "name":["ayushi","sheetal","Aditi"],
    "marks":[50,60,70],
    "package":[10,12,14]
})
st.dataframe(df)
st.metric("Revenue","Rs 3 lacks","3")
st.json({
"name":["ayushi","sheetal","Aditi"],
    "marks":[50,60,70],
    "package":[10,12,14]
})
st.image('ak.jpg')
st.video('task.mp4')

st.sidebar.title("title of sidebar")

# columns
col1,col2=st.columns(2)
with col1:
    st.image('ak.jpg')
with col2:
    st.image('ak.jpg')

st.error("login fail")
st.success("login success")
st.warning("warning")

# prograss
import time
bar=st.progress(0)

#for i in range(1,101):
    #time.sleep(0.1)
    #bar.progress(i)

# taking user input
email=st.text_input("enter email.")
no=st.number_input("enter no.")
date=st.date_input("enter date")

emal=st.text_input("enter email")
password=st.text_input("enter password")
st.selectbox("select gender",["male","female","other"])
btn=st.button("login karo")
if btn:
    if emal == "ayushi@gmail.com" and password == "1234":
        st.balloons()
        st.write(gender)
    else:
        st.error("login fail")

file = st.file_uploader("Upload your file")

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())