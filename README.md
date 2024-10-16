# civiliser
A framework that uses LLM and Langchain to analyze and sort resumes with uploaded job description

### To-Dos:
1. Chunk Resumes -> Done
2. Embed Resumes -> 
3. Implement a vector database
4. Store embeddings in the vector database
5. (Agent) Get relevant skills from Job Description
6. (Agent Tool) Take that answer and produce query embeddings and retreive chunks from vector db
7. (Agent) Output relevant resumes with summaries 

### Revised To-Dos:
1. Chunk resumes
2. Chunk JDs
3. Embed resumes
4. Embed JDs
5. Similarity between Embed JD and Embed Resumes
6. Top 2 selected resumes
7. Resumes summarized and skills extracted with LLMs
8. Does it match JD?
9. Strengths and Weaknesses (?)
10. Compare different embedding models, LLM models, other hyperparameters

### Interview To-Dos:
- [ ]Go through the Github Q&A for question answering
- [ ]Go through the Resume and ask cross questions
- [ ]Clean up the project. While cleaning up, ask yourselves all types of cross-questions
- [ ]How to use RAGs with time-series data

### Open-questions
- [ ] What is the context window of my embedding model / LLM?
