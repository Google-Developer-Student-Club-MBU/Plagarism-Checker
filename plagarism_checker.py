import difflib

def compare_texts(text1, text2):
    """
    Compare two texts and identify similar passages.
    :param text1: The first text to compare.
    :param text2: The second text to compare against.
    :return: A list of tuples containing the start and end positions of similar passages.
    """
    d = difflib.Differ()
    diff = list(d.compare(text1.split(), text2.split()))
    
    similar_passages = []
    start, end = 0, 0
    in_passage = False
    
    for line in diff:
        if line.startswith('  '):  # This line is common in both texts
            if not in_passage:
                start = end
            end += len(line.split())
            in_passage = True
        else:
            if in_passage:
                similar_passages.append((start, end))
            in_passage = False
            end += len(line.split())
    
    if in_passage:
        similar_passages.append((start, end))
    
    return similar_passages

def main():
    text1 = "This is an example text. It can be used for testing."
    text2 = "This is a sample text. It is suitable for testing purposes."
    
    similar_passages = compare_texts(text1, text2)
    
    if similar_passages:
        print("Plagiarism Detected in the following passages:")
        for start, end in similar_passages:
            print(" ".join(text1.split()[start:end]))
    else:
        print("No plagiarism detected.")

if __name__ == "__main__":
    main()
