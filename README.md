# Music Recommendation Application

A Streamlit-based web application that provides personalized music recommendations using machine learning and the Spotify API.

## Overview

This project implements a music recommendation system that suggests similar songs based on user input. It uses:
- Machine learning to analyze song features and find similarities
- Spotify API to fetch song metadata and album artwork
- Streamlit for the web interface

## Project Structure

- `app.py`: The main Streamlit application that handles the user interface and recommendation logic
- `Model_training.ipynb`: Jupyter notebook containing the data preprocessing and model training code
- `df.pkl`: Pickled DataFrame containing processed song data
- `similarity.pkl`: Pickled similarity matrix used for recommendations
- `requirements.txt`: List of Python dependencies
- `spotify_millsongdata.csv`: Dataset containing song information

## Features

- Interactive song selection from a dropdown menu
- Display of album artwork for recommended songs
- Top 5 song recommendations based on similarity
- Integration with Spotify's extensive music catalog
- User-friendly web interface

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ashish0ct/Music_Recommendation_Application.git
   cd Music_Recommendation_Application
2. Install the required dependencies:
   ```shellscript
   pip install -r requirements.txtpip install -r requirements.txt
3. Run the Streamlit app:
   ```shellscript
   streamlit run app.pystreamlit run app.py

## How It Works

1. The application loads preprocessed song data and a pre-computed similarity matrix
2. Users select a song from the dropdown menu
3. When "Show Recommendation" is clicked, the system:
   - Finds similar songs using cosine similarity
   - Fetches album artwork using the Spotify API
   - Displays the top 5 recommendations with their artwork

## Technical Details
### Model Training (`Model_training.ipynb`)

- Data preprocessing and feature engineering
- Creation of similarity matrix using cosine similarity
- Model serialization using pickle

### Web Application (`app.py`)

- Streamlit for the web interface
- Spotify API integration using `spotipy`
- Recommendation logic implementation
- Dynamic fetching of album artwork

## Dependencies
Key packages used in this project:

- streamlit==1.27.2
- spotipy==2.23.0
- pandas==2.1.1
- scikit-learn==1.3.2
- numpy==1.26.1

For a complete list of dependencies, see `requirements.txt`.
