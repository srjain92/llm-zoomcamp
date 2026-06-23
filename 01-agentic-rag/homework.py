# import minsearch
# from gitsource import GithubRepositoryDataReader

# # 1. Fetch files from repository
# reader = GithubRepositoryDataReader(
#     repo_owner="DataTalksClub",
#     repo_name="llm-zoomcamp",
#     commit_id="8c1834d",
#     allowed_extensions={"md"},
#     filename_filter=lambda path: "/lessons/" in path,
# )

# files = reader.read()

# # 2. Parse raw repository markdown files into dictionaries 
# # The .parse() method maps the file path to 'filename' and contents to 'content'
# documents = []
# for file in files:
#     doc = file.parse()
#     documents.append(doc)

# # 3. Initialize minsearch Index
# index = minsearch.Index(
#     text_fields=["content"],
#     keyword_fields=["filename"]
# )

# # 4. Index documents
# index.fit(documents)

# # 5. Query the index
# query = "How does the agentic loop keep calling the model until it stops?"
# search_results = index.search(
#     query=query,
#     filter_dict={},
#     boost_dict={"content": 1.0},
#     num_results=3
# )

# # 6. Extract the filename of the first result
# if search_results:
#     print("First result filename:", search_results[0]['filename'])
# else:
#     print("No results returned.")



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