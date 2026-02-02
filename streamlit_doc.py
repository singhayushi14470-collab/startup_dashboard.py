import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
df=pd.read_csv("startup_cleaned.csv")

def load_investor_details(investors):
    st.title(investors)
    # load the recent 5 investment of the investors
    #recent investors
    df["invertors"].fillna(False)
    last5_df=df[df['invertors'].str.contains(investors, na=False)].head()[["date", "startup", "vertical", "location", "round", "amount"]]
    st.subheader("Most Recent Investments")
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
        #biggest investments
        big_series=df[df['invertors'].str.contains(investors, na=False)].groupby("startup")["amount"].sum().sort_values(ascending=False).head()
        st.subheader("biggest Investments")
        fig,ax=plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

st.sidebar.title("Startup Funding Analysis")

option=st.sidebar.selectbox("Select One",["Overall Analysis","Startup","Investor"])

if option=="Overall Analysis":
    st.title("Overall Analysis")
elif option=="Startup":
    st.sidebar.selectbox("Select Startup",sorted(df["invertors"].str.split(",").explode().dropna().unique()))
    btn1=st.sidebar.button("Find startup details")
    st.title("Startup Analysis")

else:
    selected_investor=st.sidebar.selectbox("Select Startup",df["invertors"].explode().tolist())
    btn2=st.sidebar.button("Find investor details")
    if btn2:
        load_investor_details(selected_investor)

