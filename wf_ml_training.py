from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from sklearn.svm import SVC


def train_model(x_train, x_test, y_train, y_test):
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    joblib.dump(model, 'models/text_category_model.pkl')

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, zero_division=1)
    # By starting the summary file here, I can append the rest and use the first model as the creator of the file since
    # the other models use the vectorized data instead.
    with open('evaluation/summary.txt', 'w') as file:
        file.write(f"Accuracy: {accuracy}\n\nClassification Report:\n{report}")
        file.write('\n')
    return model, accuracy


def train_random_forest(x_train, x_test, y_train, y_test):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    return model, accuracy


def train_gradient_boosting(x_train, x_test, y_train, y_test):
    model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    return model, accuracy


def train_svm(x_train, x_test, y_train, y_test):
    model = SVC(kernel='linear', random_state=42)
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    return model, accuracy


