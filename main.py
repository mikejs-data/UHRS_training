import cv2
import pytesseract


#Mouse Callback Function
def capture_coordinates(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


image = cv2.imread('test4.png')
WIDTH, HEIGHT, _ = image.shape
# print(WIDTH, HEIGHT)
cv2.namedWindow('my_image', cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow('my_image', HEIGHT//3, WIDTH//3)
cv2.imshow('my_image', image)

#Cropping Image and Saving
# crop = image[1280:1650, 161:377]
# cv2.imshow('my_image', crop)
# cv2.imwrite('crop.jpg', crop)

#Mouse Callback
cv2.setMouseCallback('my_image', capture_coordinates)

label = image[1447:1480, 1131:1280]
# cv2.imshow('my_image', label)

label = pytesseract.image_to_string(label)
if label.startswith('Abuse'):
    label = 'Abuse'
else:
    label = label.split()[0]

print(label)
cv2.waitKey(0)

# 161 1298
# 377 1301

# 1131 1447
# 1281 1480
