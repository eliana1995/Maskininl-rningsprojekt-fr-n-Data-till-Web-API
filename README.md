# Writing Score Project
# Writing Score Prediction API

Ett maskininlärningsprojekt som förutsäger studenters skrivpoäng baserat på indata.
Byggt med Flask och Python.

2- jag har Skapat virtuell miljö:
python3 -m venv .venv
source .venv/bin/activate

3- Installera beroenden- 
pip install -r requirements.txt

4- Starta API
python app.py

5- bör se:
API fungerar! Använd /predict för att göra en prediktion.


6- Testa med Postman
Skapa en POST-request till:
http://127.0.0.1:5003/predict

JSON, och jag skriv in

{
    "gender": "female",
    "race_ethnicity": "group B",
    "parental_level_of_education": "bachelor's degree",
    "lunch": "standard",
    "test_preparation_course": "completed",
    "math_score": 78,
    "reading_score": 85
}

jag får ett svar som:
{
    "predicted_writing_score": 1221.73
}

Det betyder att modellen har gjort en prediktion och "tror" att studentens writing_score skulle vara 1221.73.



