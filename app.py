import pickle
# streamlit is an open-source, easy to create and share beautiful, custom web apps for machine learning. 
import streamlit as st
# allows you to access the spotify API. 
import spotipy 
# This class is used to authenticate requests to the spotify API using Client Credentials flow. 
# This type of authentication does not require a user to log-in. 
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "415f182e672c4383912824d020067b3c"
CLIENT_SECRET = "251aaf026a724a65a63137fd58d0cae6"

# Initialize the Spotify client
# used to authenticate requests to the Spotify API using the Client Credentials flow. 
# This flow is specifically designed for applications that need to access Spotify's data without requiring user authorization.
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# This object is used to interact with the Spotify API and access its vast music caatlog.  
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        # if no album cover found then this default spotify logo used instead. 
        return "https://i.postimg.cc/0QNxYz4V/social.png"
    
def recommend(song):
    index = music[music['song'] == song].index[0]
    # This line calculates the cosine similarity scores between the input song and all other songs. 
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    # similar songs. 
    recommended_music_names = []
    recommended_music_posters = []
    # top 5 songs.
    for i in distances[1:6]:
        # fetch the song poster
        artist = music.iloc[i[0]].artist 
        # print astist name in console. 
        print(artist)
        print(music.iloc[i[0]].song)
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)
        
    return recommended_music_names, recommended_music_posters

st.header('Music Recommender System')
# load df.pkl to music
music = pickle.load(open('df.pkl', 'rb'))
# load similarity.pkl to similarity
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = music['song'].values
selected_movie = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])
    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])