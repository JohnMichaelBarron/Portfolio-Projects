import os
from pathlib import Path
from fastai.vision.all import *
from fastdownload import download_url
from duckduckgo_search import DDGS
import shutil

# Define paths
base_path = Path(r"Z:\Deep Learner\New_DL\lesson2")
data_path = base_path / "data"  # Store training data in a separate folder
test_images_folder = base_path / "test_images"
model_path = base_path / "bear_classifier.pkl"
image_categories = ["grizzly", "black", "teddy"]

# Ensure directories exist
def setup_directories():
    print("Setting up directories...")
    data_path.mkdir(parents=True, exist_ok=True)
    for category in image_categories:
        (data_path / category).mkdir(parents=True, exist_ok=True)
    test_images_folder.mkdir(parents=True, exist_ok=True)

# Function to search and download images
def search_and_download_images(category, max_images=10):
    print(f"Downloading images for: {category}")
    ddgs = DDGS()
    results = ddgs.images(f"{category} bear photos", max_results=max_images)
    urls = [result["image"] for result in results]
    print(f"Found URLs for {category}: {urls}")
    
    dest_folder = data_path / category
    for i, url in enumerate(urls):
        try:
            dest = dest_folder / f"{category}_{i}.jpg"
            download_url(url, dest, show_progress=False)
        except Exception as e:
            print(f"Error downloading {url}: {e}")

# Verify and clean downloaded images
def verify_images_in_path():
    print("Verifying images...")
    failed = verify_images(get_image_files(data_path))
    failed.map(Path.unlink)  # Remove invalid images
    print(f"Number of failed images removed: {len(failed)}")

# Create test images
def create_test_images():
    print("Populating test images...")
    for category in image_categories:
        source_folder = data_path / category
        dest_image_path = test_images_folder / f"test_{category}.jpg"
        # Copy the first image from each category as a test image
        example_image = next(source_folder.glob("*.jpg"), None)
        if example_image:
            shutil.copy(example_image, dest_image_path)
            print(f"Copied {example_image} to {dest_image_path}")
        else:
            print(f"No images found in {source_folder} to copy.")

# Create and train model
def train_model():
    print("Creating DataBlock...")

    # Filter to exclude `test_images`
    def filter_test_images(path):
        return path.parent.name != test_images_folder.name

    bears = DataBlock(
        blocks=(ImageBlock, CategoryBlock),
        get_items=lambda p: list(filter(filter_test_images, get_image_files(p))),
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=Resize(128)
    )

    dls = bears.dataloaders(data_path, bs=4, num_workers=0)  # Set num_workers=0 to avoid multiprocessing errors
    print(f"Classes: {dls.vocab}")  # Ensure classes are correct
    print(f"Number of training items: {len(dls.train_ds)}")
    print(f"Number of validation items: {len(dls.valid_ds)}")

    if len(dls.train_ds) == 0 or len(dls.valid_ds) == 0:
        print("Training or validation dataset is empty. Exiting.")
        return None

    print("Training model...")
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(4, base_lr=1e-3)

    print("Model training complete. Saving model...")
    learn.export(model_path)
    print(f"Model saved to {model_path}")
    return learn

# Main script
if __name__ == "__main__":
    print("Starting bear classifier script...")
    setup_directories()
    print("Starting image download...")
    for category in image_categories:
        search_and_download_images(category)
    verify_images_in_path()
    create_test_images()  # Populate test_images
    trained_model = train_model()
    if trained_model:
        print("Bear classifier script completed successfully.")
    else:
        print("Bear classifier script failed.")
