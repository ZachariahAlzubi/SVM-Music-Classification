
# data_loader.py

import os
import matplotlib.pyplot as plt

def load_data(path, genre_labels):
    """Function to load spectrogram images from the dataset."""
    X = []
    y = []
    
    # Loop through each genre folder and load the images
    for i, genre in enumerate(genre_labels):
        j = 0
        genre_path = os.path.join(path, 'images_original', genre)
        for file in os.listdir(genre_path):
            j += 1
            if j == 30:  # Limit to 30 files per genre
                break
            if file.endswith('.png'):
                img_path = os.path.join(genre_path, file)
                img = plt.imread(img_path)
                X.append(img)
                y.append(i)
    
    return X, y
