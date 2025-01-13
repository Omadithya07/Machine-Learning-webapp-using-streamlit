import numpy as np
import pandas as pd
import streamlit as st 
import pickle

# Load the pre-trained model
model = pickle.load(open(r'gnb_company_bayes_model.pkl', 'rb'))

def main(): 
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">US-Market or Not Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Input fields with specific instructions
    st.subheader("Input Values:")

    # Sales: Expected input is a positive number indicating product sales performance.
    sales = st.text_input("Enter the product's sales performance (e.g., 9.5, 11.22, 10.06)")

    # Advertising: Expected input is the amount spent on advertising (positive number).
    advertising = st.text_input("Enter the amount spent on advertising (e.g., 11, 16, 10)")

    # Price: Expected input is the product's price (positive number).
    price = st.text_input("Enter the product's price (e.g., 120, 83, 80)")

    # Age: Expected input is the age of the store or company in years (positive number).
    age = st.text_input("Enter the age of the store or company (e.g., 42, 59, 65)")

    # Education: Expected input is the education level in the range of 1-20 (positive number).
    education = st.text_input("Enter the education level of the manager (e.g., 17, 10, 12)")

    # Urban: Expected input is 1 for 'Yes' and 0 for 'No', indicating if the store is located in an urban area.
    urban = st.text_input("Enter '1' if the store is in an urban area, '0' if not (1 for Yes, 0 for No)")

    # Button to make prediction
    if st.button("Predict"): 
        # Check if inputs are valid
        try:
            data = {'Sales': float(sales), 'Advertising': float(advertising), 'Price': float(price),
                    'Age': int(age), 'Education': int(education), 'Urban': int(urban)}
            
            # Convert input data to DataFrame for prediction
            df = pd.DataFrame([data])
            
            # Get prediction from model
            prediction = model.predict(df)
            output = int(prediction[0])
            
            # Display prediction result
            if output == 1:
                st.success("The product is expected to be in the US market.")
            else:
                st.success("The product is not expected to be in the US market.")
        
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
      
if __name__=='__main__': 
    main()
