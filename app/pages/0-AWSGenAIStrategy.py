import streamlit as st
from PIL import Image

st.write("AWS Gen AI Motivation")
model_list = Image.open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/images/genai_motivation.png')
st.image(model_list)


st.write("AWS Gen AI Differentiators")
model_list = Image.open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/images/genai_differentiators.png')
st.image(model_list)

st.write("AWS Gen AI Offerings")
model_list = Image.open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/images/genai_offerings.png')
st.image(model_list)