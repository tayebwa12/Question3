import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\User\Desktop\Data_visualization\question_3\clean_african_healthcare_data.csv")

# ✅ Quick overview
print("🔎 First 5 rows:\n", df.head())
print("\n✅ Info:")
print(df.info())
print("\n📌 Descriptive stats:\n", df.describe())



plt.figure(figsize=(10, 6))
numeric_cols = df.select_dtypes(include='number')  # only numeric columns
sns.heatmap(numeric_cols.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap of Health Indicators", fontsize=14)
plt.tight_layout()
plt.show()

sns.pairplot(df[numeric_cols.columns], diag_kind='kde')
plt.suptitle("Pairwise Relationships Between Indicators", y=1.02, fontsize=14)
plt.show()


key_columns = ['Malaria_Prevalence', 'HIV_Rate', 'Facility_Density', 'Clean_Water_Access', 'Sanitation_Access']
for col in key_columns:
    if col in df.columns:
        plt.figure(figsize=(8,4))
        sns.histplot(df[col], kde=True, bins=20)
        plt.title(f"Distribution of {col}", fontsize=14)
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()


if 'Country' in df.columns and 'Malaria_Prevalence' in df.columns:
    top_malaria = df[['Country','Malaria_Prevalence']].sort_values(by='Malaria_Prevalence', ascending=False).head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(data=top_malaria, x='Malaria_Prevalence', y='Country', palette='Reds_r')
    plt.title("Top 10 Countries by Malaria Prevalence", fontsize=14)
    plt.xlabel("Malaria Prevalence (%)")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.show()


if 'Facility_Density' in df.columns and 'Clean_Water_Access' in df.columns:
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x='Facility_Density', y='Clean_Water_Access', hue='Malaria_Prevalence', palette='coolwarm')
    plt.title("Facility Density vs Clean Water Access", fontsize=14)
    plt.xlabel("Healthcare Facility Density")
    plt.ylabel("Clean Water Access (%)")
    plt.tight_layout()
    plt.show()

print("\n EDA Completed! Check the visualizations above.")
