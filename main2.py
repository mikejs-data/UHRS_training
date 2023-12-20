import cv2
import pytesseract
import os


def main(filename):
    # READ THE IMAGE
    image = cv2.imread(f'images/{filename}')

    # READ AND OCR THE LABEL
    label_image = image[1447:1480, 1131:1280]
    label = pytesseract.image_to_string(label_image)
    if label.startswith('Abuse'):
        label = 'Abuse'
    else:
        label = label.split()[0]

    # CROP THE IMAGE
    crop = image[1280:1650, 161:377]

    # SAVE FILE
    file_number = 0
    file_name = f'{label}.png'
    while os.path.exists(f'result/{file_name}'):
        file_number += 1
        file_name = f'{label} ({file_number}).png'
    cv2.imwrite(f'result/{file_name}', crop)

    # Suggestive, Abuse, Mild Racy, Youth Safety, Adult, Hate, Violence, Dangerous, Ok, #0
    cv2.waitKey(0)


if __name__ == '__main__':
    for file in os.listdir('images'):
        try:
            main(file)
        except:
            print(file)
            pass
