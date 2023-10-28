# Plagarism-Checker

#A plagiarism checker is a software application that detects plagiarism in text. 
#Plagiarism is the act of copying someone else's work and passing it off as your own. 
#Plagiarism checkers are used by students, educators, writers, and researchers to ensure that their work is original.
import re
import math

# Preprocessing functions
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    words = text.split()
    stop_words = set(["the", "and", "in", "to", "of"])  # Define your list of stop words here
    words = [word for word in words if word not in stop_words]
    return words

def cosine_similarity(vector1, vector2):
    intersection = set(vector1) & set(vector2)
    numerator = sum(vector1[word] * vector2[word] for word in intersection)
    sum1 = sum(vector1[word] ** 2 for word in vector1)
    sum2 = sum(vector2[word] ** 2 for word in vector2)
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

# Example usage
input_text = "Your input text goes here."
database_text = "A known source text from your database."

input_words = preprocess_text(input_text)
database_words = preprocess_text(database_text)

input_vector = {word: input_words.count(word) for word in input_words}
database_vector = {word: database_words.count(word) for word in database_words}

similarity = cosine_similarity(input_vector, database_vector)
print(f"Cosine Similarity: {similarity}")
