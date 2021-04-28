import streamlit as st
import time
import csv

hours = int(time.strftime('%H'))

# Section 1: Title
st.title('Affective Foretell')
st.subheader('What is your name?')
name = st.selectbox(
    'Select your nickname.',
    ('--', 'Alex', 'Ben', 'Chris', 'Don', 'Eddie', 'Fem', 'Greta',
     'Hans', 'Iris', 'Jon'))
if name != '--':
    st.write('Helloooo', name,'!')

# Section 2: Mood
st.subheader('How are you feeling right now?')
mood_calm = st.select_slider(' ',
    ['Very agitated', 'Agitated', 'Somewhat agitated', 'Neutral', 'Somewhat calm', 'Calm', 'Very calm'],
    value='Very agitated')

mood_awake = st.select_slider(' ',
    ['Very tired', 'Tired', 'Somewhat tired', 'Neutral', 'Somewhat awake', 'Awake', 'Very awake'],
    value='Very tired')

mood_content = st.select_slider(' ',
    ['Very discontent', 'Discontent', 'Somewhat discontent', 'Neutral', 'Somewhat content', 'Content', 'Very content'],
    value='Very discontent')

mood_energy = st.select_slider(' ',
    ['Very lack of energy', 'Lack of energy', 'Somewhat lack of energy', 'Neutral', 'Somewhat energized', 'Energized', 'Very Energized'],
    value='Very lack of energy')

mood_well = st.select_slider(' ',
    ['Very unwell', 'Unwell', 'Somewhat unwell', 'Neutral', 'Somewhat well', 'Well', 'Very well'],
    value='Very unwell')

mood_relaxed = st.select_slider(' ',
    ['Very tense', 'Tense', 'Somewhat tense', 'Neutral', 'Somewhat relaxed', 'Relaxed', 'Very relaxed'],
    value='Very tense')

moods = [mood_calm, mood_awake, mood_content, mood_energy, mood_well, mood_relaxed]
# Section 3: Activities
if hours in range(6, 12):
    st.subheader('How many hours did you sleep last night?')
    sleep_time = st.slider(
        label='',
        min_value=0.0,
        max_value=16.0,
        step=0.5,
        format='%1f'
    )
    food_options = 'food_options'
    activity_options = 'activity_options'
elif hours in range(12, 17):
    st.subheader('What was your last meal?')
    food_options = st.multiselect(
        'You can select multiple options.',
        ['🥩', '🍔', '🍕', '🌭', '🍝', '🍚', '🍞', '🥛',
         '🥔', '🧀', '🍎', '🍌', '🥗', '🥒', '🍰', '🍪' ])
    sleep_time = 'sleep_time'
    activity_options = 'activity_options'
else:
    st.subheader('What were your activities today?')
    activity_options = st.multiselect(
        'You can select multiple options.',
        ['⚽️', '🧘️', '🎹', '🚗', '📱', '🛏', '🛍', '📚', '💻',
         '🍽', '🍻'])
    sleep_time = 'sleep_time'
    food_options = 'food_options'


if st.button('Submit'):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name,moods, sleep_time, food_options, activity_options])
    st.write('Thank you for your submission!')
    st.balloons()
