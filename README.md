# 🎂 Personalized Birthday Countdown Flask App
In case you forget your loved one's birthday


A simple Python web application built with Flask to display a personalized countdown to a specified person's next birthday.

While Learning Python, I thought of using the random number generating feature to implement a Birthday Countdown.
First, I created a simple single-file program that checks the current date and prints the corresponding message from the array of messages, if it's your birthday, or else displays the number of days left.
And then I extended that to two separate files, one containing the logic and the other containing the birthday messages.


## ✨ Features

* **Personalized Countdown:** Displays the exact number of days remaining until the next birthday.
* **Custom Birthday Messages:** Displays a random, celebratory message on the actual birthday.
* **Easy Customization:** Easily set the name, month, and day of the birthday directly in the Python file.
* **Simple Setup:** Uses a lightweight Flask structure for quick deployment.

## 🚀 Installation & Setup

### Prerequisites

You need Python (3.6+) installed on your system.

1.  **Install Flask:**
    Open your terminal or command prompt and run:
    ```bash
    pip install Flask
    ```
 2. **Customize `app.py`**

Open the `app.py` file and update the variables at the top with the person's information:

```python
PERSON_NAME = "Saloni"  # <-- CUSTOMIZE: Enter the person's name
BIRTH_MONTH = 10        # <-- CUSTOMIZE: Month of birthday (e.g., July is 7)
BIRTH_DAY = 5           # <-- CUSTOMIZE: Day of birthday (e.g., 29)
```

3. **Run app.py **
