import streamlit as st

st.title('Girin\'s Deploy App')
st.write('My Second Deploy App!')

import os

key = os.environ.get('MY_SECRET', 'NOT SET YET')
st.write(f'Server Key : {key}')


