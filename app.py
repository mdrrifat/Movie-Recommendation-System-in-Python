import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=d19d3cc4d91e40419810d3f5253bb384&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    
    full_path = "https://image.tmdb.org/t/p/w500" + data['poster_path']
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1]) [1:11]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        # fetch the movie poster
        movie_id=movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

st.header('[ Movie Recommendation System ]')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie",
    movies['title'].values
)


if st.button('Recommendation'):
    recommended_movies,recommended_movies_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])
    with col6:
        st.text(recommended_movies[5])
        st.image(recommended_movies_posters[5])
    with col7:
        st.text(recommended_movies[6])
        st.image(recommended_movies_posters[6])
    with col8:
        st.text(recommended_movies[7])
        st.image(recommended_movies_posters[7])
    with col9:
        st.text(recommended_movies[8])
        st.image(recommended_movies_posters[8])
    with col10:
        st.text(recommended_movies[9])
        st.image(recommended_movies_posters[9])