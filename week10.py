import pandas as pd
df=pd.read_csv("population.csv")
sample_data=df.sample(n=20, random_state=42)
print("Рандом:")
print(sample_data)
sample_mean=sample_data["value"].mean()
print("\nОрта:")
print(sample_mean)