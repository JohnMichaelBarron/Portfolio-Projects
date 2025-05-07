# Bear Image Classifier

A deep learning project using FastAI to classify images of grizzly, black, and teddy bears. This script automates the workflow from data collection to model training, using image search, validation, and classification via a convolutional neural network.

## Features

- **Automated Image Search**: Uses DuckDuckGo to download images for each bear category.
- **Directory Management**: Automatically sets up directory structure for training and test data.
- **Image Verification**: Cleans corrupted or unreadable images before training.
- **Model Training**: Trains a ResNet18 CNN using FastAIs high-level API.
- **Test Image Creation**: Populates a test folder with example images for inference testing.

├── bear_classifier.pkl # Trained model (exported after training)
├── test_images/ # Folder containing test images
├── data/ # Training images organized by class
│ ├── grizzly/
│ ├── black/
│ └── teddy/
└── bear_classifier.py # Main script (this file)
***

## Requirements

- Python 3.7+
- Internet connection (for image search and downloading)

### Python Packages

Install dependencies with:

*bash*
pip install fastai fastdownload duckduckgo_search

Run the script:

python bear_classifier.py

The script will:

Set up folders

Download images via DuckDuckGo

Verify and clean the dataset

Copy test images to a separate folder

Train a model using a ResNet18 architecture

Save the trained model as bear_classifier.pkl



The script limits downloads to 10 images per category for speed. You can increase max_images in search_and_download_images() for better performance.

num_workers=0 is used in the dataloader to avoid multiprocessing issues, especially on Windows.

All training images must be valid .jpg files.