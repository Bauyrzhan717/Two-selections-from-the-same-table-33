import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("population.csv")
true_mean=df["value"].mean()
simple_mean=df.sample(n=20)["value"].mean()
strat_mean=df.groupby("stratum")\
    .apply(lambda x: x.sample(n=10))\
    .reset_index(drop=True)["value"].mean()
print("Ақиқат:",true_mean)
print("Жай:",simple_mean)
print("Стратифицировтік:",strat_mean)
plt.bar(["True","Simple","Stratified"],
        [true_mean,simple_mean,strat_mean])
plt.savefig("result.png")