import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

def predict(input_text, model_file, vectorizer_file):
    # Load the model and vectorizer
    model = joblib.load(model_file)
    vectorizer = joblib.load(vectorizer_file)

    # Transform input text into numerical features
    input_vectorized = vectorizer.transform([input_text])

    # Perform prediction on the vectorized input text
    prediction = model.predict(input_vectorized)
    return prediction

if __name__ == "__main__":
    # Your input text for prediction
    raw_data1 = 'so what exactly are the roadblocks preventing riot from having a balanced game after 13 years dont get me wrong im not an expert on the subject so my opinion probably means squat but ive been playing league for about 8 years so i at least know what some things are or were like the obvious ones are'
    raw_data2 = 'why do people in low elo play jayce im gold 1 atm and whenever i get jayce on my team it just feels like an automatic loss hes supposed to be a lane bully if youre skilled enough but every time i see it they just go even or lose lane by the time 20 minutes rolls around they basically turn into a caster minion for the rest of the game but almost worse since they almost always miss their one skill shot either that or they jump on like a melee minion and die within 2 seconds the champ has one of the worst win rates in the game right now  jayce build with highest winrate  lol runes items and skill orderhttpsugglolchampionsjaycebuildrankgold   just genuinely curious what compels people to pick him edit okay so i guess people think its more fun to cosplay huni than win the game '

    # Path to your trained model file and vectorizer file
    model_path = 'models/gradient_boosting_model.pkl'
    vectorizer_path = 'models/vectorizer.pkl'

    # Making predictions
    result1 = predict(raw_data1, model_path, vectorizer_path)
    result2 = predict(raw_data2, model_path, vectorizer_path)

    print("Predicted category 1:", result1[0])
    print("Predicted category 2:", result2[0])
