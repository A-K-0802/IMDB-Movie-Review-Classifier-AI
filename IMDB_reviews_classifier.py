from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain.output_parsers import PydanticOutputParser
from pydantic import Field,BaseModel
from typing import Literal,Optional
import os
from langchain_community.document_loaders import CSVLoader
import streamlit as st

os.environ['HUGGINGFACEHUB_API_TOKEN']="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"

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation',
    temperature=0
)

model=ChatHuggingFace(llm=llm)

loader=CSVLoader(file_path='IMDB_Reviewer_AI/IMDB_Dataset.csv')

data= loader.lazy_load()

class Review(BaseModel):
    Movie_details:str=Field(description='Name of movie along with Director and Starcast of the movie')
    Review_Summary:str=Field(description='Summary of the review')
    Sentiment:Literal['Positive','Negative'] = Field(description="Describe the sentiment of the review")

parser=PydanticOutputParser(pydantic_object=Review)

prompt=PromptTemplate(
    template = """
    You are a movie review summarizer. Given the following reviews about the movie {movie}:\n\n{data}

    Generate a JSON summary with:
    - Movie_details: A string with movie name, director, and cast.
    - Review_Summary: A string summarizing the opinions.
    - Sentiment: One overall sentiment: "Positive" or "Negative".

    {format_instructions}
    """,
    input_variables=['data','movie'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = prompt | model | parser

st.header("IMDB Reviews Classifier AI")
user_input=st.text_input("Enter movie name you want reviews for")
if st.button("Get Reviews"):
    result=chain.invoke({'data':data,'movie':user_input})
    st.subheader("Movie Details")
    st.code(result.Movie_details)

    st.subheader("Review Summary")
    st.markdown(result.Review_Summary)

    st.subheader("Sentiment")
    st.success(result.Sentiment)



