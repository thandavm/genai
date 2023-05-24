import streamlit as st
from streamlit_chat import message
from cohere_sagemaker import Client
import yaml
import boto3
import json
from utils import helper

# Setting page title and header
st.set_page_config(page_title="Search Engine", page_icon=":robot_face:")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
    
aws_waf_index = helper.get_knowledge_index('aws_waf')
aws_waf_index = helper.get_knowledge_index('legal')

cohere_endpoint = helper.get_endpoint('cohere')
flant5_endpoint = helper.get_endpoint('flant5')

sagemaker_runtime_client = helper.get_sagemaker_runtime_client()
kendra_client = helper.get_kendra_client()


# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'knowledge_base' not in st.session_state:
    st.session_state['knowledge_base'] = []
if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []


def query_endpoint_with_json_payload(encoded_json, endpoint_name, content_type='application/json'):
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType=content_type, Body=encoded_json)
    return response

def parse_response_multiple_texts(query_response):
    model_predictions = json.loads(query_response['Body'].read())
    generated_text = model_predictions['generated_texts']
    return generated_text

def get_kendra_results(query, index_id):
    result = ''
    context = []

    response = kendra_client.query(QueryText= query,
                                IndexId=index_id,)

    first_result_type = ''
    if response['TotalNumberOfResults']!=0:
        first_result_type = response['ResultItems'][0]['Type']
        
    if first_result_type == 'QUESTION_ANSWER' or first_result_type == 'ANSWER':
        result = response['ResultItems'][0]['DocumentExcerpt']['Text']
    
    elif first_result_type == 'DOCUMENT':
        for query_result in response["ResultItems"]:
            if query_result["Type"]=="DOCUMENT":
                answer_text = query_result["DocumentExcerpt"]["Text"]
                context.append(answer_text)
            
            for text in context:
                result += text
    
    return result

st.subheader('Enterprise Search - powered by RAG')

# container for chat summary
selection_container = st.container()
col1, col2 = st.columns((2, 1))

with selection_container:
    with col2:
        model_name = st.selectbox("Choose a Model:", ("cohere-medium", 
                                                      "flant5",))
    
        knowledge_base = st.selectbox("Choose a Knowledge Base:", ("AWS WAF", 
                                                                   "Legal",))
    
        temperature = st.slider('Temperature', 0.0, 2.0, 0.4, 0.1 )
        tokens = st.slider('Tokens', 50, 400, 300, 10)
    
        clear_button = st.button("Clear Conversation", key="clear")
    
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['model_name'] = []
    st.session_state['knowledge_base'] = []

# container for chat summary
response_container = st.container()

# container for text box
container = st.container()

context = ''

with container:
    with col1:
        with st.form(key='my_form', clear_on_submit=True):
            query = st.text_area("Query:", key='input', height=100)
            submit_button = st.form_submit_button(label='Search')

        if submit_button and query:
            if knowledge_base == 'AWS WAF':
                context = get_kendra_results(query, aws_waf_index)
            elif knowledge_base == 'Legal':
                context = get_kendra_results(query, legal_index)
            
            if model_name == 'cohere-medium':
                qa_prompt = f'prompt: {context}\nQuestion: {query}\nAnswer:'
                co = Client(endpoint_name='cohere-medium')
                response = co.generate(prompt=qa_prompt, max_tokens=tokens, temperature=temperature)
                output = response.generations[0].text
            
            elif model_name == 'flant5':
                qa_prompt = "Summarize the Context:" + context
                parameters = {"max_length":tokens, "num_return_sequences":1, "top_k":50, "top_p":0.95, "do_sample":True}
                payload = {"text_inputs": qa_prompt, **parameters}    
                query_response = query_endpoint_with_json_payload(json.dumps(payload).encode('utf-8'), endpoint_name=flant5_endpoint)
                output = parse_response_multiple_texts(query_response)
                
            st.session_state['past'].append(query)
            st.session_state['generated'].append(output)
            st.session_state['model_name'].append(model_name)
            
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))
            st.write(f"Model used: {st.session_state['model_name'][i]}")


#sample questions

#what are the 5 pillars of well architected framework
#Design principles of Security Pillar
