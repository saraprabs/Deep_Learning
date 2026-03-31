import tensorflow as tf
from tensorflow.keras import datasets
import matplotlib.pyplot as plt

# 1. Load the dataset
# This will automatically download it (~170MB) if it's not on your computer
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# 2. Define the class names (CIFAR-10 labels are just numbers 0-9)
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# 3. Visualize the first 15 images
plt.figure(figsize=(10,6))
for i in range(15):
    plt.subplot(3, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i])
    # The labels are arrays, so we need the extra index
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

# Print the resolution to confirm
print(f"Image shape: {train_images[0].shape}")