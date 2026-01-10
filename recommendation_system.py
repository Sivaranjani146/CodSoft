# CODSOFT - Artificial Intelligence Internship
# Task 4: Recommendation System (Content-Based Filtering)

# Movie database with genres
movies = {
    "Inception": "Sci-Fi",
    "Interstellar": "Sci-Fi",
    "The Matrix": "Sci-Fi",
    "Titanic": "Romance",
    "The Notebook": "Romance",
    "Avengers": "Action",
    "John Wick": "Action",
    "Gladiator": "Action",
    "Coco": "Animation",
    "Toy Story": "Animation"
}

def recommend_movies(preferred_genre):
    recommendations = []

    for movie, genre in movies.items():
        if genre.lower() == preferred_genre.lower():
            recommendations.append(movie)

    return recommendations

# Main program
print("MOVIE RECOMMENDATION SYSTEM")
print("Available genres: Sci-Fi, Romance, Action, Animation\n")

user_genre = input("Enter your preferred genre: ")

recommended_movies = recommend_movies(user_genre)

if recommended_movies:
    print("\nRecommended Movies for you:")
    for movie in recommended_movies:
        print("-", movie)
else:
    print("\nSorry, no movies found for this genre.")
