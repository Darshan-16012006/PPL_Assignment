import pandas as pd

# Create DataFrame
data = {
    'State': ['Maharashtra', 'Uttar Pradesh', 'Bihar', 'Rajasthan', 'Karnataka'],
    'Area': [307713, 243286, 94163, 342239, 191791],   # in sq km
    'Population': [124000000, 240000000, 130000000, 81000000, 70000000]
}

df = pd.DataFrame(data)

# a) Print complete information
print("\n--- Complete State Information ---")
print(df)

# b) State with largest area
largest_area_state = df.loc[df['Area'].idxmax(), 'State']
print("\nState with Largest Area:", largest_area_state)

# c) State with largest population
largest_population_state = df.loc[df['Population'].idxmax(), 'State']
print("State with Largest Population:", largest_population_state)

# d) Calculate population density
df['Population Density'] = df['Population'] / df['Area']

print("\n--- Data with Population Density ---")
print(df)

# e) State with highest population density
highest_density_state = df.loc[df['Population Density'].idxmax(), 'State']
print("\nState with Highest Population Density:", highest_density_state)