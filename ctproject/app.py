import streamlit as st
import pandas as pd
#import plotly.figure_factory as ff
import plotly.express as px
#import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='My app')

#global variable
url = "https://www.youtube.com/watch?v=XyEOEBsa8I4"

#html variagle
html='''
<html>
    <head>
        <title>This HTML App</title>
    </head>
    <body>
        <h1>This Long Text!!!</h1>
        <br>
        <hr>
        <h3>This a small text</h3>
    </body>
</html>
'''

with open('./temp_html.html', 'r', encoding='UTF-8') as f:
    filehtml = f.read()
    f.close()

#data app
df = pd.read_csv('./data/data.csv')

st.title('This is my first webapp!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content1...'):
        st.subheader('Content1...')
        st.video(url)

    with st.expander('Content2...'):
        st.subheader('Content2...')
        st.table(df)    
        #dff=df.groupby(by='name').sum()
        #st.table(dff)
        dff=px.bar(df, x='name', y='kor', title='KoreanScores')
        st.plotly_chart(dff)
        
    with st.expander('Content3...'):
        st.subheader('Content3...')
        st.image('./images/images.jpg')
        st.write('<h1>This is new title</h1>', unsafe_allow_html=True)
        st.markdown(html, unsafe_allow_html=True)

    with st.expander('Content4...'):
        st.subheader('Content4...')
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml, height=800)

with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')