# app.py

from flask import Flask, render_template
import datetime
import random

app = Flask(__name__)

# --- CONFIGURATION ---
PERSON_NAME = "name"  # <-- CUSTOMIZE: Enter the person's name
BIRTH_MONTH = 1      # <-- CUSTOMIZE: Month of birthday (e.g., July is 7)
BIRTH_DAY = 1      # <-- CUSTOMIZE: Day of birthday (e.g., 29)
# ---------------------

@app.route('/')
def countdown():
    # 1. Birthday Messages
    bday_messages = [
      f'Happy Birthday, {PERSON_NAME}! Hope you have a magical day! 🎂✨',
      f'It\'s your special day, {PERSON_NAME}! Get out there and celebrate! 🎉🥳',
      f'{PERSON_NAME}, you were born and the world got better – everybody wins! Happy Birthday! 🌟'
    ]
    random_message = random.choice(bday_messages)

    today = datetime.date.today()
    
    current_year_bday = datetime.date(today.year, BIRTH_MONTH, BIRTH_DAY)
    

    if today > current_year_bday:
        my_next_birthday = datetime.date(today.year + 1, BIRTH_MONTH, BIRTH_DAY)
    else:
        my_next_birthday = current_year_bday

    days_away = my_next_birthday - today
    
    
    is_birthday = (my_next_birthday == today)
    
    if is_birthday:
        countdown_data = {
            'title': f'It\'s {PERSON_NAME}\'s Birthday!',
            'message': random_message,
            'days_left': '0',
            'is_birthday': True
        }
    else:
        countdown_data = {
            'title': f'{PERSON_NAME}\'s Birthday Countdown',
            'message': f'Mark your calendar for {my_next_birthday.strftime("%B %d, %Y")}.',
            'days_left': days_away.days,
            'is_birthday': False
        }
        

    return render_template(
        'index.html', 
        data=countdown_data, 
        person_name=PERSON_NAME,
        
        BIRTH_MONTH=BIRTH_MONTH,
        BIRTH_DAY=BIRTH_DAY
    )

if __name__ == '__main__':
    
    app.run(debug=True)