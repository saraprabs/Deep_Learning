""" 
Access and modify specific pixels in an image using OpenCV
Print its values
Modify that pixel to a new color
Display the updated image
"""
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
        # Access a single pixel at specific coordinates (y, x)
        # Let's look at the pixel at Row 100, Column 50
        y, x = 100, 50
        pixel_value = img[y, x]
        print(f"Original BGR value at ({y}, {x}): {pixel_value}")

        # Print individual color channels
        blue = img[y, x, 0]   # pixel [0] is Blue channel
        green = img[y, x, 1]  # pixel [1] is Green channel
        red = img[y, x, 2]    # pixel [2] is Red channel
        print(f"Individual channels - B: {blue}, G: {green}, R: {red}")

        # Modify that pixel to a new color (e.g., bright Yellow)
        # Yellow in BGR is (0, 255, 255)
        img[y, x] = [0, 255, 255]
        print(f"New BGR value at ({y}, {x}): {img[y, x]}")

        # Modify a larger "patch" so you can actually see it
        # Changes a 20x20 square to Green
        # image[row_start:row_end(Y-Axis), col_start:col_end(X-axis), channel_index(::2)skip pixels scaling down the image]
        img[150:170, 150:170] = [0, 255, 0]
    
        # LOAD THE IMAGE 
        cv2.imshow('Loaded Image', img) 
        print("Press any key on the image window to close it...")
        
        # wait must be called after imshow to keep the window open otherwise it will freeze or crash
        cv2.waitKey(0) # Waits indefinitely until a key is pressed

        cv2.destroyAllWindows() # Closes all OpenCV windows

        