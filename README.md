# 🎬 Movie Recommendation System using Machine Learning

## 📌 Project Overview

This project is a **Movie Recommendation System** developed using **Machine Learning** techniques.
The system recommends movies to users based on:

* ✅ Content-Based Filtering
* ✅ Collaborative Filtering

The project uses the **MovieLens 100K Dataset** and demonstrates how recommendation engines used in platforms like Netflix and Amazon work.

---

# 🚀 Features

## ✅ Content-Based Filtering

Recommends movies based on:

* Genre
* Movie similarity
* Keywords
* Cast/Director (optional)

Example:
If user likes **PK**, the system recommends similar comedy/drama movies.

---

## ✅ Collaborative Filtering

Recommends movies using:

* User-item interaction matrix
* Similar users
* Rating patterns

Example:
Users who liked movie A also liked movie B.

---

## ✅ Data Visualization

The project includes:

* Genre Distribution
* Ratings Distribution
* Word Cloud Visualization
* Correlation Heatmaps
* Recommendation Outputs

---

## ✅ Evaluation Metrics

Implemented:

* Precision@K
* Recall@K

---

## ✅ Interactive Web App

Built using:

* Streamlit

Features:

* Movie selection
* Recommendation button
* Professional UI
* Dark/Light Theme

---

# 📂 Dataset Used

## 🎥 MovieLens 100K Dataset

Contains:

* Movies
* User Ratings
* Genres
* User-Movie interactions

Dataset Link:

[MovieLens Dataset](https://grouplens.org/datasets/movielens/100k/?utm_source=chatgpt.com)

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn
* Scikit Surprise
* WordCloud

---

# 📊 Machine Learning Concepts Used

## 🔹 Content-Based Filtering

Uses:

* TF-IDF Vectorization
* Cosine Similarity

---

## 🔹 Collaborative Filtering

Uses:

* User-Item Matrix
* Similarity-based recommendations

---

# 📁 Project Structure

```bash
Movie-Recommendation-System/
│
├── app.py
├── movies.csv
├── ratings.csv
├── Movie_Recommendation.ipynb
├── requirements.txt
├── README.md
└── assets/
```

---

# ▶️ How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📈 Observations

* Drama and Comedy are the most common genres.
* Collaborative Filtering provides more personalized recommendations.
* Content-Based Filtering works well for similar movie discovery.
* Hybrid recommendation systems can improve accuracy further.

---

# 📸 Sample Outputs

## 🎬 Recommendation Output

* PK → Kahaani, Bawali Unlimited, Yaraan Naal Baharaan 2

## 📊 Feature Visualizations

* Genre Frequency Graph
* Word Cloud
* Ratings Distribution

---

# 🎯 Internship Requirements Covered

✅ Content-Based Filtering
✅ Collaborative Filtering
✅ MovieLens Dataset
✅ Precision@K and Recall@K
✅ Interactive Web Interface
✅ Data Visualization
✅ Recommendation Engine

---

# 📚 Future Improvements

* Hybrid Recommendation System
* Deep Learning-based Recommendations
* Real-time User Login
* Personalized User Profiles
* Bollywood + Hollywood Combined Recommendation Engine

---

# 👨‍💻 Author

**Ashraf Shikalgar**
AI & Machine Learning Enthusiast 🚀

---

# ⭐ Conclusion

This project demonstrates how machine learning can be used to build intelligent recommendation systems similar to Netflix and YouTube recommendation engines. It covers both theoretical and practical implementation of recommendation algorithms with interactive visualization and deployment support.
