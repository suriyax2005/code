import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = {
    'title': ['The Matrix', 'John Wick', 'The Godfather', 'Toy Story', 'Finding Nemo', 'Avengers','12th Fail','Final Destination'],
    'genre': ['Action Sci-Fi', 'Action Thriller', 'Crime Drama', 'Animation Comedy', 'Animation Adventure', 'Action Superhero','Educational','Twisted']
}

df = pd.DataFrame(data)


vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(df['genre'])


cosine_sim = cosine_similarity(genre_matrix, genre_matrix)


def recommend(movie_title, df, similarity_matrix):
    if movie_title not in df['title'].values:
        return f"Movie '{movie_title}' not found in database."

    idx = df[df['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_movies = [df['title'][i] for i, score in similarity_scores[1:4]]
    return top_movies


user_input = input("Enter the movie you like: ")
recommendations = recommend(user_input, df, cosine_sim)

print(f"Because you liked '{user_input}', you might also like:")
for rec in recommendations:
    print(f"- {rec}")
