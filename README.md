# House Price Prediction

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## Project Overview

This project implements a complete machine learning pipeline to predict house prices using the **California Housing Dataset** from scikit-learn. It covers data exploration, feature engineering, model training, evaluation, and business insights — developed as **Task 6** of the AI/ML Engineering Internship at **DevelopersHub Corporation**.

## Dataset

The **California Housing Dataset** is derived from the 1990 U.S. Census data and contains 20,640 samples with 8 features:

| Feature | Description |
|---|---|
| MedInc | Median income in block group |
| HouseAge | Median house age in block group |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms per household |
| Population | Block group population |
| AveOccup | Average household occupancy |
| Latitude | Block group latitude |
| Longitude | Block group longitude |

**Target Variable:** MedHouseVal — Median house value (in $100,000s)

## Exploratory Data Analysis Findings

- The dataset contains **20,640 records** with **8 numeric features** and no missing values
- Median income shows the **strongest positive correlation** (~0.69) with house prices
- Geographic location (latitude/longitude) has a significant impact on pricing
- Feature engineering (rooms per household, population density) improves model performance
- Price distribution is right-skewed, concentrated around $100K–$200K

## Models Used

| Model | Description |
|---|---|
| Linear Regression | Baseline model using ordinary least squares |
| Gradient Boosting Regressor | Ensemble method with sequential tree boosting |

## Results

| Metric | Linear Regression | Gradient Boosting |
|---|---|---|
| MAE | ~0.53 | ~0.31 |
| RMSE | ~0.74 | ~0.46 |
| R² Score | ~0.58 | ~0.84 |

> Gradient Boosting significantly outperforms Linear Regression across all metrics.

## Project Structure

```
Task 6/
├── house_price_prediction.ipynb   # Main Jupyter notebook (29 cells)
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
└── screenshots/                    # Output screenshots
    └── .gitkeep
```

## How to Run

1. **Clone or navigate to the project directory:**
   ```bash
   cd "D:\Documents\GIT\AI ML Internship Tasks\Task 6"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook house_price_prediction.ipynb
   ```

4. **Run all cells** sequentially from the top.

## Screenshots

> Add output screenshots to the `screenshots/` folder and reference them here.

![Notebook Output](screenshots/.gitkeep)

## Future Improvements

- Integrate additional datasets (e.g., crime rates, school ratings, proximity to amenities)
- Implement advanced models (XGBoost, LightGBM, neural networks)
- Deploy the model as a REST API using FastAPI or Flask
- Build an interactive Streamlit dashboard for real-time predictions
- Add hyperparameter tuning with Optuna or GridSearchCV

## Author

**Shahab Ahmed**  
AI/ML Engineering Intern  
[DevelopersHub Corporation](https://developershub.com)

## License

This project is licensed under the [MIT License](LICENSE).
