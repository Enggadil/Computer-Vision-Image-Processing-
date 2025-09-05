# Computer-Vision-Image-Processing-
I learned how to apply basic image algebra operations using Python and OpenCV. Images are represented as pixel matrices, and we can perform mathematical operations on them directly.

1.	Loading Images
o	Used cv2.imread() to load standard test images (Lena).
o	Converted them to grayscale for easy processing.
o	Resized them to the same size so operations could be done pixel by pixel.

2.	Image Algebra Operations
o	Addition: Brightens or blends images.
o	Subtraction: Detects changes or differences between images.
o	Multiplication: Adjusts contrast or applies masking.
o	Division:  Normalizes intensity and can remove shadows.

3.	Results
o	Displayed original and processed images using matplotlib.
o	Saved results (add_result.jpg, sub_result.jpg, mul_result.jpg, div_result.jpg) to the output folder.

4.	Learning Outcome
o	Understood how pixel values (0–255) can be manipulated with arithmetic.
o	Saw how simple operations can be useful in real-world applications such as brightness adjustment, motion detection, contrast enhancement, and shadow removal.
o	Gained practical skills in using OpenCV (cv2) for computer vision tasks.
