import streamlit as st
from PIL import Image

#st.subheader("What is Generative AI")
st.text_area("What is Generative AI", height= 150, value= "Generative AI is a type of AI that can create new content and ideas, including conversations, stories, images, videos, and music. Like all AI, generative AI is powered by ML models—very large models that are pretrained on vast corpuses of data and commonly referred to as Foundation Models (FMs). Transition. Recent advancements in ML (specifically the invention of transformer-based neural network architecture) have led to the rise of  models that contain billions of parameters or variables")

st.text_area("What is a Foundation Model?", height= 175, value= "With tradition ML models, in order to achieve each specific task, customers need to gather labeled data, train a model and deploy that model. With foundation models, instead of gathering labeled data for each model and training multiple models, customers can use the same pretrained FM to adapt various tasks. FMs can also be customized to perform domain-specific functions that are differentiating to their businesses, using only a small fraction of the data and compute required to train a model from scratch.")

foundation_model = Image.open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/images/foundation_model.png')
st.image(foundation_model)

st.write("Who is building foundation Models")
model_list = Image.open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/images/model_list.png')
st.image(model_list)

st.write("What are the challenges with using Foundation Models")
fm_challenges = Image.open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/images/fm_challenges.png')
st.image(fm_challenges)