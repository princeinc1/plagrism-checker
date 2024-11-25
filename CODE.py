from difflib import SequenceMatcher
import sys

def print_similar_words(text1, text2):
    sequence_matcher = SequenceMatcher(None, text1.split(), text2.split())
    matches = sequence_matcher.get_matching_blocks()
    for match in matches:
        a, b, length = match
        words1 = text1.split()[a:a + length]
        words2 = text2.split()[b:b + length]
        print(f"Similar words: {words1}, {words2}")

def plagiarism_checker(text1, text2):
    if text1.strip() and text2.strip():
        text1 = text1.lower().split()
        text2 = text2.lower().split()
        sequence_matcher = SequenceMatcher(None, text1, text2)
        print(sequence_matcher)
        similarity_ratio = sequence_matcher.ratio()
        return similarity_ratio
    else:
        return 0

def accept_text_input():
    text1 = input("Enter first text:")
    text2 = input("\nEnter second text:")
    return text1, text2

def main():
    text1, text2 = accept_text_input()
    similarity_ratio = plagiarism_checker(text1, text2)
    average_length = (len(text1) + len(text2)) / 2
    normalized_similarity_ratio = similarity_ratio / average_length
    print(f"\nSimilarity ratio: {similarity_ratio * 100}%")
    if normalized_similarity_ratio > 30.0:
        print("The texts are very similar.")
        print_similar_words(text1, text2)
    elif normalized_similarity_ratio==0.0:
        print("The texts are not similar.")
        print_similar_words(text1, text2)
    else:
        print("The texts are less similar.")
        print_similar_words(text1, text2)

if __name__ == "__main__":
    main()