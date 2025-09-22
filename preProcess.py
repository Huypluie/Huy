import os
import cv2
import numpy as np
from tqdm import tqdm
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input
# Kích thước resize mong muốn
IMAGE_HEIGHT = 299
IMAGE_WIDTH = 299

# Hàm crop ảnh (giữ lại vùng có nội dung)
def crop_image_from_gray(img, tol=7):
    if img.ndim == 2:  # grayscale
        mask = img > tol
        return img[np.ix_(mask.any(1), mask.any(0))]
    elif img.ndim == 3:  # RGB
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        mask = gray_img > tol        
        if mask.any():
            img1 = img[:,:,0][np.ix_(mask.any(1), mask.any(0))]
            img2 = img[:,:,1][np.ix_(mask.any(1), mask.any(0))]
            img3 = img[:,:,2][np.ix_(mask.any(1), mask.any(0))]
            img = np.stack([img1,img2,img3], axis=-1)
        return img
    return img

# Hàm preprocess ảnh
def preprocess_image(image_path, sigmaX=10):
    image = cv2.imread(image_path)  # BGR
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # sang RGB ngay
    image = crop_image_from_gray(image)
    image = cv2.resize(image, (IMAGE_HEIGHT, IMAGE_WIDTH))
    image = cv2.addWeighted(image, 4, cv2.GaussianBlur(image, (0,0), sigmaX), -4, 128)

    # split theo RGB luôn
    r, g, b = cv2.split(image)

    # CLAHE lên kênh G
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8,8))
    g_clahe = clahe.apply(g)

    # merge lại
    img_clahe = cv2.merge((r, g_clahe, b))
    return img_clahe  # vẫn RGB