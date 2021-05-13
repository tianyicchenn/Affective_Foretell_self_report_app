import streamlit as st
import time
from oocsi import OOCSI


def main():
    hours = int(time.strftime('%H'))

    # Section 1: Title
    st.title('Affective Foreteller')
    st.subheader('What is your name?')
    nickname = st.selectbox(
        'Select your nickname.',
        ('--', 'Hans', 'Mark', 'Nora', 'Oz', 'Paul', 'Quinn', 'Roy', 'Sam'))
    if nickname != '--':
        st.write('Hello', nickname, '!')

    # Section 2: Mood
    st.subheader('How are you feeling right now?')
    mood_option = st.radio(
        'Select an option of words that best describe your mood.',
        ('Excited, elated, ebullient', 'Happy, pleased, content', 'Calm, serene, tranquil',
         'Tense, nervous, upset', 'Miserable, unhappy, discontent', 'Depressed, bored, lethargic')
    )

    # Section 3: Activities
    if hours in range(5, 11):
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
    elif hours in range(11, 17):
        st.subheader('What was your last meal?')
        food_options = st.text_input('Type or use emojis to describe what you ate.', value='', max_chars=50)
        sleep_time = 'sleep_time'
        activity_options = 'activity_options'
    else:
        st.subheader('What were your activities today?')
        activity_options = st.multiselect(
            'You can select multiple options.',
            ['⚽ sport️', '🧘️ meditation', '🎼 music', '🎨 hobbies', '🚗 commute', '📱 apps',
             '🛏 rest', '🛍 shopping', '📚 read', '💻 work', '🍽 meals', '🍻 drinks'])
        sleep_time = 'sleep_time'
        food_options = 'food_options'

    def send_data():
        oocsi.send('Affective_Foretell_Self_Report', {
            'name': nickname,
            'mood': mood_option,
            'sleep': sleep_time,
            'food': food_options,
            'activities':activity_options})

    if st.button('Submit'):
        if nickname == '--':
            st.write('Please select your nickname.')
        else:
            st.write('Thank you for your submission!')
            oocsi = OOCSI('Affective_Foretell', 'oocsi.id.tue.nl')
            oocsi.subscribe('Affective_Foretell_Self_Report', send_data())
            oocsi.stop()
            st.balloons()


if __name__ == '__main__':
    main()