# 🎬 IMDB Review Classifier AI

A GenAI-powered web app that analyzes and summarizes IMDB movie reviews using a Large Language Model (Mistral 7B). The model outputs structured insights including:

-  Movie Details (Name, Director, Starcast)
-  Review Summary (combined user sentiment)
-  Sentiment (Positive / Negative)

Built using:
- LangChain 
- HuggingFace Transformers 
- Streamlit 
- Pydantic for structured output

Requirements (to import)
- streamlit
- langchain
- langchain_huggingface
- langchain_community
- python-dotenv
- pydantic
- huggingface_hub

## Project Structure
IMDB_Reviewer_AI/ <br>
│<br>
├── IMDB_reviews_classifier.py # Main Streamlit app<br>
├── IMDB_Dataset.csv # Dataset with raw reviews<br>
├── .env #(optional) for API keys<br>
└── README.md #Project documentation<br>



## License
This project is non-commercial and for educational or experimental use only.

## Contributing
If you’d like to contribute or enhance functionality (e.g., add RAG, multiple input handling, or charts), feel free to fork and submit a pull request!
