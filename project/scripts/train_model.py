import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_sent_model():

    data = pd.read_csv(r"project\data\labeled.csv")
    comments = data['comment']
    labels = data['label']


    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(comments)
    y = labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training started \n")
    model = LogisticRegression()
    model.fit(X_train, y_train)
    print("Training completed \n")


    y_pred = model.predict(X_test)
    print(r"Model accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test,y_pred))

    models_direc = 'project/models'

    joblib.dump(model, os.path.join(models_direc, 'sentiment_model.pkl'))
    joblib.dump(vectorizer, os.path.join(models_direc, 'tfidf_vectorizer.pkl'))
    print("Model and vectorizer saved in models directory")

train_sent_model()