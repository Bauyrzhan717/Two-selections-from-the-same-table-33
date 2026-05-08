from flask import Flask, jsonify
import pandas as pd
app=Flask(__name__)
@app.route("/means", methods=["POST"])
def means():
    df=pd.read_csv("population.csv")
    true_mean=df["value"].mean()
    simple_mean=(df.sample(n=20, random_state=42)["value"].mean())
    stratified_mean=(df.groupby("stratum").sample(n=10,random_state=42)["value"].mean())
    result={"true_mean": true_mean,"simple_mean": simple_mean,"stratified_mean": stratified_mean}
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)