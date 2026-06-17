# 🔥 Algerian Forest Fire Prediction

A machine learning web application that predicts the **Fire Weather Index (FWI)** and classifies fire risk levels based on environmental and weather conditions.

Built using **Python, Scikit-learn, and Streamlit**, this project provides an interactive interface for real-time predictions.

---

## 🚀 Live Demo

👉 Deploy easily using **Streamlit Community Cloud**

---

## 📌 Features

* Predicts **Fire Weather Index (FWI)**
* Classifies risk levels:

  * 🟢 Low
  * 🟡 Moderate
  * 🟠 High
  * 🔴 Extreme
* Interactive UI with user inputs
* Real-time predictions
* Clean and simple dashboard

---

## 🧠 Machine Learning

* Model: Ridge Regression
* Preprocessing: Standard Scaler
* Libraries:

  * NumPy
  * Pandas
  * Scikit-learn

---

## 📂 Project Structure

```
algerianforestfires/
│
├── app.py                # Streamlit application
├── requirements.txt      # Dependencies
├── models/
│   ├── ridge.pkl         # Trained ML model
│   └── scaler.pkl        # Scaler for preprocessing
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/algerianforestfires.git
cd algerianforestfires
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app locally

```
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Community Cloud**:

1. Push your code to GitHub
2. Go to Streamlit Cloud
3. Select your repository
4. Set `app.py` as the main file
5. Deploy 🚀

---

## 📊 Input Parameters

The model uses the following features:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* FFMC
* DMC
* ISI
* Classes
* Region

---

## 📈 Output

* **FWI Score** (numeric prediction)
* **Risk Level Classification**

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by **Subayan Ghosh**
