from collections import defaultdict

# Sample input data: Each line represents a document with a unique ID
input_data = [
    "1: hello world",
    "2: hello mapreduce",
    "3: mapreduce is powerful",
    "4: world of mapreduce"
]

def mapper(input_data):
    """Map step: Emit (word, document_id) for each word in the document."""
    mapped_data = []
    for line in input_data:
        # Split the line into document ID and content
        doc_id, content = line.split(":", 1)
        doc_id = doc_id.strip()
        words = content.strip().split()  # Tokenize the content into words
        for word in words:
            mapped_data.append((word.lower(), doc_id))  # Emit (word, document_id)
    return mapped_data

def reducer(mapped_data):
    """Reduce step: Combine all document IDs for each word."""
    inverted_index = defaultdict(set)  # Use a set to avoid duplicate doc IDs
    for word, doc_id in mapped_data:
        inverted_index[word].add(doc_id)  # Add the doc_id to the set for the word

    # Convert sets to sorted lists for a clean output
    inverted_index = {word: sorted(list(doc_ids)) for word, doc_ids in inverted_index.items()}
    return inverted_index

# Map Step
mapped_data = mapper(input_data)

# Reduce Step
inverted_index = reducer(mapped_data)

# Output Results
print("Inverted Index:")
for word, doc_ids in inverted_index.items():
    print(f"{word}: {doc_ids}")