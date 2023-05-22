import streamlit as st
import boto3
import yaml
from sagemaker.jumpstart.notebook_utils import list_jumpstart_models
from sagemaker.jumpstart.model import JumpStartModel

# Set org ID and API key
with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/creds.yml', 'r') as file:
    config = yaml.safe_load(file)
    
access_key = config['aws']['access_key']
secret_key = config['aws']['secret_token']
region = config['aws']['region']

sagemaker_client = boto3.client('sagemaker',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

sagemaker_runtime_client = boto3.client('runtime.sagemaker',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

kendra_client = boto3.client('kendra',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

endpoints_json = sagemaker_client.list_endpoints(MaxResults=10)
indexes = kendra_client.list_indices()

filter_value = "task == text2text"
text_generation_models = list_jumpstart_models(filter=filter_value)

st.subheader("Available Jumpstart Models:")
modelid = st.radio("Select the Model to deploy:",
                    options = text_generation_models)

deploy_model = st.button("Deploy Model")

st.subheader("Deployed Endpoints:")
for endpoint in endpoints_json['Endpoints']:
    st.checkbox(endpoint['EndpointName'], value = True, disabled=True)
        
if deploy_model:
    model_id = modelid
    my_model = JumpStartModel(model_id=modelid)
    predictor = my_model.deploy()

#with col2:
#    st.write('Knowledge Base')
#    for index in indexes['IndexConfigurationSummaryItems']:
#        st.checkbox(index['Name'], value = True, disabled=True)