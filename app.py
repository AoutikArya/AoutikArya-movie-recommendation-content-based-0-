
import streamlit as st
import joblib
import requests
from urllib.request
import urlopen

st.title('Movie Recommendation System')

new_df=joblib.load('new_df.pkl')

def get_poster(movieid):
    response=requests.get(('https://api.themoviedb.org/3/movie/{}?api_key=e688210e49489266d056d2b4dc7da618&language=en-US').format(movieid))
    response=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+response['poster_path']


def recommend(movie):
    l=[]
    poster=[]
    mvidx=new_df[new_df.title==movie].index[0]
    distances=similarity[mvidx]
    mvlist=sorted(list(enumerate(distances)),reverse=True,key=lambda x : x[1])[1:6]

    for i in mvlist:
        l.append(new_df.iloc[i[0]].title)
        poster.append(new_df.iloc[i[0]].id)
    return l,poster

movie_poster=[]

movie_selected = st.selectbox('Select a movie',(new_df['title'].values))

similarity = joblib.load(urlopen("https://drive.google.com/file/d/15V8uSdHisS4dSUSs1-8sSYqKc7jG-QU7/view?usp=sharing"))
#similarity=joblib.load('similarity.pkl')

if st.button("Recommend"):
    recomm,id=recommend(movie_selected)
    for i in id:
        movie_poster.append(get_poster(i))

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.write(recomm[0])
        st.image(movie_poster[0])

    with col2:
        st.write(recomm[1])
        st.image(movie_poster[1])

    with col3:
        st.write(recomm[2])
        st.image(movie_poster[2])
    with col4:
        st.write(recomm[3])
        st.image(movie_poster[3])
    with col5:
        st.write(recomm[4])
        st.image(movie_poster[4])


import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f'''
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    ''',
    unsafe_allow_html=True
    )
add_bg_from_local('1.jpg')


