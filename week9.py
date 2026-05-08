import pandas as pd
df=pd.read_csv("population.csv")
stratum_A=df[df["stratum"]=="A"]["value"]
stratum_B=df[df["stratum"]=="B"]["value"]
print("A:")
print(stratum_A)
print("\n B:")
print(stratum_B)
true_mean=df["value"].mean()
print("\nшынайы орташа:")
print(true_mean)