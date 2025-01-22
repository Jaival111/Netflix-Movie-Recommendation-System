import pandas as pd
import pickle
import streamlit as st

df = pickle.load(open('movie_dict.pkl', mode='rb'))
df = pd.DataFrame(df)
similarity = pickle.load(open('similarity.pkl', mode='rb'))

def recommend(movie):
    recommended_movies = []
    movie_index = df[df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movie_list:
        recommended_movies.append(df.iloc[i[0]].title)

    return recommended_movies

st.title('Netflix Movie Recommendation System')
selected_movie = st.selectbox('Choose your movie:', df['title'].values)
btn = st.button('Recommend')

if btn:
    movies_list = recommend(selected_movie)
    for movie in movies_list:
        st.write(movie)