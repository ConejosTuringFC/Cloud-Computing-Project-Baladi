# Cloud-Computing-Project-Baladi
Our cloud computing project at National Autonomous University of México. 
Baladi is an online game in which the player has to guess the name of the astronomical object shown on the NASA's Astronomy Picture Of the Day.
In order to guess the answer, the player has access to the picture and the description of the astronomical object they're looking at. The picture and description change daily, so there's a new game each day. 


This project seeks to implement the NASA's API called APOD and deploy it in a funny way using Django as the backend framework. Here are the general steps:

- NASA's APOD API provides a daily astronomical image along with its title and description.
- We process the data using Python to extract the "target word" from the image title, prioritizing known astronomical objects such as galaxy, nebula, aurora, and others.
- The description is presented to the player with the target word hidden, serving as the main clue to solve the puzzle.

## Members
- Bialy Calderon - bialycalderonm@gmail.com
- Christian Morales - chrisimg06@gmail.com
- Jesus Almaguer - correodefinitivo97@gmail.com

## Affiliation
 
National Autonomous University of México (UNAM)

ENES-UNAM
 
## License
 
This project is licensed under the **GNU General Public License v3.0**.
See the [LICENSE](LICENSE) file for details.
 
---
 
## Installation & Setup
 
**Requirements**
- Python 3.10+
- pip

**Steps**
 
```bash
# 1. Clone the repository
git clone https://github.com/ConejosTuringFC/Cloud-Computing-Project-Baladi.git
cd Cloud-Computing-Project-Baladi/baladi
 
# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate
 
# 3. Install dependencies
pip install -r requirements.txt
 
# 4. Apply migrations
python manage.py migrate
 
# 5. Run the development server
python manage.py runserver
```

## Implementation
 
The application is built on top of Django's framework and structured as two apps: `core` (home page) and `game` (main game logic).
 
**Backend — `views.py`**

The processed data is passed to the template via Django's context dictionary.
 
**Frontend — `main.js`**
 
The JavaScript reads the target word and its length from a hidden HTML element injected by Django. It then dynamically builds a Wordle-style grid (6 rows × N columns, where N is the word length) and handles all game interactions client-side: input validation, color-coding of letters, win/loss detection, and game state management.

## Methodology
 
The development followed a local-first approach: all features were built and validated in a local environment before being deployed to a cloud instance. The project was divided into three main layers:
 
1. **Data layer** — consumption of NASA's APOD API and extraction of the target word from the image title using Python.
2. **Application layer** — Django backend handling routing, template rendering, and game logic.
3. **Presentation layer** — HTML, CSS, and JavaScript delivering the Wordle-style interface to the player.

## Results
 
The application successfully fetches a new astronomical image and description from NASA's APOD API every day and presents it as a playable word-guessing game. The target word extraction, clue generation, and Wordle-style feedback system all work correctly across tested cases.

## Conclusions
 
This project demonstrated that publicly available scientific resources, such as NASA's APOD API, can be leveraged not only for educational purposes but also as the foundation for engaging and interactive applications. By combining cloud infrastructure, a lightweight web framework, and a simple game mechanic, we were able to build a tool that invites players to learn something new about our place in the universe every single day.
 
From a technical standpoint, the project reinforced the importance of separating development and production configurations, managing static files correctly in a cloud environment, and structuring a Django project in a maintainable way.

# Bibliography
 
- NASA APOD API Documentation — https://api.nasa.gov/
- Django Documentation — https://docs.djangoproject.com/

