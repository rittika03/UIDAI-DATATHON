import pandas as pd
import numpy as np
# 1. Load the dataset
# Using a raw string (r"...") to handle the backslashes in the Windows file path
file_path = r"D:\Aadhar Dataset UIDAI\api_data_aadhar_biometric\api_data_aadhar_biometric\aadhaar_biometric_merged.csv"

# Note: If you encounter an encoding error, try adding encoding='ISO-8859-1' or 'cp1252'
try:
    df = pd.read_csv(file_path)
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

# 2. Define the state mapping dictionary
state_mapping = { 
    'WEST BENGAL': 'West Bengal',
    'WESTBENGAL': 'West Bengal',
    'West  Bengal': 'West Bengal',
    'West Bangal': 'West Bengal',
    'West Bengli': 'West Bengal',
    'West bengal': 'West Bengal',
    'Westbengal': 'West Bengal',
    'west Bengal': 'West Bengal',

    'Andaman & Nicobar Islands': 'Andaman and Nicobar Islands',
    'andhra pradesh': 'Andhra Pradesh',

    'Chhatisgarh': 'Chhattisgarh',
    
    'Dadra & Nagar Haveli': 'Dadra and Nagar Haveli and Daman and Diu',
    'Daman & Diu': 'Dadra and Nagar Haveli and Daman and Diu',
    'The Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
    'Dadra and Nagar Haveli': 'Dadra and Nagar Haveli and Daman and Diu',
    'Daman and Diu': 'Dadra and Nagar Haveli and Daman and Diu',

    'Jammu & Kashmir': 'Jammu and Kashmir',
    'Jammu And Kashmir': 'Jammu and Kashmir',

    'Puttenahalli': 'Karnataka',
    
    'ODISHA': 'Odisha',
    'Orissa': 'Odisha',
    'odisha': 'Odisha',

    'Pondicherry':'Puducherry',

    'Jaipur': 'Rajasthan',
    
    'Tamilnadu': 'Tamil Nadu',
    'Raja Annamalai Puram': 'Tamil Nadu',

    'Uttaranchal': 'Uttarakhand'
}

# 3. Create the new column 'states_cleaned'
# Make sure to replace 'state' below with the exact column name in your CSV (e.g., 'State' or 'State Name') if it differs.
if 'state' in df.columns:
    col_name = 'state'
elif 'State' in df.columns:
    col_name = 'State'
else:
    # Fallback or raise error if column not found
    print("Column 'state' or 'State' not found. Please check your CSV column names.")
    col_name = None

if col_name:
    # Map the values. Values not in the dictionary result in NaN, so we fill them with the original values.
    df['states_cleaned'] = df[col_name].map(state_mapping).fillna(df[col_name])
    print(np.unique(df['states_cleaned']))
    print(len(np.unique(df['states_cleaned'])))

    # 4. Verify the results
    print("Processing complete.")
    print(df['states_cleaned'].nunique())

    # Optional: Save the cleaned data to a new file
    df.to_csv(r"D:\Aadhar Dataset UIDAI\api_data_aadhar_biometric\api_data_aadhar_biometric\aadhaar_biometric_cleaned.csv", index=False)