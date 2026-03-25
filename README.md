# 🤖 Ensemble Methods Agent

A Streamlit app that lets you upload any tabular dataset and train **Bagging**, **Boosting**, and **Stacking** ensemble models with full EDA.

---

## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)

---

## 📁 Project Structure

```
ensemble_agent/
├── app.py                          # Home page
├── requirements.txt
├── sample_data/
│   └── loan_default.csv            # Sample dataset to try
├── utils/
│   └── helpers.py                  # Shared preprocessing & metrics
└── pages/
    ├── 1_📁_Upload_&_EDA.py        # File upload + EDA
    ├── 2_🎒_Bagging.py             # Random Forest + BaggingClassifier
    ├── 3_⚡_Boosting.py            # AdaBoost + GBM + XGBoost
    ├── 4_📚_Stacking.py            # Stacking with meta-learner
    └── 5_📊_Model_Comparison.py    # Side-by-side metrics dashboard
```

---

## ⚙️ Setup & Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ensemble-methods-agent.git
cd ensemble-methods-agent

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 🌐 Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select your repo
4. Set **Main file path** to `app.py`
5. Click **Deploy!**

---

## 📊 Features

| Feature | Details |
|---|---|
| **File upload** | CSV, Excel (.xlsx/.xls), TXT (auto-detects delimiter) |
| **Auto task detection** | Classification or Regression based on target column |
| **EDA** | Overview, distributions, correlation heatmap, target analysis, missing values |
| **Bagging** | Random Forest + generic BaggingClassifier/Regressor, OOB curve, feature importance |
| **Boosting** | AdaBoost, Gradient Boosting, XGBoost — learning curves, feature importance |
| **Stacking** | Choose base learners + meta-learner, compare vs individual models |
| **Comparison** | Metrics table, bar charts, radar chart, CV scores |

---

## 🧪 Sample Data

Try the included `sample_data/loan_default.csv`:
- **Target column:** `has_default`
- **Task:** Classification
- **Features:** age, income, education_years, employment_years, credit_score, loan_amount

---

## 📦 Dependencies

- `streamlit` — web app framework
- `scikit-learn` — ML models
- `xgboost` — gradient boosting
- `pandas`, `numpy` — data handling
- `matplotlib`, `seaborn` — visualisations
- `openpyxl`, `xlrd` — Excel support

---

## 🤝 Contributing

Pull requests welcome! Open an issue first to discuss what you'd like to change.
