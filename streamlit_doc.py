import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide",page_title="Startup Analysis")
df=pd.read_csv("startup_cleaned.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')

df["month"]=df["date"].dt.month
df["year"]=df["date"].dt.year

def load_overall_analysis():
    st.title("Overall Analysis")

# total invested amount
    total=round(df["amount"].sum())
# max amount infused in a startup
    max_funding=df.groupby("startup")["amount"].max().sort_values(ascending=False).head(1).values[0]
# avg ticket size
    avg_funding=df.groupby("startup")["amount"].sum().mean()
# total funded startup
    num_startup=df["startup"].nunique()
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total",str(total)+ "Million")
    with col2:
        st.metric("Max", str(max_funding) + "Million")
    with col3:
        st.metric("Average",str(avg_funding)+ "Million")
    with col4:
        st.metric("Funded Startup",str(num_startup) + "Million")

    st.header("Month on Month graph")
    selected_option=st.selectbox("Select Type",["Total","Count"])
    if selected_option=="Total":
         temp_df = df.groupby(["year", "month"])["amount"].sum().reset_index()
    else:
        temp_df = df.groupby(["year", "month"])["amount"].count().reset_index()

    temp_df["x_axis"]=temp_df["month"].astype("str") + "-" + temp_df["year"].astype("str")

    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df["x_axis"], temp_df["amount"])
    st.pyplot(fig5)


def load_investor_details(investors):
    st.title(investors)
    # load the recent 5 investment of the investors
    #recent investors
    df["invertors"].fillna(False)
    last5_df=df[df['invertors'].str.contains(investors, na=False)].head()[["date", "startup", "vertical", "location", "round", "amount"]]
    st.subheader("Most Recent Investments")
    st.dataframe(last5_df)

    col1,col2,=st.columns(2)
    with col1:
        #biggest investments
        big_series=df[df['invertors'].str.contains(investors, na=False)].groupby("startup")["amount"].sum().sort_values(ascending=False).head()
        st.subheader("biggest Investments")
        fig,ax=plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series=df[df["invertors"].str.contains(investors, na=False)].groupby("vertical")["amount"].sum()
        st.subheader("Sector invested in")
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    col1,col2=st.columns(2)
    with col1:
        round_series=df[df["invertors"].str.contains(investors, na=False)].groupby("round")["amount"].sum()
        st.subheader("Stage invested in")
        fig2, ax2 = plt.subplots()
        ax2.pie(round_series,labels=round_series.index,autopct="%0.01f%%")
        st.pyplot(fig2)

    with col2:
        city_series=df[df["invertors"].str.contains(investors,na=False)].groupby("location")["amount"].sum()
        st.subheader("City invested in")
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series, labels=city_series.index, autopct="%0.01f%%")
        st.pyplot(fig3)

    year_series = df[df["invertors"].str.contains(investors, na=False)].groupby("year")["amount"].sum()

    st.subheader("Year On Year investment")
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)
    st.pyplot(fig4)

st.sidebar.title("Startup Funding Analysis")

option=st.sidebar.selectbox("Select One",["Overall Analysis","Startup","Investor"])

if option=="Overall Analysis":
    load_overall_analysis()

elif option=="Startup":
    st.sidebar.selectbox("Select Startup",sorted(df["invertors"].str.split(",").explode().dropna().unique()))
    btn1=st.sidebar.button("Find startup details")
    st.title("Startup Analysis")

else:
    selected_investor=st.sidebar.selectbox("Select Startup",df["invertors"].explode().tolist())
    btn2=st.sidebar.button("Find investor details")
    if btn2:
        load_investor_details(selected_investor)

# similar investors