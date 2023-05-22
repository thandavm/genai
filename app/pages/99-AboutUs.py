import streamlit as st
from PIL import Image

col1, col2 = st.columns([1,2])

with col1:
    meena = Image.open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/images/meena.png')
    st.image(meena)

with col2:
    st.write("Meena Thandavarayan")
    st.write("https://phonetool.amazon.com/users/thandavm")
    st.write("https://www.linkedin.com/in/meenakshisundaramt")
    
    

meena_age = Image.open('/Users/thandavm/work/strategic_accounts/ai_summit/gen_ai_app/pages/images/meena_age.png')
st.image(meena_age)