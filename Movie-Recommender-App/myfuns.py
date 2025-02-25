import pandas as pd
import numpy as np
import requests

# Define the URL for movie data
myurl = "https://liangfgithub.github.io/MovieData/movies.dat?raw=true"

# Fetch the data from the URL
response = requests.get(myurl)

# Split the data into lines and then split each line using "::"
movie_lines = response.text.split('\n')
movie_data = [line.split("::") for line in movie_lines if line]

# Create a DataFrame from the movie data
movies = pd.DataFrame(movie_data, columns=['movie_id', 'title', 'genres'])
movies['movie_id'] = movies['movie_id'].astype(int)

# Use entire list of popular movies since this is needed for ICBF & System 1
popular_movies = pd.read_csv("popular_movies.csv").rename(columns={"MovieID": "movie_id", "Title": "title"})
popular_movies['m_movie_id'] = 'm' + popular_movies['movie_id'].astype(str)

# Loading Similarity matrix
S = pd.read_csv("S_top_30.csv")
S = S.set_index('Unnamed: 0')

def get_displayed_movies():
    return movies.head(100)

def get_recommended_movies(new_user_ratings):
    # Do ICBF function things here 
    user_ratings_df = pd.DataFrame(np.nan, columns=S.columns, index=[0])
    for movie_id, rating in new_user_ratings.items():
        user_ratings_df[f"m{movie_id}"] = rating

    
    new_user_ratings = user_ratings_df.loc[0]
    new_user_recs = myIBCF(new_user_ratings)

    recommended_movie_ids = [int(movie_id[1:]) for movie_id in new_user_recs.index]
    recommended_movies_df = movies[movies['movie_id'].isin(recommended_movie_ids)]
    recommended_movies_df = recommended_movies_df.set_index('movie_id')
    
    recommended_movies_df = recommended_movies_df.loc[recommended_movie_ids].reset_index() 

    return recommended_movies_df

def get_popular_movies():
    # System 1
    return popular_movies.head(10)

# Helper functions 

# Helper function to handle edge case: If fewer than 10 predictions are non-NA,
# select the remaining movies based on the popularity defined in System 1.
def handle_edge_case(top_predictions, w, n, non_na_size):

  remainder = n - non_na_size

  rated_movies = w.dropna().index
  unrated_movies = []

  for movie in popular_movies['m_movie_id']:
      if movie not in rated_movies:
          unrated_movies.append(movie)

  additional_movies = pd.Series(data=["Recommended"] * remainder, index=unrated_movies[:remainder])

  # Add additional movies to predictions
  top_predictions = pd.concat([top_predictions, additional_movies])

  return top_predictions

def myIBCF(w, n=10):

  predictions = pd.Series(index=w.index, dtype=float)

  for movie_id in predictions.index:

      # Skip already-rated movies
      if not pd.isna(w[movie_id]):
          predictions[movie_id] = np.nan
          continue

      # Retrieve similarity scores for this movie
      S_movie = S.loc[movie_id]

      # Filter for movies rated by the user
      rated_movies = w.dropna()
      relevant_similarities = S_movie[rated_movies.index]

      # Compute weighted average of ratings
      weighted_sum = (relevant_similarities * rated_movies).sum()
      similarity_sum = np.abs(relevant_similarities).sum()

      # Compute predicted rating if denominator is nonzero
      if similarity_sum > 0:
          predictions[movie_id] = weighted_sum / similarity_sum
      else:
          predictions[movie_id] = np.nan

  # Select the top N predictions
  top_predictions = predictions.nlargest(n)
  top_predictions.name = "predictions"

  # EDGE CASE: if number of non-NA values < n
  non_na_size = top_predictions.notna().sum().sum()

  # Fill NA with movies from popular movies list that were not rated by the user
  if non_na_size < n:
    return handle_edge_case(top_predictions[top_predictions.notna()], w, n, non_na_size)

  return top_predictions
