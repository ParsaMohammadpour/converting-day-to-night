#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[136]:


img = cv2.imread('day.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


# In[137]:


# img = img * np.array([0.1, 0.2, 0.5])
img = img * np.array([0.5, 0.3, 0.7])
img_max = img.max()
img = (255 * img) / img_max
img = img.astype(np.uint8)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


# In[138]:


gama = 2
img = 255 * (((img / 255)) ** gama)
img = np.array(img, dtype='uint8')
cv2.imwrite('night.jpg', img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


# # Source: mlwithpython
