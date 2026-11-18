import os
import pandas as pd
from flask import Flask, render_template

current_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(current_dir, "templates"),
    static_folder=os.path.join(current_dir, "static"),
)

# ------------------------------------------------------------------------------
# 1. Load Dataset (Cache locally in pandda folder for fast offline access)
# ------------------------------------------------------------------------------
csv_path = os.path.join(current_dir, "titanic.csv")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

if os.path.exists(csv_path):
    print("Loading Titanic dataset from local cache...")
    titanic_df = pd.read_csv(csv_path)
else:
    print("Downloading Titanic dataset from URL...")
    titanic_df = pd.read_csv(url)
    titanic_df.to_csv(csv_path, index=False)
    print("Dataset saved to local file: titanic.csv")

# Print first few rows to console (maintains original file.py functionality)
print("\n--- Titanic Dataset Head ---")
print(titanic_df.head())
print("-----------------------------\n")

# ------------------------------------------------------------------------------
# 2. Flask Route
# ------------------------------------------------------------------------------
@app.route("/")
def index():
    # Calculate Summary Statistics
    total_passengers = len(titanic_df)
    survived_count = int(titanic_df["Survived"].sum())
    survival_rate = round((survived_count / total_passengers) * 100, 2)
    avg_age = round(titanic_df["Age"].mean(), 1)
    min_age = round(titanic_df["Age"].min(), 1)
    max_age = round(titanic_df["Age"].max(), 1)
    avg_fare = round(titanic_df["Fare"].mean(), 2)
    max_fare = round(titanic_df["Fare"].max(), 2)

    # Prepare rows dictionary for clean rendering
    df_copy = titanic_df.copy()
    pclass_map = {1: "1st Class", 2: "2nd Class", 3: "3rd Class"}
    df_copy["Pclass_Label"] = df_copy["Pclass"].map(pclass_map)
    df_copy = df_copy.astype(str)

    rows = df_copy.to_dict(orient="records")
    for r in rows:
        r["Survived"] = int(float(r["Survived"]))
        r["Pclass"] = int(float(r["Pclass"]))
        r["Fare"] = float(r["Fare"])

    return render_template(
        "index.html",
        total_passengers=total_passengers,
        survived_count=survived_count,
        survival_rate=survival_rate,
        avg_age=avg_age,
        min_age=min_age,
        max_age=max_age,
        avg_fare=avg_fare,
        max_fare=max_fare,
        rows=rows,
    )

# ------------------------------------------------------------------------------
# 3. Run Application on Localhost
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Starting Flask web server on http://127.0.0.1:5000 ...")
    app.run(host="127.0.0.1", port=5000, debug=False)
