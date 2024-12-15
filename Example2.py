from collections import defaultdict

# Sample input file as a list of strings (each line is a number)
input_data = [
    "10",
    "20",
    "30",
    "40",
    "50"
]

def mapper(input_data):
    """Map step: Emit (1, value) for each line."""
    mapped_data = []
    for line in input_data:
        value = float(line.strip())  # Convert the line to a numeric value
        mapped_data.append((1, value))  # Emit (1, value)
    return mapped_data

def reducer(mapped_data):
    """Reduce step: Aggregate values and count to calculate average."""
    total_value = 0
    total_count = 0

    for _, value in mapped_data:
        total_value += value  # Sum all values
        total_count += 1      # Count each occurrence

    average = total_value / total_count if total_count != 0 else 0  # Compute average
    return average

# Map Step
mapped_data = mapper(input_data)

# Reduce Step
average = reducer(mapped_data)

# Output Results
print(f"The average of the dataset is: {average}")