from flask import Flask,request,jsonify
import pandas as pd
app=Flask(__name__)
@app.route("/analyze", methods=["POST"])
def analyze():
    file=request.files["file"]
    df=pd.read_csv(file)
    return jsonify({
        "true_mean": df["value"].mean(),
        "simple_mean": df.sample(n=20)["value"].mean(),
        "stratified_mean": df.groupby("stratum")
            .apply(lambda x: x.sample(n=10))
            .reset_index(drop=True)["value"].mean()
    })
app.run(debug=True)