import os
import math
from collections import defaultdict, Counter


# ===== LOAD FILES =====
def load_snippets():
    folder = "code_snippets"
    docs = {}

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # include filename words also
        docs[filename] = filename.replace("_", " ") + " " + content

    return docs


# ===== TOKENIZE =====
def tokenize(text):
    symbols = ['(', ')', '{', '}', ':', ';', ',', '.', '\n', '\t', '_']
    for s in symbols:
        text = text.replace(s, ' ')

    return text.lower().split()


# ===== TF =====
def compute_tf(tokens):
    count = Counter(tokens)
    total = len(tokens)

    tf = {}
    for w, c in count.items():
        tf[w] = c / total

    return tf


# ===== IMPROVED IDF =====
def compute_idf(all_tokens):
    N = len(all_tokens)
    idf = {}

    vocab = set()
    for tokens in all_tokens:
        vocab.update(tokens)

    for term in vocab:
        df = sum(1 for tokens in all_tokens if term in tokens)

        # SMOOTHED IDF (important for small dataset)
        idf[term] = math.log((N + 1) / (df + 1)) + 1

    return idf


# Processes the user query and returns ranked results
def search(query, docs):
    q_tokens = tokenize(query)

    docs_tokens = [tokenize(t) for t in docs.values()]

    idf = compute_idf(docs_tokens)

    results = []

    for (name, text), tokens in zip(docs.items(), docs_tokens):

        tf = compute_tf(tokens)

        score = 0
        for t in q_tokens:
            score += tf.get(t, 0) * idf.get(t, 0)

        results.append((name, round(score, 4)))

    return sorted(results, key=lambda x: x[1], reverse=True)


# ===== MAIN =====
if __name__ == "__main__":

    docs = load_snippets()

    print("=== System Ready ===")

    query = input("\nEnter programming keyword: ")

    results = search(query, docs)

    print("\n=== Ranked Snippets ===")
    for name, score in results:
        print(name, " --> ", score)
