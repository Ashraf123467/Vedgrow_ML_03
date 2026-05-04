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

/* Fonts */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main Title */
.title {
    text-align: center;
    font-size: 70px;
    font-weight: 800;
    color: white !important;
    margin-top: 20px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 24px;
    color: #e2e8f0 !important;
    margin-bottom: 25px;
}

/* Recommendation Technique */
.technique {
    text-align: center;
    font-size: 22px;
    color: #cbd5e1 !important;
    margin-top: 20px;
    margin-bottom: 25px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Selectbox */
.stSelectbox label {
    color: white !important;
}

/* Dropdown Styling */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #0f172a !important;
    color: white !important;
}

/* Movie Cards */
.movie-card {
    background: linear-gradient(145deg,#111827,#1e293b);
    padding: 15px;
    border-radius: 18px;
    text-align: center;
    color: white !important;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.5);
}

/* Movie Titles */
.movie-title {
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
    color: white !important;
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(135deg,#dc2626,#991b1b);
    color: white !important;
    border: none;
    border-radius: 12px;
    height: 55px;
    font-size: 20px;
    font-weight: bold;
}

/* Images */
img {
    border-radius: 15px;
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

    collaborative_scores = similarity_df[movie_name].sort_values(
        ascending=False
    )[2:n+2]

    recommendations = collaborative_scores.index.tolist()

    posters = []

    for movie in recommendations:

        posters.append(fetch_poster(movie))

    return recommendations, posters

# -------------------------------------------------
# FETCH MOVIE POSTER (GENERALIZED VERSION)
# -------------------------------------------------
def fetch_poster(movie_name):

    api_key = "59719fce3e3e7376212d15ea32321f78"

    try:

        # Clean movie title
        clean_name = movie_name.split('(')[0].strip()

        # TMDB API URL
        url = (
            f"https://api.themoviedb.org/3/search/movie"
            f"?api_key={api_key}"
            f"&query={clean_name}"
        )

        response = requests.get(url, timeout=10)

        # If API request fails
        if response.status_code != 200:
            return None

        data = response.json()

        # Check results exist
        if (
            "results" in data and
            len(data["results"]) > 0
        ):

            poster_path = data["results"][0].get("poster_path")

            # If poster exists
            if poster_path:

                return (
                    "https://image.tmdb.org/t/p/w500"
                    + poster_path
                )

        # If no poster found
        return None

    except Exception:

        return None

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

st.markdown("""
<div style="
text-align:center;
color:#94a3b8;
font-size:18px;
margin-bottom:25px;
">

🤖 Recommendation Technique Used:
<b style='color:#38bdf8;'>
Collaborative Filtering + Cosine Similarity
</b>

</div>
""", unsafe_allow_html=True)
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

    recommendations, posters = recommend_movies(selected_movie)

    st.markdown(f"""
    <h2 style='text-align:center; margin-top:30px; color:white;'>
    Top Recommendations for: {selected_movie}
    </h2>
    """, unsafe_allow_html=True)

    cols = st.columns(5)

    for idx in range(len(recommendations)):

        with cols[idx]:

            st.markdown(
                '<div class="movie-card">',
                unsafe_allow_html=True
            )

            # Show movie poster
            if posters[idx]:

                st.image(
                    posters[idx],
                    use_container_width=True
                )

            else:

                st.markdown("""
                <div style="
                    height:320px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    background:#1e293b;
                    border-radius:15px;
                    color:white;
                    font-size:70px;
                ">
                🎬
                </div>
                """, unsafe_allow_html=True)

            # Movie title
            st.markdown(
                f"""
                <div class='movie-title'>
                    {recommendations[idx]}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )
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
