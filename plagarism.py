import re
from collections import Counter
from difflib import SequenceMatcher

# Database of known sources
known_sources = {
    "source1": "This is the content of source 1.",
    "source2": "This is the content of source 2.",
    # Add more sources as needed
}

def preprocess_text(text):
    # Tokenize and preprocess the text
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = text.split()
    return Counter(words)

def calculate_similarity(text1, text2):
    # Calculate the similarity ratio between two texts
    similarity = SequenceMatcher(None, text1, text2).ratio()
    return similarity

def check_for_plagiarism(input_text, threshold=0.8):
    input_text = preprocess_text(input_text)

    # Initialize a report
    plagiarism_report = {}

    for source_name, source_text in known_sources.items():
        source_text = preprocess_text(source_text)
        similarity = calculate_similarity(input_text, source_text)

        if similarity >= threshold:
            plagiarism_report[source_name] = similarity

    return plagiarism_report

if __name__ == "__main__":
    input_text = "This is a sample text that may contain plagiarism."
    plagiarism_report = check_for_plagiarism(input_text)

    if plagiarism_report:
        print("Plagiarism Detected:")
        for source, similarity in plagiarism_report.items():
            print(f"Source: {source}, Similarity: {similarity}")
    else:
        print("No plagiarism detected.")
