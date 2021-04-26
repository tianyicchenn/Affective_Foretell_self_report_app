import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Affective Foretell')
st.write("What's your name?")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
checker = st.checkbox('I am a robot.')
if st.button('Say hello'):
    st.write('Why hello there')
    print(checker)
else:
    st.write('Goodbye')




option = st.sidebar.selectbox(
    'Which number do you like best?', df['first column'])

st.write('You selected: ', option)

progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')