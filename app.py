import streamlit as st
import pickle
import requests

# Load movie data and similarity matrix
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values  # Extract movie titles

# TMDb API key
API_KEY = "cd69d02c3ebeeeec2925a88847fe0969"

# Function to fetch movie poster from TMDb
def fetch_poster(movie_name):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(search_url).json()
    
    if response.get("results"):
        poster_path = response["results"][0].get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:  # Get top 5 recommendations
        movie_name = movies.iloc[i[0]].title
        recommended_movies.append(movie_name)
        recommended_posters.append(fetch_poster(movie_name))  # Fetch poster
    
    return recommended_movies, recommended_posters

# Streamlit UI
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .stApp {
        background-image: url("https://png.pngtree.com/thumb_back/fw800/background/20240926/pngtree-overhead-shot-of-dark-modern-workplace-with-copy-space-image_16250595.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        animation: fadeIn 2s ease-in-out;
    }
    .title {
        font-size: 2.5em;  /* Increased title size */
        font-weight: bold;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.7);
        text-align: center;
        color: #ffffff;
    }
    .select-text {
        font-size: 1.8em;  /* Increased font size */
        font-weight: bold;
        color: white;
        text-align: center;
        margin-bottom: 15px;
    }
    .movie-card {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s;
        text-align: center;
    }
    .movie-card:hover {
        transform: scale(1.05);
    }
    .movie-title {
        font-size: 10em;  /* Increased font size for movie names */
        font-weight: bold;
        color: white;
        text-align: center;
        margin-top: 10px;
    }
    .stSelectbox div[data-baseweb="select"] {
        border: 2px solid white !important;
        border-radius: 10px;
        font-size: 1.2em;
        color: white !important;
        background-color: rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease-in-out;
    }
    .stSelectbox div[data-baseweb="select"]:hover {
        border-color: #ffcc00 !important;
        background-color: rgba(255, 255, 255, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🎬 MOVIE RECOMMENDER SYSTEM</div>', unsafe_allow_html=True)

# Custom styled "Select a movie" text with bigger font
st.markdown('<p class="select-text">🎥 Select a movie:</p>', unsafe_allow_html=True)

selected_movie = st.selectbox("", movies_list)  # Keeping label empty since we added custom styled text

# Show recommendations when button is clicked
if st.button("Show Recommendations"):
    movie_names, movie_posters = recommend(selected_movie)
    
    cols = st.columns(5)  # Create 5 columns for layout
    
    for idx, col in enumerate(cols):
        with col:
            st.markdown(f'<div class="movie-card">', unsafe_allow_html=True)
            st.markdown(f'<p class="movie-title">{movie_names[idx]}</p>', unsafe_allow_html=True)  # Styled movie name
            if movie_posters[idx]:
                st.image(movie_posters[idx], use_container_width=True)
            else:
                st.text("Poster not available")
            st.markdown('</div>', unsafe_allow_html=True)

