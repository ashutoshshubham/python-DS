import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import re      
from textblob import TextBlob

st.set_page_config(layout = 'wide')
st.title("Sentiment Analysis On Video Game Tweets 🤩")


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

@st.cache
def load_data():
    df = pd.read_csv('Valorant.csv')
    df.rename(columns={'Text':'Tweets'}, inplace = True)
    df['Tweets'] = df['Tweets'].str.lower()
    df['Tweets'] = df['Tweets'].apply(remove_hashtags)
    df['Tweets'] = df['Tweets'].apply(remove_mentions)
    df['Tweets'] = df['Tweets'].apply(remove_links)
    df['Sentiment'] = df['Tweets'].apply(get_sentiment)
    df['SentimentName'] = df["Sentiment"].apply(get_sentiment_name)
    return df

df = load_data()
if st.checkbox("Show raw data"):
    st.write(df)

if st.checkbox("Visualize"):
    st.header("Sentiment Count")
    counter = df.SentimentName.value_counts().reset_index()
    c1,c2 = st.columns([1,3])
    c1.write(counter)
    # fig = px.line_geo(counter,'index','SentimentName')
    fig = px.bar(counter,'index','SentimentName')
    c2.plotly_chart(fig,use_container_width= True)
