import streamlit as st
from clf import *                                                   

def main():
    st.title("Financial Inclusion Predictor")
    st.write("Provide the individual's details to predict thier likelihood of having a bank account")


    country = st.selectbox("Select the Country", ["", "Kenya", "Rwanda", "Tanzania", "Uganda"])
    year = st.number_input("Enter the Year", min_value=2000, max_value=2025, step=1, value=2016)
    uniqueid = st.text_input("Enter the Unique ID")
    location_type = st.selectbox("Select the Location Type", ["", "Urban", "Rural"])
    cellphone_access = st.selectbox("Does the Individual Have Cellphone Access?", ["Yes", "No"])
    household_size = st.number_input("Enter the Household Size", min_value=1, step=1, value=1)
    age_of_respondent = st.number_input("Enter Age of Respondent", min_value=1, max_value=120, step=1, value=30)
    gender_of_respondent = st.selectbox("select Gender of Respondent", ["", "Male", "Female"])
    relationship_with_head = st.selectbox("Select Relationship with Head of Household", 
                                          ["", "Head of Household", "Spouse", "Child", "Parent", "Other Relative", "Non-Relative"])
    marital_status = st.selectbox("Select Marital Status", ["", "Married", "single", "Divorced", "Widowed", 'Seperated'])
    education_level = st.selectbox("select Education Level", ["", "No Formal Education", "Primary Education", "Secondary Education", "Tertiary Education"])
    job_type = st.selectbox("Select Job Type", ["", "Unemployed", "Government Worker", "Private Sector Worker", "Other"])


    bank_account = ""

    if st.button("Predict"):
        
        bank_account = prediction([
            country, year, uniqueid, location_type, cellphone_access, household_size,
            age_of_respondent, gender_of_respondent, relationship_with_head,
            marital_status, education_level, job_type
        ])
    st.success(bank_account)


if __name__ == "__main__":
    main()