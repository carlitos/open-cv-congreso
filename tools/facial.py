"""
Author: Rodolfo Ferro @ Datlacuache
Twitter: @rodo_ferro

Script: Face detection tools module.
"""

import os

import cv2


def extract_faces_from_image(image_path,
                             cascade_path,
                             output_dir,
                             padding=0,
                             scale_factor=1.3,
                             min_neighbors=5,
                             extension='jpg'):
    """Detects faces in an image."""

    # If output folder does not exist, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    base_name = os.path.basename(image_path).split('.')[0]

    # Load cascade
    cascade = cv2.CascadeClassifier(cascade_path)

    # Detect faces
    faces = cascade.detectMultiScale(gray, scale_factor, min_neighbors)

    for index, (x, y, w, h) in enumerate(faces):
        if x - padding > 0:
            x_init = x - padding
        else:
            x_init = x

        if x + w + padding < img.shape[1]:
            x_end = x + w + padding
        else:
            x_end = x + w

        if y - padding > 0:
            y_init = y - padding
        else:
            y_init = y

        if y + h + padding < img.shape[0]:
            y_end = y + h + padding
        else:
            y_end = y + h

        roi_color = img[y_init:y_end, x_init:x_end]
        out_face_path = os.path.join(
            output_dir, f'{base_name}_{index + 1:0>5}.{extension}')
        cv2.imwrite(out_face_path, roi_color)
