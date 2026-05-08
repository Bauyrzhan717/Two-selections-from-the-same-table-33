import pandas as pd
df=pd.read_csv("population.csv")
true_mean=df["value"].mean()
simple_sample=df.sample(n=20,random_state=42)
simple_mean=simple_sample["value"].mean()
stratified_sample=(df.groupby("stratum").sample(n=10,random_state=42))
stratified_mean=stratified_sample["value"].mean()
means_table=pd.DataFrame({"Type":["True Mean","Simple Sample","Stratified Sample"],"Mean":[true_mean,simple_mean,stratified_mean]})
print(means_table)