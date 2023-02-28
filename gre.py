# import required module
import random
import streamlit as st

if st.button('Tap for new word'):
    # st.write('Why hello there')
    st.write(random.choice(open("wordList.txt","r").readline().split()))
else:
    st.write('Press')

  
# print random word
