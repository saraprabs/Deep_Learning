# 🐾PetImages: Deep Learning Image Classifier
This repository contains an end-to-end computer vision pipeline using TensorFlow and Keras to classify images of cats and dogs. The project emphasizes data integrity, automated cleaning, and a custom CNN architecture optimized for high-throughput environments.

## 📖 Overview

This project demonstrates a robust pipeline for classifying images of cats and dogs using a deep Convolutional Neural Network (CNN). Beyond simple modeling, this project focuses on data integrity and production-readiness, implementing custom data cleaning and automated learning rate adjustments to achieve high accuracy on real-world, "noisy" data.

## 🏗️ Model Architecture

The model is a sequential Convolutional Neural Network (CNN) designed to extract hierarchical features from images resized to 150x150x3.

- Convolutional Layers: Four stages of Conv2D (32, 64, 128, and 128 filters) using 3x3 kernels and ReLU activation.

- Downsampling: MaxPooling2D (2x2) follows each convolution to reduce spatial dimensions and computational load.

- Regularization: * Batch Normalization: Applied after dense layers to stabilize learning and accelerate convergence.

- Dropout: Strategic dropout (0.5 and 0.3) to prevent overfitting by randomly deactivating neurons during training.

- Output Layer: A single neuron with a Sigmoid activation function for binary classification (0: Cat, 1: Dog).

## 🛠️ Implementation Details
1. Automated Data Integrity (Cleanup)
Raw image datasets often contain hidden junk files or corrupted headers. My implementation includes a pre-training script that:

- Filters out non-image files (e.g., Thumbs.db).

- Deletes zero-byte files.

- Uses Pillow (PIL) to verify() image headers, ensuring no truncated JPEGs crash the training process.

2. Data Augmentation
To improve generalization, the ImageDataGenerator was configured with:

- Random rotations (40°)

- Width/Height shifts (20%)

- Shear and Zoom transformations

- Horizontal flips

3. Model Tuning & Optimization
- Optimizer: Adam (Adaptive Moment Estimation) for efficient gradient descent.

- Loss Function: binary_crossentropy, the standard for two-class classification.

- Learning Rate Scheduler: Implemented ReduceLROnPlateau which monitors val_loss and reduces the learning rate by a factor of 0.2 if improvement stalls for 3 epochs.

## 📦 Packages Used
- TensorFlow / Keras: For building the deep learning layers and managing the training loops.

- Pandas: To handle and visualize the training history logs.

- Matplotlib: For plotting accuracy and loss curves.

- PIL (Pillow): For deep image verification and preprocessing.

- NumPy: For tensor manipulation and array processing during inference.

## 📈 Performance & Results

The model achieved high stability between training and validation metrics, indicating successful regularization.

| Metric   | Value   |
| :----------- | :---------- |
| Final Accuracy | 91.6%    |
| Final Training loss | 0.2028 |
| Final Validation loss     | 0.2063  | 
| Validation accuracy  | 91.5%   |
| Epochs    | 25      |