
# MapReduce Examples in Python

This repository contains Python implementations of various MapReduce exercises. The goal is to demonstrate how to process data in a distributed fashion using the Map and Reduce paradigm. Each example focuses on a different data processing task.

---


 1. Word Count

Objective:
Count the occurrences of each word in a text dataset.

Input:
A text file with multiple lines of text, where each line contains multiple words.

Steps:
1. Map: Split each line into words and emit `(word, 1)` for each word.
2. Reduce: Sum all the occurrences for each word to get total occurrences.

Explanation:
In this exercise, each word is treated as a key, and its occurrence in the dataset is counted. The `Map` step emits a key-value pair `(word, 1)` for each occurrence, and the `Reduce` step aggregates all the counts for each word to give the final total count for each word.

---

 2. Average Calculation

Objective:
Calculate the average of numbers in a dataset.

Input:
A file where each line contains a numeric value.

Steps:
1. Map: Emit `(1, value)` for each line.
2. Reduce: Aggregate the values and divide by the total count to compute the average.

Explanation:
In this exercise, the map function emits the number `1` along with each value from the dataset to count the total number of values. The reduce step aggregates the sum of the values and counts the occurrences, and then computes the average by dividing the sum by the count.

---

 3. Inverted Index

Objective:
Create an inverted index for words in a document.

Input:
A dataset with multiple documents (each line is a document with an ID).

Steps:
1. Map: Emit `(word, document_id)` for each word in the document.
2. Reduce: Combine all document IDs for each word.

Explanation:
This task involves creating an index that maps each word to the set of document IDs in which the word appears. In the map step, for each word in each document, a pair `(word, document_id)` is emitted. The reduce step aggregates all the document IDs for each word to create the final inverted index.

---

 4. Top-N Words

Objective:
Find the top N most frequent words in a text file.

Input:
A text file with multiple lines of text.

Steps:
1. Map: Split the text into words and emit `(word, 1)` for each word.
2. Reduce: Sum the occurrences of each word.
3. Sort: Sort the result by frequency and pick the top N words.

Explanation:
In this exercise, the map step emits `(word, 1)` for each word, and the reduce step aggregates the total count for each word. After reducing, the words are sorted by their frequency, and the top N words are selected.

---

 5. Product Sales Analysis

Objective:
Calculate the total sales for each product.

Input:
A dataset where each line contains `product_id`, `quantity`, and `price`.

Steps:
1. Map: Emit `(product_id, quantity * price)` for each line.
2. Reduce: Sum the total sales for each product.

Explanation:
In this exercise, for each product, we calculate its total sales by multiplying the quantity by the price. The map function emits a pair `(product_id, total_sale)`, and the reduce step aggregates the total sales for each product by summing up all the individual sales amounts.

---
