import os

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
from sklearn.svm import SVC
from wf_ml_prediction import predict
from wf_ml_training import *
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier


def load_and_split(file_path):
    df = pd.read_csv(file_path)
    df['Text'] = df['Content'].fillna('')
    X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['Category'], test_size=0.2, random_state=42)

    train_data = pd.DataFrame({'Text': X_train, 'Category': y_train})
    test_data = pd.DataFrame({'Text': X_test, 'Category': y_test})

    train_data.to_csv('data_processed/train_data.csv', index=False)
    test_data.to_csv('data_processed/test_data.csv', index=False)
    return X_train, X_test, y_train, y_test


def vectorize_text(x_train, x_test):
    tfidf = TfidfVectorizer(max_features=1000)
    x_train_tfidf = tfidf.fit_transform(x_train)
    x_test_tfidf = tfidf.transform(x_test)

    vectorizer_file = os.path.join('models', 'vectorizer.pkl')
    joblib.dump(tfidf, vectorizer_file)

    return x_train_tfidf, x_test_tfidf


def evaluate_models(models, x_test, y_test):
    try:
        evaluation_summary = []
        for name, model in models.items():
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, zero_division=1)
            evaluation_summary.append((name, accuracy, report))

        with open('evaluation/summary.txt', 'a') as file:
            for name, accuracy, report in evaluation_summary:
                file.write(f"Model: {name}\n")
                file.write(f"Accuracy: {accuracy}\n")
                file.write(f"Classification Report:\n{report}\n\n")

        print("Evaluation summary saved successfully.")
    except FileNotFoundError:
        print("Model file not found. Please ensure the models are saved.")
    except Exception as e:
        print(f"An error occurred during evaluation: {e}")


if __name__ == '__main__':
    x_train, x_test, y_train, y_test = load_and_split('data_processed/categorized_reddit_data.csv')
    initial_model = train_model(x_train, x_test, y_train, y_test) # First model

    x_train_tfidf, x_test_tfidf = vectorize_text(x_train, x_test)

    models = {
              'Random Forest': train_random_forest(x_train_tfidf, x_test_tfidf, y_train, y_test)[0],
              'Gradient Boosting': train_gradient_boosting(x_train_tfidf, x_test_tfidf, y_train, y_test)[0],
              'SVM': train_svm(x_train_tfidf, x_test_tfidf, y_train, y_test)[0]}

    for name, model in models.items():
        joblib.dump(model, f'models/{name.lower().replace(" ", "_")}_model.pkl')
    evaluate_models(models, x_test_tfidf, y_test)


