
import streamlit as st
import boto3
import json
import time
import numpy as np
import pandas as pd
from cohere_sagemaker import Client
import yaml

# Set org ID and API key
with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/creds.yml', 'r') as file:
    config = yaml.safe_load(file)
    
access_key = config['aws']['access_key']
secret_key = config['aws']['secret_token']
region = config['aws']['region']
cohere_endpoint = config['endpoints']['cohere']
flant5_endpoint = config['endpoints']['flant5']

sagemaker_runtime_client = boto3.client('runtime.sagemaker',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

sagemaker_client = boto3.client('sagemaker',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

def query_endpoint_with_json_payload(encoded_json, endpoint_name, content_type='application/json'):
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType=content_type, Body=encoded_json)
    return response

def parse_response_multiple_texts(query_response):
    model_predictions = json.loads(query_response['Body'].read())
    generated_text = model_predictions['generated_texts']
    return generated_text

def call_cohere_model(inputs, tokens, temperature):
    co = Client(endpoint_name=cohere_endpoint)
    response = co.generate(prompt=inputs, max_tokens=tokens, temperature=temperature)
    return response.generations[0].text

def call_flant5_model(inputs):
    parameters = {"max_length":250, "num_return_sequences":1, "top_k":50, "top_p":0.95, "do_sample":True}
    input_text = "Answer based on context:" + "\n\n" + inputs
    payload = {"text_inputs": input_text, **parameters}  
    query_response = query_endpoint_with_json_payload(json.dumps(payload).encode('utf-8'), endpoint_name=flant5_endpoint)
    generated_text = parse_response_multiple_texts(query_response)
    return generated_text

st.subheader('Compare models in your secure environment.')

col1, col2 = st.columns(2)
with col1:
    left_model = st.selectbox('Choose First Model:', ['cohere-gpt-medium', 'flan-t5-xxl'])
with col2:
    right_model = st.selectbox('Choose Second Model:', ['cohere-gpt-medium', 'flan-t5-xxl'])

input_value = st.text_area('Input: ', placeholder='Ask me anything ...', key='prompt', height =  250, max_chars= 5000)
submit_button = st.button("Generate")
col3, col4 = st.columns(2)

if submit_button:
    with col1:
        if left_model == 'cohere-gpt-medium':
            output = call_cohere_model(input_value, tokens=300, temperature=0.7)
            st.text_area(label='cohere-gpt-medium: ', height =  250, value = output)
            
        if left_model == 'flan-t5-xxl':
            output = call_flant5_model(inputs=input_value)
            st.text_area(label='flan-t5-xxl: ', height =  250, value = output)
            
    with col2:
        if right_model == 'cohere-gpt-medium':
            output = call_cohere_model(input_value, tokens=300, temperature=0.7)
            st.text_area(label='cohere-gpt-medium: ', height =  250, value = output)
            
        if right_model == 'flan-t5-xxl':
            output = call_flant5_model(inputs=input_value)
            st.text_area(label='flan-t5-xxl: ', height =  250, value = output)