# 👁️ Computer Vision & Deep Learning Lab
This repository serves as a comprehensive laboratory for Computer Vision and Deep Learning. 
It ranges from foundational pixel-level manipulations using OpenCV to building and deploying high-accuracy CNN models with TensorFlow.

## 📂 Repository Structure
| Folder / File | Description | Key Tech|
| :------------ | :----------- | :---------- |
| Image Classification Cat VS Dog/ | End-to-end CNN pipeline achieving 91.5% validation accuracy. | TensorFlow, Keras, MLOps | 
| Computer Vision CV2/ | Foundational scripts for image loading, metadata inspection, and pixel manipulation. | OpenCV (cv2), NumPy |
| CIFAR-10 Exploration/  | Visualizing and inspecting the standard CIFAR-10 multi-class dataset. | Matplotlib, TensorFlow |

## 🚀 Projects & Modules

1. **Cat vs. Dog Classification (Deep Learning)**
- A robust binary classifier trained on the PetImages dataset.

- Key Features: Automated data cleaning (removing corrupt/zero-byte JPEGs), data augmentation, and a 4-layer CNN architecture.

- Performance: 91.6% Training Accuracy | 91.5% Validation Accuracy.

- Stack: TensorFlow, Keras, Matplotlib, Pillow.

2. **OpenCV Foundations**
Located in the Computer Vision CV2 section, these scripts demonstrate core image processing techniques:

- Inspection: Loading images and extracting metadata (Shape, Dtype, Mean Pixel Value).

- Pixel Manipulation: Accessing BGR channels and modifying specific coordinate ranges (ROIs) to alter image data.

- Interactive Visualization: Using cv2.imshow and cv2.waitKey for real-time image feedback.
  
- Normalization Logic: Calculating mean pixel values for data centering and feature scaling.

3. **Dataset Inspection (CIFAR-10)**
A specialized module for handling the CIFAR-10 dataset (60,000 32x32 color images in 10 classes).

- Visualization: Batch visualization of labeled training data using matplotlib.

- Preprocessing: Identification of image resolution and label mapping for multi-class classification preparation.

## 🛠️ Technical Implementation Details

#### Image Preprocessing
In this lab, I prioritize data integrity. Every image is validated before entering the model:

- OpenCV Loading: Images are loaded in BGR format, with checks for decoding errors.

- Normalization: Scaling pixel values from [0, 255] to [0, 1] to ensure faster convergence during gradient descent.

- Batch Sizing: Calculating nbytes of images to ensure batch sizes fit within GPU VRAM limits.

#### Model Optimization
- Optimizer: Adam

- Callback: ReduceLROnPlateau (monitors validation loss and decays learning rate by 0.2x).

- Regularization: Batch Normalization and Dropout (up to 0.5) to ensure the model generalizes to new, unseen data.

## 📦 Requirements & Setup

To run the files in this repository, you will need:
 ```bash
  pip install tensorflow opencv-python matplotlib pandas pillow numpy
  ```
## 🤝 Collaborative Approach
I believe in honest and humble engineering. I have documented these scripts to be easily understood by teammates. I value:

- Active Listening: Adapting code based on peer feedback.

- Thought Sharing: Providing clear comments on why specific architectures (like CNNs vs. Dense layers) were chosen.
  
  
