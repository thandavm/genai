# Building your differentiated application on AWS in < 4 hours

When building your differentiated application on Gen AI, you are often faced with challenges from 

- identifying the right foundation model that best fits your use case
- Ability to fine tune / deploy the model in a secure environment
- understanding of the frameworks, optimization techniques for fine tuning and deployment
- ability to orchestrate, dynamically keep with the changes in data, models etc
- keeping you data and IP protected
- ensuring low cost of operations

Using AWS, you can address the above challenges and build you Gen AI application in less than 4 hrs.  

## Pre-requisites

We will need a bunch of pre-requisties / frameworks to be installed on your laptop.  

### Environment:  AWS

1. AWS Account.  Get the secret key and access key 
2. Install awscli
`pip install awscli`
3. Install IDE - VS Code

### User Experience:Streamlit

Install the Streamlit essentialls
`pip install streamlit`
`pip install streamlit_chat`

### Orchestration:Langchain

Install the orchestration framework
`pip install langchain`

### Models

install the model providers
`pip install sagemaker`
`pip install cohere`
`pip install openai`

### Vector Databases

Install the vector db's
`pip install chroma`
`pip install pinecone`
`pip install FAISS`

### Git Repo

`git clone https://github.com/thandavm/genai.git`

## Understanding the Code Repo

1. app folder - has the streamlit application providing you the user experience.  
2. data - data required for the knowledge base is stored here
3. models - notebooks to create sagemaker endpoint are avalable here
4. utils - utility funtions are here
5. secrets - yaml file with all the creds is available here


## Set up

In your AWS account, we will create the knowledge repos, deploy LLM as Amazon SageMaker end points. Thus keeping in secure in your environment.  The data, model and IP does not leave your environment and protected at all costs 

### Build the Knowledge Repositories

We will be using the following Knowledge Repos

1. Amazon Kendra

- Log in to the AWS Console
- Go to Amazon Kendra Service
- Create an Index in Amazon Kendra

2. Amazon OpenSearch Service


### Create Endpoints for LLMs

Amazon SageMaker offers jumpstart

### Create a creds.yml