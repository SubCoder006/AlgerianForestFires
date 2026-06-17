from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# ── App Initialization ─────────────────────────────

app = Flask(__name__)

# ── Load Models ───────────────────────────────────

ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
scaler_model = pickle.load(open("models/scaler.pkl", "rb"))

# ── Home Route ────────────────────────────────────


@app.route("/")
def index():
    return render_template("index.html")


# ── Prediction Route ──────────────────────────────


@app.route("/predict", methods=["POST"])
def predict():
    try:
        temperature = float(request.form["temperature"])
        rh = float(request.form["rh"])
        ws = float(request.form["ws"])
        rain = float(request.form["rain"])
        ffmc = float(request.form["ffmc"])
        dmc = float(request.form["dmc"])
        isi = float(request.form["isi"])
        classes = float(request.form["classes"])
        region = float(request.form["region"])

        data = pd.DataFrame(
            [[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]],
            columns=[
                "Temperature",
                "RH",
                "Ws",
                "Rain",
                "FFMC",
                "DMC",
                "ISI",
                "Classes",
                "Region",
            ],
        )

        scaled_data = scaler_model.transform(data)

        prediction = ridge_model.predict(scaled_data)[0]

        if prediction < 10:
            risk = "Low 🟢"
        elif prediction < 30:
            risk = "Moderate 🟡"
        elif prediction < 60:
            risk = "High 🟠"
        else:
            risk = "Extreme 🔴"

        return render_template(
            "index.html",
            prediction_text=f"FWI: {prediction:.2f} | Risk: {risk}",
            temperature=temperature,
            rh=rh,
            ws=ws,
            rain=rain,
            ffmc=ffmc,
            dmc=dmc,
            isi=isi,
            classes=classes,
            region=region,
        )

    except Exception as e:
        print(e)  # debug in terminal
        return render_template("index.html", prediction_text=f"Error: {str(e)}")


# ── Run App ───────────────────────────────────────

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
