import streamlit as st
from streamlit_chat import message
from cohere_sagemaker import Client
import yaml
import boto3
import json

from audio_recorder_streamlit import audio_recorder

# Set org ID and API key
with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/creds.yml', 'r') as file:
    config = yaml.safe_load(file)
    
access_key = config['aws']['access_key']
secret_key = config['aws']['secret_token']
region = config['aws']['region']
aws_waf_index = config['aws_keys']['aws_waf']
legal_index = config['aws_keys']['legal']

cohere_endpoint = config['endpoints']['cohere']
flant5_endpoint = config['endpoints']['flant5']

sagemaker_runtime_client = boto3.client('runtime.sagemaker',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

kendra_client = boto3.client('kendra',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

transcribe_client = boto3.client('transcribe',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)


audio_bytes = audio_recorder()
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    
job_args = {
    'TranscriptionJobName': job_name,
    'Media': {'MediaFileUri': media_uri},
    'MediaFormat': media_format,
    'LanguageCode': 'en'}

if vocabulary_name is not None:
    job_args['Settings'] = {'VocabularyName': vocabulary_name}
response = transcribe_client.start_transcription_job(**job_args)