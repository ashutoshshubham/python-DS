import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import re      
from textblob import TextBlob
import plotly.graph_objects as go

st.set_page_config(page_title  = "Valorant",layout = 'wide')
st.title("Sentiment Analysis On Video Game Tweets 🤩")

adf = pd.read_csv('Valorant.csv')

@st.cache
def load_data():
    valorantdf = pd.read_csv('Valorant.csv',parse_dates= ['Date'], dayfirst = True)
    valorantdf.sort_values(by = 'Date', inplace = True)
    valorantdf.rename(columns = {'Text':'Tweets'}, inplace = True)
    valorantdf.drop(columns = ['Id','Length','Source'], inplace = True)

    valorantdf['Tweets'] = valorantdf['Tweets'].str.lower()
    valorantdf['Tweets'] = valorantdf['Tweets'].apply(remove_hashtags)
    valorantdf['Tweets'] = valorantdf['Tweets'].apply(remove_mentions)
    valorantdf['Tweets'] = valorantdf['Tweets'].apply(remove_links)
    valorantdf['Sentiment'] = valorantdf['Tweets'].apply(get_sentiment)
    valorantdf['SentimentName'] = valorantdf["Sentiment"].apply(get_sentiment_name)

    return valorantdf

def remove_mentions(tweet):
    return re.sub('@[A-Za-z0-9_]+'," ",tweet)

def remove_hashtags(tweet): 
    return re.sub('#[A-Za-z0-9_]+'," ",tweet)

def remove_links(tweet): 
    tweet = re.sub('[()!?]'," ",tweet)           
    tweet = re.sub(r'http\S+'," ",tweet)         
    tweet = re.sub(r'www.\S+'," ",tweet)         
    tweet = re.sub(r'\[.*?\]',' ', tweet)        
    return re.sub(r'[^a-z0-9]'," ",tweet)   

def get_sentiment(tweet):
    blob = TextBlob(tweet)
    return blob.sentiment.polarity

def get_sentiment_name(sentiment):
    if sentiment == 0:
        return "Neutral 😊"
    elif sentiment > 0:
        return "Positive🥳"
    else:
        return "Negative🤬" 

st.sidebar.header("OPTIONS")
vdf = load_data()
view_data = st.sidebar.checkbox("See Raw Data")
if view_data:
    st.write(adf)






if st.sidebar.checkbox("Visualize"):
    graph_types = ['pie','bar']
    gtype = st.sidebar.radio("Select a graph type ",graph_types)
    st.header("Overall Sentiment Count")
    count = vdf.SentimentName.value_counts().reset_index()
    if gtype == graph_types[0]:
        fig = px.pie(count,'index','SentimentName',color='index',color_discrete_sequence=["yellow", "green", "red"])
    if gtype == graph_types[1]:
        fig = px.bar(count,'index','SentimentName',color='index',color_discrete_sequence=["yellow", "green", "red"]) 
    st.plotly_chart(fig,use_container_width= True)

if st.sidebar.checkbox("View By Date"):
    st.header("Sentiments on Various Dates")
    df = load_data()
    counter = df.SentimentName.reset_index()
    counter['Date'] = df['Date']
    # counter[counter['Date']<='2020-02-04']
    counter = pd.concat([counter,pd.get_dummies(counter['SentimentName'])], axis=1)
    counter['Date'] = pd.to_datetime(counter['Date'])
    counterdf = counter.set_index('Date').resample('D').sum()
    counterdf.replace(0,np.nan,inplace=True)
    counterdf.dropna(how='all',inplace=True)

    graph_types = ['bar','funnel']
    gtype = st.sidebar.radio("Select a graph type ",graph_types)
    if gtype == graph_types[0]:
        fig = px.bar(counterdf, counterdf.index, ['Negative🤬','Neutral 😊','Positive🥳'],color='variable',color_discrete_sequence=["red", "yellow", "green"])
    if gtype == graph_types[1]:
        fig = px.funnel(counterdf, counterdf.index, ['Negative🤬','Neutral 😊','Positive🥳'],color='variable',color_discrete_sequence=["red", "yellow", "green"])
    st.plotly_chart(fig,use_container_width= True)

    
    

    

