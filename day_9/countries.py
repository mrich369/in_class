"""
LOAD
read_csv()
CLEAN
fillna()
str.title()
VALIDATE
assert

groupby()
mean()

plt.bar()
savefig()
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("day_9/world_development_data.csv")

df["region"] = df["region"].str.title().str.strip()

df["gdp_per_capita"] = pd.to_numeric(
    df["gdp_per_capita"].astype(str).str.replace(",",""), errors = "coerce"
)

"""
print(df.head())
print(df.describe())
print(df.shape) #how many rows and columns
print(df.info())

water_crisis = df[df["clean_water_pct"] < 80]
print(water_crisis[["country", "clean_water_pct"]])

# life expectancy below 60
low_life = df[df["life_expectancy"] < 60]
print()
print(low_life[["country", "life_expectancy"]])
print(f"Total Count: {len(low_life)}")

# higheset life expectancy
high_life = df.loc[df["life_expectancy"].idxmax()]
print(high_life[["country", "life_expectancy"]])

# how many missing values?
null = df.isnull().sum()
print(null)

# sub-saharan africa 
ssa = df[df["region"] == "Sub-Saharan Africa"]
print(ssa[["country", "region"]])



# num of unique regions
df["region"] = df["region"].str.title().str.strip()
regions = df["region"].unique()
print(regions)

# fill in missing values in clean_water_pct
df["clean_water_pct"] = df["clean_water_pct"].fillna(0)
print(df[["clean_water_pct"]])
# check for no missing values
assert df["clean_water_pct"].notna().all(), "Missing clean water data!"

print(df.groupby("region")["life_expectancy"].mean())

print(df.groupby("region")["literacy_rate"].mean())
print()
print(df.groupby("region")["literacy_rate"].mean().idxmin())
print()

# low_lit_rate = df.loc[df["literacy_rate"].idxmin()]
# print(low_lit_rate[["country", "literacy_rate"]])

# total pop by region
print(df.groupby("region")["population_thousands"].sum().sort_values(ascending=False))

# total num of countries in each region
print(df.groupby("region")["country"].count())

# max life expectancy by region
print(df.groupby("region")["life_expectancy"].max())
print(df.loc[df["life_expectancy"].idxmax()])


print()
print()
# avg gdp per capita 
high_le = df[df["life_expectancy"] > 70]
low_le = df[df["life_expectancy"] < 60]

print(high_le["gdp_per_capita"].mean())
print(low_le["gdp_per_capita"].mean())
print()

# print new column
df['total_gdp'] = df["gdp_per_capita"] * df["population_thousands"]
print(df.groupby("region")["total_gdp"].sum().idxmax())
print(df.groupby("region")["total_gdp"].sum().max())

"""

# Scatter plot
plt.scatter(df["life_expectancy"], df["literacy_rate"], color="purple")
plt.title("Life Expectancy vs. Literacy Rate")
plt.xlabel("Life Expectancy")
plt.ylabel("Literacy Rate")
plt.tight_layout()

plt.savefig("life_and_literacy.png")
plt.show()