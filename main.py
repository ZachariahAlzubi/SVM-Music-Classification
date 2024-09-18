
# main.py

from data_loader import load_data
from svm_model import train_svm
from utils import start_timer, end_timer

# Define genre labels
genre_labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

def main():
    # Start the timer
    start_time = start_timer()

    # Path to the dataset (replace with your actual path)
    path = './Data'
    
    # Load the data
    X, y = load_data(path, genre_labels)
    print(f"Loaded {len(X)} samples.")
    
    # Train the SVM model and get accuracy
    accuracy = train_svm(X, y)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    # End the timer
    end_timer(start_time)

if __name__ == "__main__":
    main()
