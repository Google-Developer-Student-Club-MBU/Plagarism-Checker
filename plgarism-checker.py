import re
import math
from collections import Counter

def preprocess_text(text):
    # Tokenize and preprocess the text
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    words = text.split()
    return Counter(words)

def cosine_similarity(vec1, vec2):
    # Calculate the cosine similarity between two text vectors
    intersection = set(vec1) & set(vec2)
    numerator = sum(vec1[word] * vec2[word] for word in intersection)
    sum1 = sum(vec1[word] ** 2 for word in vec1)
    sum2 = sum(vec2[word] ** 2 for word in vec2)
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def check_plagiarism(input_text, known_sources):
    input_vector = preprocess_text(input_text)
    plagiarism_matches = []

    for source_name, source_text in known_sources.items():
        source_vector = preprocess_text(source_text)
        similarity = cosine_similarity(input_vector, source_vector)
        
        if similarity > 0.7:  # You can adjust the threshold
            plagiarism_matches.append((source_name, similarity))

    return plagiarism_matches

if __name__ == "__main__":
    # Sample known sources (you should have a database)
    known_sources = {
        "Source1": "This is a known source text.",
        "Source2": "Another known source for testing plagiarism.",
    }

    # Input text to check for plagiarism
    input_text = "This is a known source text with a slight variation."

    plagiarism_matches = check_plagiarism(input_text, known_sources)

    if plagiarism_matches:
        print("Plagiarism Detected:")
        for source_name, similarity in plagiarism_matches:
            print(f"Source: {source_name}, Similarity: {similarity}")
    else:
        print("No plagiarism detected.")
