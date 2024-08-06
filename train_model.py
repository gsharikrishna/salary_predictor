import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load and preprocess data
data = pd.read_csv('salary_data.csv')

# Define all possible categories for each feature
all_categories = {
    'education_level': ['bachelor\'s', 'master\'s', 'phd'],
    'job_title': ['java developer', 'backend developer', 'web developer'],
    'geographic_location': ['mumbai', 'delhi', 'bangalore'],
    'company_size': ['small', 'medium', 'large'],
    'skills_and_abilities': ['java', 'python', 'javascript']
}

# Fit label encoders with all possible categories
label_encoders = {}
for column, categories in all_categories.items():
    le = LabelEncoder()
    le.fit(categories)
    label_encoders[column] = le

# Encode the data
for column, le in label_encoders.items():
    data[column] = data[column].map(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

# Check the data before filtering
print(f"Data before filtering: {data.shape}")

# Define features and target
X = data.drop('salary', axis=1)
y = data['salary']

# Filter out rows with unseen labels
X = X[X.apply(lambda row: all(val != -1 for val in row), axis=1)]
y = y[X.index]

# Check the data after filtering
print(f"Data after filtering: {X.shape}")

# Check for empty DataFrames
if X.empty:
    raise ValueError("After filtering, the dataset is empty. Check for issues in preprocessing.")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Save the model and label encoders
joblib.dump(model, 'salary_model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print("Model and label encoders have been saved successfully.")
