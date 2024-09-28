import sqlite3
import pandas as pd
from sqlalchemy import create_engine 
from sklearn.ensemble import RandomForestClassifier
import pickle

# Connect to the SQLite database (ensure the path is correct)
conn = sqlite3.connect('D:/OneDrive/Desktop/BovineGuard/Bovine/cattle_disease.db')

# Load the data from the SQLite database into a pandas DataFrame
query = "SELECT * FROM disease_data"
data = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Assuming your dataset has a 'label' column for the target and the rest are features
X = data.drop('label', axis=1) 
y = data['label']  

# Split data into training and testing sets (optional, you can use the entire dataset for training if needed)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)


model.fit(X_train, y_train)

# Save the trained model to a .pkl file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model training complete and saved to model.pkl.")
