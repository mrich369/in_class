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
df = pd.read_csv("day_9/world_development_data.csv")
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

# num of unique regions
df["region"] = df["region"].str.title().str.strip()
regions = df["region"].unique()
print(regions)

# how many missing values?
null = df.isnull().sum()
print(null)

# sub-saharan africa 
ssa = df[df["region"] == "Sub-Saharan Africa"]
print(ssa[["country", "region"]])

# fill in missing values in clean_water_pct
df["clean_water_pct"] = df["clean_water_pct"].fillna(0)
print(df[["clean_water_pct"]])
# check for no missing values
assert df["clean_water_pct"].notna().all(), "Missing clean water data!"