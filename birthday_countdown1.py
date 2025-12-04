
import datetime
import random

bday_messages = [
  'Hope you have a very Happy Birthday! 🎈',
  'It\'s your special day – get out there and celebrate! 🎉',
  'You were born and the world got better – everybody wins! Happy Birthday! 🥳',
  'Have lots of fun on your special day! 🎂',
  'Another year of you going around the sun! 🌞'
]

random_message = random.choice(bday_messages)

today = datetime.date.today()

# **IMPORTANT:** Set your next birthday date here (Year, Month, Day)
my_next_birthday = datetime.date(2025, 12 ,4)

days_away = my_next_birthday - today

if my_next_birthday == today:

  print(random_message)
else:
  print(f'My next birthday is {days_away.days} days away!')