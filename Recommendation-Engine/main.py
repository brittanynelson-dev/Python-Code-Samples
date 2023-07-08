import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# User-item matrix representing the ratings
user_item_matrix = np.array([
    [5, 3, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 4, 0],
    [0, 0, 4, 0, 0, 0, 2],
])

# Calculate the similarity matrix using cosine similarity
similarity_matrix = cosine_similarity(user_item_matrix)

# Function to get top N similar users for a given user
def get_similar_users(user_id, N):
    user_similarity = similarity_matrix[user_id]
    similar_users = np.argsort(user_similarity)[::-1][1:N+1]
    return similar_users

# Function to get top N recommended items for a given user
def get_recommendations(user_id, N):
    similar_users = get_similar_users(user_id, N)
    user_ratings = user_item_matrix[user_id]
    recommendations = np.zeros(user_item_matrix.shape[1])
    
    for similar_user in similar_users:
        similar_user_ratings = user_item_matrix[similar_user]
        recommendations += similar_user_ratings

    recommendations[user_ratings.nonzero()] = 0  # Exclude already rated items
    sorted_indices = np.argsort(recommendations)[::-1]
    top_recommendations = sorted_indices[:N]
    return top_recommendations

# Example usage
user_id = 0
top_recommendations = get_recommendations(user_id, 3)
print(f"Top recommendations for User {user_id}: {top_recommendations}")
