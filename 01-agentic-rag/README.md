## Homework 1: Agentic RAG

### Question 1. How many lesson pages?
Here is the script to count the total number of lesson pages in the dataset:

```python
from gitsource import GithubRepositoryDataReader

# Fetch the files using your existing configuration
reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

files = reader.read()

# Print the total number of lesson pages found
print(f"Total lesson pages: {len(files)}")