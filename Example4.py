from collections import defaultdict
from heapq import nlargest

# Sample input: Lines from a text file
input_data = [
    "hello world hello mapreduce",
    "mapreduce is powerful",
    "hello world of mapreduce",
    "world mapreduce hello"
]

def mapper(input_data):
    """Map step: Emit (word, 1) for each word."""
    mapped_data = []
    for line in input_data:
        words = line.strip().split()  # Tokenize the line into words
        for word in words:
            mapped_data.append((word.lower(), 1))  # Emit (word, 1)
    return mapped_data

def reducer(mapped_data):
    """Reduce step: Sum the occurrences of each word."""
    word_counts = defaultdict(int)
    for word, count in mapped_data:
        word_counts[word] += count  # Aggregate counts for each word
    return word_counts

def top_n_words(word_counts, n):
    """Find the top N most frequent words."""
    # Use a heap to get the N largest items based on word frequencies
    return nlargest(n, word_counts.items(), key=lambda x: x[1])

# Map Step
mapped_data = mapper(input_data)

# Reduce Step
word_counts = reducer(mapped_data)

# Get Top-N Words (e.g., Top 3 Words)
N = 3
top_words = top_n_words(word_counts, N)

# Output Results
print(f"Top {N} words:")
for word, count in top_words:
    print(f"{word}: {count}")