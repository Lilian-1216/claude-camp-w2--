import string
from collections import Counter

# Common English stop words
STOP_WORDS = {"the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
              "be", "been", "being", "to", "of", "in", "on", "at", "for", "with",
              "by", "from", "as", "it", "this", "that", "these", "those",
              "i", "you", "he", "she", "we", "they", "my", "your", "his", "her",
              "me", "him", "us", "them", "its", "our", "their",
              "do", "does", "did", "have", "has", "had", "will", "would",
              "can", "could", "should", "may", "might", "shall", "if", "then",
              "so", "not", "no", "yes", "up", "down", "out", "over", "under"}

text = input("Enter your English text:\n")

# 1. Normalize: lowercase + remove punctuation
text = text.lower()
for p in string.punctuation:
    text = text.replace(p, " ")

# 2. Split into words
words = text.split()

# 3. Filter: remove stop words and single-letter words
words = [w for w in words if w not in STOP_WORDS and len(w) > 1]

# 4. Count
word_count = Counter(words)

# 5. Show Top 10
print("\nTop 10 most frequent words:\n")
for word, count in word_count.most_common(10):
    print(f"{word}: {count}")