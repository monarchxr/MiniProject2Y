from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
import os
import joblib


def train_sent_model():
    data = pd.read_csv(r"project\data\unlabeled.csv")
    data['comment'] = data['comment'].fillna('')
    comments = data['comment']
    labels = data['label']
    
    
    # Vectorize the comments
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X = vectorizer.fit_transform(comments)
    y = labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training started \n")
    
    # Use class weights to handle imbalance
    model = LogisticRegression(class_weight='balanced')
    model.fit(X_train, y_train)
    print("Training completed \n")

    # Predict and evaluate the model
    y_pred = model.predict(X_test)
    print(f"Model accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))

    # Save model and vectorizer
    models_direc = 'project/models'
    joblib.dump(model, os.path.join(models_direc, 'sentiment_model.pkl'))
    joblib.dump(vectorizer, os.path.join(models_direc, 'tfidf_vectorizer.pkl'))
    print("Model and vectorizer saved in models directory")

train_sent_model()