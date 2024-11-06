import os
import gdown

# Define the path and Google Drive file ID
FILE_PATH = "Dataset"  # Local path where you want to save the file
FILE_ID = "1YWzNC3rzv2WVSiNUDE57GA4vHpNKhR4P"  # File ID from the shared link
FILE_URL = f"https://drive.google.com/uc?id={FILE_ID}"

def load_model():
    if not os.path.exists(FILE_PATH):
        print("Downloading YOLO model from Google Drive...")
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        try:
            # Download the file using gdown
            gdown.download(FILE_URL, FILE_PATH, quiet=False)
            print(f"Model downloaded successfully at: {FILE_PATH}")
        except Exception as e:
            print(f"Error downloading the model: {e}")
            return None
    else:
        print(f"Model already exists at: {FILE_PATH}")
    
    return FILE_PATH

# Call the function to download and use the model
model_path = load_model()

if model_path:
    print(f"Model is ready at: {model_path}")
else:
    print("Model download failed.")