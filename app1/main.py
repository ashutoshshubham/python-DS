'''

how to run 
 - open terminal
 - cd app1 (press enter)
 - streamlit run main.py (press enter)


to stop
 - press ctrl + c

'''

import streamlit as st

st.title("this is a title")
st.header("this is Heading")
st.subheader("Subheading")
st.text("A very normal text on a  normal day")
st.write("This is the magic function to write stuff")
st.success("This is text written for success message")
st.error("This is text written for error message")
st.info("This is the information message text")
st.warning("This is a warning text")
st.markdown('''
this is markdown text, here u are free to use
<h5> HtML <h5>
<p> this is a paragraph </p>
<ul>
       <li> One two <li>
       <li> Three Four </li>
       <li> Five Six </li>
</ul>
or 
# Markdown heading
''', unsafe_allow_html=True)
st.code('Area where we can put code')