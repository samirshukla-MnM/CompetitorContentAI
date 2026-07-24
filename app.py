import streamlit as st
from modules.database import init_db

st.set_page_config(page_title='Competitor Content AI',layout='wide')
init_db()

st.sidebar.title('Navigation')
page=st.sidebar.radio('Go to',['Dashboard','Upload'])

st.title('Competitor Content Intelligence')

if page=='Dashboard':
    st.success('Project initialized successfully.')
    st.info('Next part will implement crawler, snapshots and AI comparison.')
else:
    file=st.file_uploader('Upload Excel',type=['xlsx'])
    if file:
        st.success('Excel received. Parsing will be implemented in Part 2.')
