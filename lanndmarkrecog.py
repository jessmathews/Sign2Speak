import os
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt
mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
DATA_DIR='./data'
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR,dir_,))[:1]:
        img = cv2.imread(os.path.join(DATA_DIR,dir_,img_path))
        img_rgb=cv2.cvtcolor(img,cv2.COLOR_BGR2RGB)
        results= mp_hands.process(img_rgb)
    if results.multi_hand_land_marks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_1landmarks(
                img_rgb,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_styles()

            ) 
    plt.figure()
    plt.imshow(img_rgb)
plt.show()    