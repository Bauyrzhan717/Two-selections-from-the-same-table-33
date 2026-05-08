import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("population.csv")
true_mean=df["value"].mean()
simple_mean=(df.sample(n=20,random_state=42)["value"].mean())
stratified_mean=(df.groupby("stratum").sample(n=10,random_state=42)["value"].mean())
names=["True","Simple","Stratified"]
values=[true_mean,simple_mean,stratified_mean]
plt.bar(names, values)
plt.title("Comparison of Means")
plt.ylabel("Mean")
plt.savefig("means.png")
print("PNG saved as means.png")
plt.show()