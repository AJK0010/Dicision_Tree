# app.py

import streamlit as st
import pandas as pd
import pickle
import os

# --- Configuration ---
FILE_NAME = 'dcision_tree.pkl'

def load_data_or_model(file_path):
    """
    Loads the object from the pickled file. 
    It is assumed to be a pandas DataFrame based on the content analysis.
    """
    if not os.path.exists(file_path):
        st.error(f"Error: The file '{file_path}' was not found.")
        st.stop()
        
    try:
        # Load the object from the pickle file
        with open(file_path, 'rb') as f:
            data_or_model = pickle.load(f)
        return data_or_model
    except Exception as e:
        st.error(f"An error occurred while loading the pickle file: {e}")
        st.stop()

def main():
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(
        page_title="Pickled Data Viewer",
        layout="wide"
    )

    st.title("🚗 Pickled Data Viewer (Car Performance Data)")
    st.markdown("---")

    # Load the DataFrame
    data = load_data_or_model(FILE_NAME)

    if isinstance(data, pd.DataFrame):
        st.header("Loaded DataFrame")
        st.caption(f"Showing the first {len(data)} rows of the DataFrame.")
        
        # Display the DataFrame
        st.dataframe(data)

        st.subheader("Descriptive Statistics")
        st.write(data.describe())
        
        st.subheader("Data Information")
        # Display column names and dtypes in a cleaner way
        info_df = pd.DataFrame({
            'Feature': data.columns,
            'Data Type': data.dtypes.astype(str)
        })
        st.table(info_df)
        
    else:
        st.warning("The loaded object is not a pandas DataFrame. Its type is:")
        st.code(type(data))

if __name__ == "__main__":
    main()
