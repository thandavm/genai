import boto3
import yaml

def get_aws_creds():
    with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/secrets/creds.yml', 'r') as file:
        config = yaml.safe_load(file)
        
    access_key = config['aws']['access_key']
    secret_key = config['aws']['secret_token']
    region = config['aws']['region']
    
    return access_key, secret_key, region
    
def get_endpoint(endpoint_name):    
    with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/secrets/creds.yml', 'r') as file:
        config = yaml.safe_load(file)
    
    endpoint = config['endpoints'][endpoint_name]
    return endpoint

def get_sagemaker_runtime_client():
    access_key, secret_key, region = get_aws_creds()
    sagemaker_runtime_client = boto3.client('runtime.sagemaker',
                                aws_access_key_id= access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

    return sagemaker_runtime_client

def get_kendra_client():
    access_key, secret_key, region = get_aws_creds()
    kendra_client = boto3.client('kendra',
                                aws_access_key_id= access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

    return kendra_client

def get_sagemaker_client():
    access_key, secret_key, region = get_aws_creds()
    sagemaker_client = boto3.client('sagemaker',
                                aws_access_key_id= access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

    return sagemaker_client

def get_transcribe_client():
    access_key, secret_key, region = get_aws_creds()
    transcribe_client = boto3.client('transcribe',
                                aws_access_key_id= access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)

    return transcribe_client

def get_knowledge_index(indexname):
    with open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/secrets/creds.yml', 'r') as file:
        config = yaml.safe_load(file)
    
    endpoint = config['knowledge_index'][indexname]
    return endpoint