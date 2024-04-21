from langchain.llms.bedrock import Bedrock
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import boto3
import streamlit as st

## Bedrock client
bedrock_client = boto3.client(
    service_name = 'bedrock-runtime',
    region_name = 'us-east-1',
)

model_id = 'ai21.j2-mid-v1'
# "meta.llama2-13b-chat-v1"

llm = Bedrock(
    model_id=model_id,
    client = bedrock_client,
    model_kwargs={'temperature':0}

)

def my_chatbot(language, user_text):
    prompt = PromptTemplate(
        input_variables=['language', 'user_text'],
        template = 'You are a chatbot. You are in {language}. \n\n{user_text}'
    )

    bedrock_chain = LLMChain(llm=llm, prompt=prompt)
    response = bedrock_chain({'language':language, 'user_text':user_text})

    return response

st.title('Chatbot using Amazon Bedrock - Demo')
language = st.sidebar.selectbox("Language", ['English', 'Spanish', 'Hindi', 'Telugu'])

if language:
    user_text = st.sidebar.text_area(label='What is your Question?',
                                     max_chars=100)
if user_text:
    response = my_chatbot(language, user_text)
    st.write(response['text'])
