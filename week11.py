import pandas as pd
df=pd.read_csv("population.csv")
stratified_sample=(df.groupby("stratum").sample(n=10, random_state=42))
print("Стратифицировтік:")
print(stratified_sample)
stratified_mean=stratified_sample["value"].mean()
print("\nорта:")
print(stratified_mean)