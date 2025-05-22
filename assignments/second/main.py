import cv2
import numpy as np
import matplotlib.pyplot as plt

def resize_image(image_path):
    img = cv2.imread(image_path)
    return cv2.resize(img, (200, 200))

def process_image1(image_path):
    img = resize_image(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _, binary = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    _, binary_inv = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)
    _, trunc = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TRUNC)
    _, tozero = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO)
    
    plt.figure(figsize=(10, 8))
    
    plt.subplot(2, 2, 1)
    plt.title('THRESH_BINARY')
    plt.imshow(binary, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.title('THRESH_BINARY_INV')
    plt.imshow(binary_inv, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.title('THRESH_TRUNC')
    plt.imshow(trunc, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 4)
    plt.title('THRESH_TOZERO')
    plt.imshow(tozero, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('image1_thresholding.png')
    plt.close()

def process_image2(image_path):
    img = resize_image(image_path)
    
    gamma = 0.25
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')
    
    kernel = np.ones((3, 3), np.float32) / 9
    filter2d_img = cv2.filter2D(img, -1, kernel)
    
    blur_img = cv2.blur(img, (3, 3))
    
    gaussian_blur_img = cv2.GaussianBlur(img, (3, 3), 10)
    
    median_blur_img = cv2.medianBlur(img, 3)
    
    plt.figure(figsize=(12, 12))
    
    plt.subplot(3, 2, 1)
    plt.title('Gamma Correction (gamma=0.25)')
    plt.imshow(cv2.cvtColor(gamma_corrected, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(3, 2, 2)
    plt.title('2D Filter (3x3 kernel)')
    plt.imshow(cv2.cvtColor(filter2d_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(3, 2, 3)
    plt.title('Blur (ksize=(3,3))')
    plt.imshow(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(3, 2, 4)
    plt.title('Gaussian Blur (ksize=(3,3), sigmaX=10)')
    plt.imshow(cv2.cvtColor(gaussian_blur_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(3, 2, 5)
    plt.title('Median Blur (ksize=3)')
    plt.imshow(cv2.cvtColor(median_blur_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('image2_smoothing.png')
    plt.close()

def process_image3(image_path):
    img = resize_image(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_x = cv2.convertScaleAbs(sobel_x)
    
    sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    
    laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    
    plt.figure(figsize=(10, 8))
    
    plt.subplot(2, 2, 1)
    plt.title('Sobel X')
    plt.imshow(sobel_x, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.title('Sobel Y')
    plt.imshow(sobel_y, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.title('Laplacian')
    plt.imshow(laplacian, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('image3_edge_detection.png')
    plt.close()

def process_image4(image_path):
    img = resize_image(image_path)
    
    img_rect = img.copy()
    cv2.rectangle(img_rect, (50, 50), (150, 150), (0, 0, 255), 2)
    
    img_circle = img.copy()
    cv2.circle(img_circle, (100, 100), 50, (0, 0, 255), 2)
    
    img_line = img.copy()
    cv2.line(img_line, (25, 25), (175, 175), (0, 0, 255), 2)
    
    plt.figure(figsize=(10, 8))
    
    plt.subplot(2, 2, 1)
    plt.title('Rectangle')
    plt.imshow(cv2.cvtColor(img_rect, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.title('Circle')
    plt.imshow(cv2.cvtColor(img_circle, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.title('Diagonal Line')
    plt.imshow(cv2.cvtColor(img_line, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('image4_drawing.png')
    plt.close()

def main():
    process_image1('image1.jpeg')
    process_image2('image2.jpeg')
    process_image3('image3.jpeg')
    process_image4('image4.jpeg')
    
    print("All image processing tasks completed successfully!")

if __name__ == "__main__":
    main()
