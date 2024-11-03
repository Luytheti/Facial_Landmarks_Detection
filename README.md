# Facial Landmark Detection


## Introduction
This project implements a facial landmark detection system using the Xception model, trained on the ibug dataset. The goal is to accurately detect facial landmarks from images and provide a user-friendly web application for real-time detection. 

## Try the App
You can try out the facial landmark detection application here: [Facial Landmark Detection on Streamlit](http://digitrecognizerr.streamlit.app/).



## Table of Contents
- [Dataset](#dataset)
- [Xception Model Architecture](#xception-model-architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Data Augmentation](#data-augmentation)
- [Dataset Splitting](#dataset-splitting)
- [Training Process](#training-process)
- [Results](#results)
- [License](#license)

## Dataset
The model is trained on the [ibug dataset](https://www.kaggle.com/datasets/toxicloser/ibug-300w-large-face-landmark-dataset), which contains diverse facial images with annotated landmarks, commonly used for facial landmark detection tasks.

## Xception Model Architecture
The Xception model uses depthwise separable convolutions, making it highly effective for image classification and detection tasks. Below is a visual representation of the architecture:

![Xception Model Architecture](https://github.com/Luytheti/Facial_Landmarks_Detection/blob/main/Images/xception-architecture.jpg)

## Requirements
This project requires the following Python libraries:

- **OpenCV**
- **Torch**
- **Torchvision**
- **Streamlit**
- **Pillow**
- **Matplotlib**
- **NumPy**
- **Requests**
- **Io**
- **ElementTree**
- **TQDM**
- **Scikit-image**

## Installation
To install the required libraries, use:

```bash
pip install -r requirements.txt

```

## Data Augmentation
Data augmentation was applied to enhance the training dataset's diversity and improve the facial landmark detection model's robustness:

- **Random Jitter**: Introduces slight variations in brightness, contrast, saturation, and hue for resilience against lighting changes.
- **Random Rotation**: Randomly rotates images and adjusts landmark coordinates for various orientations.
- **Bounding Boxes**: Adjusts bounding boxes around facial features to align with image transformations.
- **Random Cropping**: Simulates different scales and perspectives while keeping key facial features visible.
- **Color Jittering**: Alters image colors to increase invariance to lighting conditions.

These techniques collectively improve the model's performance in real-world applications.

## Dataset Splitting
The dataset was split into training, validation, and testing subsets:

1. **Total Images**: 6666 images.
2. **Training Set**: 6000 images (90%).
3. **Validation Set**: 666 images (10%).
4. **Testing Set**: 1008 images, kept separate for evaluating model performance.

**DataLoader Creation**:
- **Training DataLoader**: Batch size of 32 with shuffling.
- **Validation DataLoader**: Batch size of 64.
- **Testing DataLoader**: Batch size of 64 for consistency.

## Training Process
The model was trained for **50 epochs** using 6000 images:

1. **Training Parameters**:
   - **Batch Size**: 32
   - **Learning Rate**: 0.00075

2. **Checkpointing**: Saves model and optimizer states, with the best model saved based on validation loss.

3. **Training Loop**: 
   - Processes data in batches, computes loss, and performs backpropagation.
   - Prints average training and validation loss for each epoch.

4. **Validation**: Evaluates performance on unseen data after each epoch.

## Results

![Training Loss Graph](https://github.com/Luytheti/Facial_Landmarks_Detection/blob/main/Images/loss_epochs.png) 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.










