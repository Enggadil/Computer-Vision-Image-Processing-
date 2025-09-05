#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import os
import matplotlib.pyplot as plt

# ---- Set folder and filenames (change if needed) ----
folder = r"D:\CUNY 2025\CV\standard_test_images\standard_test_images"
file1 = "lena_gray_512.tif"    
file2 = "lena_color_512.tif"

# ---- Full paths ----
img1_path = os.path.join(folder, file1)
img2_path = os.path.join(folder, file2)

# ---- Load images in grayscale ----
img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

# ---- Check if loaded ----
if img1 is None or img2 is None:
    raise FileNotFoundError("One or both images could not be loaded. Check filenames and extensions!")

# ---- Resize second image to match first ----
if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# ---- Image algebra operations ----
add_img = cv2.add(img1, img2)
sub_img = cv2.subtract(img1, img2)
mul_img = cv2.multiply(img1, img2)
div_img = cv2.divide(img1, img2 + 1)  # +1 avoids division by zero

# ---- Display results ----
titles = ['Image 1', 'Image 2', 'Addition', 'Subtraction', 'Multiplication', 'Division']
images = [img1, img2, add_img, sub_img, mul_img, div_img]

plt.figure(figsize=(10,6))
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

# ---- Save results ----
output_folder = r"D:\CUNY 2025\CV\output"
os.makedirs(output_folder, exist_ok=True)

cv2.imwrite(os.path.join(output_folder, "add_result.jpg"), add_img)
cv2.imwrite(os.path.join(output_folder, "sub_result.jpg"), sub_img)
cv2.imwrite(os.path.join(output_folder, "mul_result.jpg"), mul_img)
cv2.imwrite(os.path.join(output_folder, "div_result.jpg"), div_img)

print("✅ All operations done. Results saved to:", output_folder)


# In[ ]:





# In[ ]:





# In[33]:


print(img)


# In[41]:


print(img.dtype)


# In[42]:


print(img.shape)


# In[43]:


print(img.ndim)


# In[37]:


print(img.size
     )


# In[51]:


add_img = cv2.add(img1, img2


# In[ ]:




