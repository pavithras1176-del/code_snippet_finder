# Source Code Snippet Finder

## Objective
A web-based Information Retrieval system that searches and ranks Python code snippets based on user-entered programming keywords using TF-IDF and Inverted Index techniques.

## Tools and Technologies
- Python
- Flask Framework
- TF-IDF (Term Frequency-Inverse Document Frequency)
- Inverted Index
- HTML

## Project Structure
```
irproject/
├── code_snippets/
│   ├── binary_search.py
│   ├── db_connection.py
│   ├── linear_search.py
│   ├── login_validation.py
│   ├── queue.py
│   └── stack.py
├── templates/
│   └── index.html
├── app.py
├── snippet_finder.py
├── requirements.txt
└── README.md
```

## Installation Steps
1. Clone the repository

2. Navigate to the project folder

3. Install dependencies

## How to Run
Open:
```
python app.py
```
Then open your browser and go to: http://127.0.0.1:5000

## How It Works
1. Enter a programming keyword in the search box (e.g. `queue`, `binary`, `login`)
2. The system searches through all stored Python code snippets
3. Results are ranked by TF-IDF relevance score
4. Click "Copy Snippet" to copy any result to clipboard
## END OF PROJECT