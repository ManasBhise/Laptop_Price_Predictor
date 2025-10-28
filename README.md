

# 💻 Laptop Price Predictor

<p align="center">
	<img src="dataset-cover.jpg" alt="Dataset Cover" width="600" />
</p>

Welcome to the Laptop Price Predictor! This project is a complete data science solution that leverages machine learning to estimate the price of a laptop based on its specifications. The goal is to provide users with a simple, interactive web app where they can enter details about a laptop and instantly receive a price prediction.

## Explore My Project

https://laptoppricepredictor-sdvybhgcakgwppwjbcxbml.streamlit.app/

## 🚀 What Does This Project Do?

This app takes in key laptop features—such as brand, processor, RAM, storage, graphics, and display size—and predicts the price using a trained regression model. It demonstrates the full workflow of a real-world machine learning project:

1. **Data Collection:** Gathered a dataset of laptops and their specifications.
2. **Data Cleaning & Preprocessing:** Removed inconsistencies, handled missing values, and transformed categorical and numerical data for modeling.
3. **Feature Engineering:** Selected and encoded the most relevant features for price prediction.
4. **Model Training:** Built and evaluated regression models using scikit-learn to find the best fit for the data.
5. **Deployment:** Created a user-friendly web app with Streamlit, allowing anyone to use the model online.



## 🛠️ Technologies Used

- Python
- Pandas
- Numpy
- Scikit-learn
- Streamlit


## 🌟 Key Features

- **Instant Price Prediction:** Enter laptop specs and get a price estimate in seconds.
- **Interactive Web Interface:** Simple, clean UI built with Streamlit.
- **End-to-End Data Science:** From raw data to deployed app, all steps are included.
- **Open Source:** All code and data are available for learning and improvement.





## 📊 Results

### Model Performance

- **Best Algorithm Used:** Voting Regressor (Random Forest, Gradient Boosting, XGBoost, Extra Trees)
- **R² Score:** 0.87
- **Mean Absolute Error (MAE):** 0.21 (log price)

The model achieves a strong R² score, indicating it explains 87% of the variance in laptop prices. The low MAE (in log price) means predictions are close to actual prices.




## 📂 Project Structure

- `app.py` — Main Streamlit app
- `laptop_data.csv` — Raw data
- `df.pkl`, `pipe.pkl` — Preprocessed data and trained model
- `requirements.txt` — Python dependencies



## 👤 Author
**Manas**

## 📅 Date of Project Creation
**October 24, 2025**
