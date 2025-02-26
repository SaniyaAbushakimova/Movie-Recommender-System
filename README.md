# Movie-Recommender-System

## Project Overview

This project is a Movie Recommender System that leverages **collaborative filtering techniques** to generate personalized movie recommendations. It is built using the **MovieLens dataset**, which includes approximately **1 million ratings** from **6,040 users** for **3,706 movies**, providing a rich foundation for analyzing user preferences and movie similarities.

The recommender system is implemented from scratch, focusing on two key recommendation strategies:
1. **Popularity-Based Recommendation** – Recommends movies based on overall popularity.
2. **Item-Based Collaborative Filtering (IBCF)** – Uses similarity between movies to generate personalized recommendations for users.

Additionally, a **Movie Recommender Web App** was built to provide an interactive interface for users to explore and receive movie recommendations.

See Movie Recommender Web App demo below:

https://github.com/user-attachments/assets/f8afa8af-f9bc-43cc-a69f-87c63ba60f40


## Repository Contents

`Movie-Recommender-System.ipynb` - Jupyter Notebook containing the implementation of the recommender system, including data preprocessing, model development, and evaluation.
`Instructions.pdf` - Project details and problem statement.
`Rmat.csv` - User-movie rating matrix generated from the MovieLens dataset, used as the input for collaborative filtering.
`similarity_matrix.csv` - Precomputed similarity scores between movies, used for item-based collaborative filtering.
`top_10_movies.csv` - A list of the top 10 most recommended movies for each user based on the model’s predictions.
`ml-1m/` - Folder containing the MovieLens 1M dataset, which includes user ratings, movie metadata, and user demographic information.
`Movie-Recommender-App/` - Folder containing the Dash web application that allows users to explore movie recommendations interactively.
  * `app.py` - The main Dash application that serves the web interface for recommendations.
  * `myfuns.py` - Contains helper functions for generating recommendations based on precomputed similarity scores.
  * `popular_movies.csv` - A dataset containing the most popular movies based on rating frequency and scores.
  * `S_top_30.csv` - A dataset containing similarity scores for the top 30 most similar movies for each title.
  * `requirements.txt` - A list of required Python libraries to run the Dash app.

## How to Run the Web App

1. **Install Dependencies:**
   
`pip install -r requirements.txt`

2. **Run the Dash App:**
   
`python app.py`

## Dataset Details
