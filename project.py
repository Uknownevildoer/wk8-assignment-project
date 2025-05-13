import pandas as pd

# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# Preview the structure
print(df.columns)
print(df.head())



# Check for missing values
print(df.isnull().sum())
# Filter for selected countries
countries = ["Kenya", "United States", "India"]
df = df[df['location'].isin(countries)]

# Drop rows with missing critical data
df = df.dropna(subset=['date', 'total_cases'])

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Fill missing numerical values
df.fillna(0, inplace=True)  # or use df.interpolate()


import matplotlib.pyplot as plt
import seaborn as sns

# Plot total cases over time
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_cases'], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.show()

# Compute and display death rate
df['death_rate'] = df['total_deaths'] / df['total_cases']


for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_vaccinations'], label=country)

plt.title("Vaccination Progress Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.show()



import plotly.express as px

latest = df[df['date'] == df['date'].max()]
fig = px.choropleth(latest,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    title="Global COVID-19 Total Cases")
fig.show()





