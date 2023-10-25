import streamlit as st
import pandas as pd

#Open the Data
schoolData = pd.read_csv("data/schoolData.csv")
frpl = pd.read_csv("data/frpl.csv")

#Cleaning School Data
#Only keep those rows in which school_name contains total
mask = schoolData["school_name"].str.contains('Total')
schoolData=schoolData[mask]

#Change the school_name to remove the "Total"
schoolData["school_name"]=schoolData["school_name"].str.replace(" Total","")

#Remove this columns  "school_group", "grade", "pi_pct" and "blank_col"
schoolData=schoolData.drop(columns=["school_group","grade","pi_pct","blank_col"])

#Remove the school name "Grand" because it was "Grand Total"
mask = schoolData["school_name"]!="Grand"
schoolData=schoolData[mask]

#Remove the percentage from the percentage columns
def removePercentageSign(dataframe,column_name):
    dataframe[column_name]=dataframe[column_name].str.replace("%","")

removePercentageSign(schoolData,"na_pct")
removePercentageSign(schoolData,"aa_pct")
removePercentageSign(schoolData,"as_pct")
removePercentageSign(schoolData,"hi_pct")
removePercentageSign(schoolData,"wh_pct")

#Clean Free Lunch
#Remove rows without school name
frpl = frpl.dropna(subset=["school_name"])

#Remove school names that have "ELM K_08", "Mid Schl", "High Schl", "Alt HS", "Spec Ed Total", "Cont Alt Total", "Hospital Sites Total", "Dist Total"
mask = ~(frpl["school_name"].isin(["ELM K_08", "Mid Schl", "High Schl", "Alt HS", "Spec Ed Total", "Cont Alt Total", "Hospital Sites Total", "Dist Total"]))
frpl = frpl[mask]

#Remove the percentage on the percentage column
removePercentageSign(frpl,"frpl_pct")



st.header("School Data")
st.dataframe(schoolData)

st.write("Free Lunch")
st.dataframe(frpl)