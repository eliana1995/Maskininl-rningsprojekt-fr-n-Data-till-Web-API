from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Ladda modell och feature-columns
model = joblib.load("writing_score_model.joblib")
feature_columns = joblib.load("feature_columns.joblib")

@app.route('/')
def home():
    return "API fungerar! Använd /predict för att göra en prediktion."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Hämta JSON-data
        data = request.get_json(force=True)

        # Skapa DataFrame
        df = pd.DataFrame([data])

        # One-hot encode kategoriska kolumner
        categorical_cols = [
            'gender', 'race_ethnicity', 
            'parental_level_of_education', 'lunch', 'test_preparation_course'
        ]
        df_encoded = pd.get_dummies(df, columns=categorical_cols)

        # Lägg till saknade kolumner som 0
        for col in feature_columns:
            if col not in df_encoded.columns:
                df_encoded[col] = 0

        # Sortera kolumner i exakt samma ordning
        df_encoded = df_encoded[feature_columns]

        # Prediktion
        prediction = model.predict(df_encoded)
        return jsonify({"predicted_writing_score": round(float(prediction[0]), 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5003)

