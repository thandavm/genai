import json
import boto3
import streamlit as st
import yaml

from langchain import llms
from langchain import LLMChain
from langchain import PromptTemplate

from langchain.chains import SequentialChain
from langchain.agents import load_tools
from langchain.text_splitter import CharacterTextSplitter

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.embeddings.sagemaker_endpoint import SagemakerEndpointEmbeddings

from langchain.vectorstores import Chroma
from langchain.vectorstores import FAISS

with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/creds.yml', 'r') as file:
    creds = yaml.safe_load(file)
    
access_key = creds['aws']['access_key']
secret_key = creds['aws']['secret_token']
region = creds['aws']['region']

st.subheader('Doc Analyzer - powered by RAG')

st.file_uploader(label= 'Upload Document', accept_multiple_files= False, key= 'doccer')

col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    embeddings_model = st.radio(label="Embedding Model", options= ['SageMaker GPT-J', 'Cohere', 'OpenAI'])
with col2:
    vector_db = st.radio(label="Vector Databse", options= ['FAISS', 'Chroma'])
with col3:
    process_button = st.button(label= "Process")

if process_button:    
    ## split the text file
    with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/data/rawText.txt') as f:
        aws_services = f.read()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(aws_services)

    #get the embeddeings model
    if embeddings_model == 'SageMaker GPT-J':
        embeddings = SagemakerEndpointEmbeddings()
    elif embeddings_model == 'Cohere':
        embeddings = CohereEmbeddings()
    elif embeddings_model == 'OpenAI':
        embeddings = OpenAIEmbeddings()

    ## Get the embeddings and store it in a vector db - FAISS database
    if vector_db == 'FAISS':
        db = FAISS.from_documents(texts, embeddings)
    elif vector_db == 'Chroma'
        db  = Chroma.from_documents(texts, embeddings)

    #db.save_local(FAISS_INDEX_PATH)

st.text_area(label= "Question", key = 'query', )
query_button = st.button(label = "Query")
if query_button:
    
    #search the doc

    ## prompt template
    #query_prompt = PromptTemplate(
    #    input_variables=['context', 'query'],
    #    template= "Context:" + context + "`\n Question:" + query + "\nAnswer:"
    #)

    #prompt the llm
    llm_model = ''
    compose_chain = LLMChain(verbose=True, llm= llm_model, output_key='answer')





