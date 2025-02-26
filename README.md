# Movie-Recommender-System

Project completed on December 9, 2024.

## Project Overview

This project is a Movie Recommender System that leverages **collaborative filtering techniques** to generate personalized movie recommendations. It is built using the **MovieLens dataset**, which includes approximately **1 million ratings** from **6,040 users** for **3,706 movies**, providing a rich foundation for analyzing user preferences and movie similarities.

The recommender system is implemented from scratch, focusing on two key recommendation strategies:
1. **System 1: Popularity-Based Recommendation** – Recommends movies based on overall popularity.
2. **System 2: Item-Based Collaborative Filtering (IBCF)** – Uses similarity between movies to generate personalized recommendations for users.

Additionally, a **Movie Recommender Web App** was built to provide an interactive interface for users to explore and receive movie recommendations.

See Movie Recommender Web App demo below:

https://github.com/user-attachments/assets/f8afa8af-f9bc-43cc-a69f-87c63ba60f40


## Repository Contents

* `Movie-Recommender-App/` - Folder containing the Dash web application that allows users to explore movie recommendations interactively.
  * `app.py` - The main Dash application that serves the web interface for recommendations.
  * `myfuns.py` - Contains helper functions for generating recommendations based on precomputed similarity scores.
  * `popular_movies.csv` - A dataset containing the most popular movies based on rating frequency and scores.
  * `S_top_30.csv` - A dataset containing similarity scores for the top 30 most similar movies for each title.
  * `requirements.txt` - A list of required Python libraries to run the Dash app.
* `MovieImages/` - Folder containing movie posters used in the recommendations web app.
* `ml-1m/` - Folder containing the MovieLens 1M dataset, which includes user ratings, movie metadata, and user demographic information.
  * `movies.dat` - Includes movie title, release year, and genres.
  * `ratings.dat` - 1,000,209 anonymous ratings from 6,040 users on 3,706 movies.
  * `users.dat` -  Gender, age, occupation, and zip code.
* `Instructions.pdf` - Project details and problem statement.
* `Movie-Recommender-System.ipynb` - Jupyter Notebook containing the implementation of the recommender system, including data preprocessing, model development, and evaluation.
* `Rmat.csv` - User-movie rating matrix generated from the MovieLens dataset used as the input for IBCF.
* `top_10_movies.csv` - A list of the top 10 most recommended movies for each user based on Popularity-Based Recommendation.
* `similarity_matrix.csv` - Precomputed similarity scores between movies, used for IBCF. [Download here](https://drive.google.com/file/d/142abx3DEtxWVGX4cVKAKlrKbF1JRJLP0/view?usp=sharing)

## Methods and Techniques Used

1. **Data Preprocessing**
 * Constructed a user-movie rating matrix from raw MovieLens ratings.
 * Normalized ratings by centering each row to adjust for user rating biases.
 * Removed movies with very few ratings to improve model efficiency.

2. **Popularity-Based Recommendation**
 * Ranked movies based on the number of user ratings, considering only those with an average rating above 4.3.
 * Recommended the top 10 most popular movies to all users.

3. **Item-Based Collaborative Filtering (IBCF)**
 * Computed a movie similarity matrix using cosine similarity.
 * Only retained the top 30 most similar movies for each title to enhance efficiency.
 * Used similarity scores to generate personalized recommendations for users based on their watched movies.

4. **Web Application**
 * Developed an interactive Dash web app where users can rate movies and receive recommendations.
 * The app leverages precomputed similarity scores for fast, real-time recommendations.

## How to Run the Web App

1. **Install Dependencies:**
   
`pip install -r requirements.txt`

2. **Run the Dash App:**
   
`python app.py`
