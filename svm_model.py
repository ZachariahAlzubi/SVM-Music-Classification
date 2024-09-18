
# svm_model.py

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_svm(X, y):
    """Train the SVM model using the provided data."""
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Initialize and train the SVM
    clf = SVC(kernel='linear', random_state=42)
    clf.fit(X_train, y_train)
    
    # Make predictions and evaluate
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy
