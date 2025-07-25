import pandas as pd


df = pd.read_excel(r"C:\Users\User\Desktop\Data_visualization\question_3\sub-saharan_health_facilities.xlsx")


print("Original columns:\n", df.columns)
print(df.head())

rename_map = {
    'Country Name': 'Country',
    'Malaria Prev (%)': 'Malaria_Prevalence',
    'HIV Rate (%)': 'HIV_Rates',
    'Facilities per 10k': 'Healthcare_Facility_Density',
    'Clean Water (%)': 'Access_Clean_Water',
    'Sanitation (%)': 'Access_Sanitation'
}
df.rename(columns=rename_map, inplace=True)

# ✨ Standardize country names (strip whitespace)
df['Country'] = df['Country'].str.strip()

# ✨ Handle missing values
# For numeric columns, fill with median; for strings, drop or fill as needed
for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].median())

# If there are any rows with missing country names, drop them
df = df.dropna(subset=['Country'])


df.to_csv('clean_african_healthcare_data.csv', index=False)
df.to_excel('clean_african_healthcare_data.xlsx', index=False)

print(" Data wrangling complete! Clean dataset saved as:")
print(" - clean_african_healthcare_data.csv")
print(" - clean_african_healthcare_data.xlsx")
