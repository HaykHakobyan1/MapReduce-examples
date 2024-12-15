from collections import defaultdict

# Sample input: Multiple lines of text
input_data = [
    "hello world",
    "hello mapreduce",
    "mapreduce is powerful",
    "world of mapreduce"
]

def mapper(input_data):
    """Map step: Emit (word, 1) for each word in the input."""
    mapped_data = []
    for line in input_data:
        words = line.strip().split()  # Tokenize the line into words
        for word in words:
            mapped_data.append((word.lower(), 1))  # Emit (word, 1) for each word
    return mapped_data

def reducer(mapped_data):
    """Reduce step: Sum the occurrences of each word."""
    word_counts = defaultdict(int)
    for word, count in mapped_data:
        word_counts[word] += count  # Aggregate word counts
    return word_counts

# Map Step
mapped_data = mapper(input_data)

# Reduce Step
word_counts = reducer(mapped_data)

# Output Results
print("Word Count Results:")
for word, count in word_counts.items():
    print(f"{word}: {count}")