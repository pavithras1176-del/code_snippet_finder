import os
from flask import Flask, render_template, request
from snippet_finder import search, load_snippets

app = Flask(__name__)
# Load documents once when server starts
docs = load_snippets()

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form["query"].strip()
        raw_results = search(query, docs)

        # Show only relevant results (score > 0)
        for name, score in raw_results:
            if score > 0:

                path = os.path.join("code_snippets", name)

                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                results.append({
                    "name": name,
                    "score": round(score, 4),
                    "content": content
                })

    return render_template("index.html",
                           results=results,
                           query=query)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
