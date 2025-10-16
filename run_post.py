import requests

url = "http://127.0.0.1:5003/predict"

data = {
    "gender": "female",
    "race_ethnicity": "group B",
    "parental_level_of_education": "bachelor's degree",
    "lunch": "standard",
    "test_preparation_course": "completed",
    "math_score": 78,
    "reading_score": 85
}

response = requests.post(url, json=data)
print("Svar från API:", response.json())
