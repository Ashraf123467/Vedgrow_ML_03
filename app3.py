import streamlit as st
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Netflix Style Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0b1120;
    color: white;
    font-family: sans-serif;
}

.title {
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:white;
    margin-top:10px;
}

.subtitle {
    text-align:center;
    font-size:22px;
    color:#cbd5e1;
    margin-bottom:40px;
}

.movie-card {
    background: linear-gradient(145deg,#111827,#1e293b);
    padding:15px;
    border-radius:18px;
    text-align:center;
    color:white;
    transition:0.3s;
    box-shadow:0px 6px 15px rgba(0,0,0,0.5);
}

.movie-card:hover {
    transform: scale(1.03);
}

.movie-title {
    font-size:18px;
    font-weight:bold;
    margin-top:10px;
    color:white;
}

.stButton>button {
    width:100%;
    background: linear-gradient(135deg,#dc2626,#991b1b);
    color:white;
    border:none;
    border-radius:12px;
    height:55px;
    font-size:20px;
    font-weight:bold;
}

section[data-testid="stSidebar"] {
    background-color:#111827;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Reduce dataset size for Streamlit stability
ratings = ratings.head(20000)

# -------------------------------------------------
# MERGE DATA
# -------------------------------------------------
movie_data = ratings.merge(movies, on='movieId')

# -------------------------------------------------
# USER MOVIE MATRIX
# -------------------------------------------------
user_movie_matrix = movie_data.pivot_table(
    index='userId',
    columns='title',
    values='rating'
)

user_movie_matrix = user_movie_matrix.iloc[:, :500]

user_movie_matrix = user_movie_matrix.fillna(0)

# -------------------------------------------------
# SIMILARITY MATRIX
# -------------------------------------------------
movie_similarity = cosine_similarity(user_movie_matrix.T)

similarity_df = pd.DataFrame(
    movie_similarity,
    index=user_movie_matrix.columns,
    columns=user_movie_matrix.columns
)


# -------------------------------------------------
# HYBRID RECOMMENDATION FUNCTION
# -------------------------------------------------
def recommend_movies(movie_name, n=5):

    if movie_name not in similarity_df.columns:
        return []

    collaborative_scores = similarity_df[movie_name].sort_values(
        ascending=False
    )[2:n+2]

    recommendations = collaborative_scores.index.tolist()

    return recommendations

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown(
    '<div class="title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Netflix-style AI Movie Recommendation Engine 🍿</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("🎥 Movie Selection")

movie_list = similarity_df.columns

selected_movie = st.sidebar.selectbox(
    "Choose Your Favorite Movie",
    movie_list
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    "🚀 Built using Collaborative Filtering + Cosine Similarity"
)

# -------------------------------------------------
# RECOMMEND BUTTON
# -------------------------------------------------
if st.button("🔥 Recommend Movies"):

    recommendations = recommend_movies(selected_movie)

    st.markdown(f"""
    <h2 style='text-align:center; margin-top:30px; color:white;'>
    Top Recommendations for: {selected_movie}
    </h2>
    """, unsafe_allow_html=True)

    cols = st.columns(5)

    for idx, movie in enumerate(recommendations):

        with cols[idx]:

            st.markdown(f"""
            <div class="movie-card">
                <h1>🎬</h1>
                <div class="movie-title">{movie}</div>
            </div>
            """, unsafe_allow_html=True)
# -------------------------------------------------
# POPULAR MOVIES
# -------------------------------------------------
st.markdown("---")

st.subheader("⭐ Most Popular Movies")

top_movies = (
    movie_data.groupby('title')['rating']
    .count()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_movies)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")

st.markdown("""
<center style='color:gray;'>
🚀 Developed by Ashraf Shikalgar
</center>
""", unsafe_allow_html=True)
