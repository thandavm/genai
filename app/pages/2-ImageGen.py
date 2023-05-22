import streamlit as st
import json
import boto3
import yaml
import numpy as np
from matplotlib import pyplot as plt

with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/creds.yml', 'r') as file:
    config = yaml.safe_load(file)
    
access_key = config['aws']['access_key']
secret_key = config['aws']['secret_token']
region = config['aws']['region']

sd_endpoint = config['endpoints']['stable_diffuse_fintune'] 
#sd_endpoint = 'jumpstart-ftc-stable-diffuse-verc'

sagemaker_runtime_client = boto3.client('runtime.sagemaker',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

sagemaker_client = boto3.client('sagemaker',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

st.subheader('Test your fine tuned LLM - Text to Image')

input_value = st.text_area('Input for Stable Diffusion: ', placeholder='Ask me anything ...', key='prompt', height =  250, max_chars= 5000)
submit_button = st.button("Generate")

if submit_button:
    response = sagemaker_runtime_client.invoke_endpoint(EndpointName=sd_endpoint, 
                        Body=input_value, 
                        ContentType='application/x-text')
    
    response_body = json.loads(response['Body'].read().decode())
    generated_image = response_body['generated_image']
    plt.figure(figsize=(12, 12))
    st.image(np.array(generated_image))