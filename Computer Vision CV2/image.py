""" Load and Inspect an Image using OpenCV"""
import cv2
import os

image_path = r'C:\Users\Elev\Deep Learning\Red_Deli.jpg' # r is prefix for raw string 

if not os.path.exists(image_path):
    print(f"Error: The file {image_path} does not exist! ")
else:
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: could not decode the image. It might be corrupted or an unsupported format.")
    else:
        print(f"Image loaded successfully!")
        print(f"Image Shape (Height, Width, Channels): {img.shape}")
        # Height = number of rows, Width = number of columns, Channels = number of color channels (e.g., 3 for RGB)
        print(f"Image dimensions: {img.ndim}") # Number of dimensions (should be 3 for a color image)
        print(f"Image Data Type: {img.dtype}") # Most images load as 8-bit integers (0-255). Models often need float32
        print(f"Image Size (Bytes): {img.nbytes}") #Helps you calculate if your "Batch Size" will fit in your GPU VRAM.
        print(f"Image Pixel Value Range: [{img.min()}, {img.max()}]") #If max is 255, it's raw. If max is 1.0, it’s already normalized.
        print(f"Image Mean Pixel Value: {img.mean():.2f}") # Average brightness of the image. Can be useful for normalization or data augmentation.
        #Used for Mean Subtraction, a common preprocessing step to center data.
        
        # LOAD THE IMAGE 
        cv2.imshow('Red Deli', img) 
        print("Press any key on the image window to close it...")
        
        # wait must be called after imshow to keep the window open otherwise it will freeze or crash
        cv2.waitKey(0) # Waits indefinitely until a key is pressed

        cv2.destroyAllWindows() # Closes all OpenCV windows

       