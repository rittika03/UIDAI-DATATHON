import pandas as pd
import os

# List of your input file paths
# using r"" (raw string) to handle backslashes correctly in Windows paths
file_paths = [
   r"D:\Aadhar Dataset UIDAI\api_data_aadhar_demographic\api_data_aadhar_demographic\api_data_aadhar_demographic_0_500000.csv",
r"D:\Aadhar Dataset UIDAI\api_data_aadhar_demographic\api_data_aadhar_demographic\api_data_aadhar_demographic_500000_1000000.csv",
r"D:\Aadhar Dataset UIDAI\api_data_aadhar_demographic\api_data_aadhar_demographic\api_data_aadhar_demographic_1000000_1500000.csv",
r"D:\Aadhar Dataset UIDAI\api_data_aadhar_demographic\api_data_aadhar_demographic\api_data_aadhar_demographic_1500000_2000000.csv",
r"D:\Aadhar Dataset UIDAI\api_data_aadhar_demographic\api_data_aadhar_demographic\api_data_aadhar_demographic_2000000_2071700.csv"
]
# Create an empty list to hold the dataframes
dataframes = []

print("Reading files...")
for file in file_paths:
    # Check if file exists to avoid errors
    if os.path.exists(file):
        print(f"Reading: {file}")
        # Read the CSV file
        df = pd.read_csv(file)
        dataframes.append(df)
    else:
        print(f"Warning: File not found: {file}")

# Merge all dataframes into one
if dataframes:
    print("Merging data...")
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Define the output path
    # I'll save it in the same folder as the input files
    output_path = r"D:\Aadhar Dataset UIDAI\api_data_aadhar_demographic\api_data_aadhar_demographic\aadhaar_demographic_merged.csv"
    
    print(f"Saving merged file to: {output_path}")
    merged_df.to_csv(output_path, index=False)
    print("Done!")
else:
    print("No files were read.")