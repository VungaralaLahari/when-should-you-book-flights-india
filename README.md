#  When Should You Book Flights in India?
### A Data-Driven Flight Price Intelligence Study

---

##  Problem Statement

Flight ticket prices in India fluctuate significantly based on multiple factors such as airline, route, booking time, and travel class.

This project answers a practical and widely relevant question:

> **Which airline is cheapest on which route, and how many days in advance should you book to get the best price?**

---

##  Dataset

- Source: EaseMyTrip flight dataset (Kaggle)
- ~300,000+ records
- 6 airlines, 6 major cities
- Features include:
  - Airline
  - Source & Destination
  - Days before departure
  - Departure time
  - Stops
  - Class (Economy / Business)
  - Price

---

##  Project Pipeline
Data → Cleaning → SQL Analysis → Python Visualization → Insights → ML Model → Streamlit App

---

## Data Cleaning (Python)

- Removed duplicates and handled missing values
- Converted duration into numeric format
- Created new features:
  - `route` (source → destination)
  - `departure_time_category`
- Ensured correct data types

---

##  SQL Analysis

Used SQLite to perform analytical queries:

- Cheapest airline overall and by class
- Price trends vs days before departure
- Route-wise pricing insights
- Cheapest airline per route
- Airline dominance per route

---

##  Key Insights

-  **AirAsia and IndiGo are consistently the cheapest airlines**
-  **Best booking window: 47–49 days before departure**
-  Prices spike significantly in the last 2–3 days
-  **Night and afternoon flights are cheaper**
-  **Non-stop flights are surprisingly the cheapest on average**
-  Delhi routes are cheaper due to high competition
- Business class is **8–9x more expensive** than Economy

---

##  Visualization (Python)

- Bar charts for airline comparison
- Line charts for price trends
- Heatmaps for airline vs time pricing
- Distribution analysis for pricing patterns

---

##  Machine Learning Model

- Model: Random Forest Regressor
- Features:
  - Airline, Route, Days Left, Stops, Time, Class
- Metrics:
  - RMSE: (your value)
  - R² Score: (your value)

### Why Random Forest?
- Handles non-linear relationships
- Reduces overfitting
- Works well with minimal tuning

---

##  Feature Importance

Key factors affecting price:
- Days before departure (most important)
- Airline choice
- Route

---

##  Streamlit Application

Built an interactive web app to:

- Input flight details
- Predict ticket price in real-time

### Features:
- User-friendly UI
- Real-time predictions
- Practical decision-making tool

---

##  How to Run

```bash
streamlit run app/app.py
```
-----

 Tech Stack
- Python (Pandas, NumPy, Scikit-learn)
- SQL (SQLite)
- Visualization (Matplotlib, Seaborn)
- Streamlit

------
 Business Impact

This project helps:

Travelers make smarter booking decisions
Identify cheapest airlines and routes
Understand pricing patterns in Indian aviation

---
 Notebook Viewer 

If the notebook does not render properly on GitHub, view it using nbviewer:

https://nbviewer.org/github/VungaralaLahari/when-should-you-book-flights-india/blob/main/Flight_Price_Intelligence.ipynb

--- 
Conclusion

This project transforms raw flight data into actionable insights and a real-world application, bridging data analysis and practical decision-making.

