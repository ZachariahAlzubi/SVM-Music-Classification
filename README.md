
# SVM Music Genre Classification

## Overview

This project performs music genre classification using Support Vector Machines (SVM) based on spectrogram images of songs from different genres. The dataset includes genres such as blues, classical, country, and more.

### Project Structure

- `main.py`: The main script that runs the data loading, model training, and evaluation.
- `data_loader.py`: Loads and preprocesses the spectrogram images from the dataset.
- `svm_model.py`: Defines the SVM classifier and trains it.
- `utils.py`: Contains utility functions for timing and performance evaluation.

### How to Use

1. Ensure the data is correctly placed in the `Data/images_original/` directory, organized by genre folders.
2. Run the `main.py` file to load the data, train the model, and evaluate its performance.
(you could also just inspect the jupyter notebook which contains fully functional usage of all of the python files involved)
### Example

```bash
python main.py
```

### Dependencies

- `scikit-learn`
- `matplotlib`
- `numpy`
