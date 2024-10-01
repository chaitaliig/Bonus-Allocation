import streamlit as st
import pandas as pd

# App title
st.title("Bonus Allocation Optimization")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data", df)

    #####################################################################################
    #######
    ##########################################################################################    

    # Define criteria for eligibility
    st.header("Eligibility Criteria")
    criteria = {
        "Age": st.slider("Age", min_value=18, max_value=80, value=18),
        "Income level": st.slider("Income level", min_value=20000, max_value=150000, value=20000),
        "Winning %": st.slider("Winning %", min_value=5, max_value=80, value=5),
        "Last bet": st.slider("Days Since Last Bet", min_value=1, max_value=40, value=1),
        "Active Days": st.slider("Active Days", min_value=1, max_value=40, value=1),
        "Total amount wagered": st.slider("Total Amount Wagered", min_value=100, max_value=100000, value=100),
        "Avg Bet Amount": st.slider("Average Bet Amount", min_value=10, max_value=1000, value=10),
        "No of bonus received": st.slider("Number of Bonuses Received", min_value=1, max_value=100, value=1),
        "Amount of bonus received": st.slider("Amount of Bonuses Received", min_value=10, max_value=1000, value=10),
        "Revenue from Bonus": st.slider("Revenue from Bonuses", min_value=10, max_value=5000, value=10),
        "Increased in bets after bonus": st.slider("Increase in Bets After Bonus", min_value=80, max_value=500, value=80),
        "Increased in wagering after bonus": st.slider("Increase in Wagering After Bonus", min_value=100, max_value=50000, value=100),
    }

    # Apply criteria to filter eligible users
    st.header("Eligible Users")
    filtered_df = df[
        (df['age'] >= criteria['Age']) &
        (df['income_level'] >= criteria['Income level']) &
        (df['Winning_percentage'] >= criteria['Winning %']) &
        (df['Days_Since_Last_Bet'] >= criteria['Last bet']) &
        (df['Active_Days'] >= criteria['Active Days']) &
        (df['Total_Amount_Wagered'] >= criteria['Total amount wagered']) &
        (df['Average_Bet_Amount'] >= criteria['Avg Bet Amount']) &
        (df['Number_of_Bonuses_Received'] >= criteria['No of bonus received']) &
        (df['Amount_of_Bonuses_Received'] >= criteria['Amount of bonus received']) &
        (df['Revenue_from_Bonuses'] >= criteria['Revenue from Bonus']) &
        (df['Increase_in_Bets_After_Bonus'] >= criteria['Increased in bets after bonus']) &
        (df['Increase_in_wagering_after_Bonus'] >= criteria['Increased in wagering after bonus'])
    ]

    st.write("Filtered Eligible Users", filtered_df)

    # Display summary statistics for eligible users
    st.subheader("Summary Statistics of Eligible Users")
    st.write(filtered_df.describe())

    # Download button for filtered data
    st.header("Download Filtered Data")
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(filtered_df)
    st.download_button(label="Download CSV", data=csv, file_name='eligible_users.csv', mime='text/csv')
else:
    st.write("Please upload a CSV file to proceed.")
