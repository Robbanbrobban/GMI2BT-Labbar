import os
from os import path
import cv2 as cv
import numpy as np

clear = lambda: os.system('cls')
#people = ['Avicii', 'Christian Bale', 'Lady Gaga']
#Tar oss till mappen vi är i
dir_path = os.getcwd()
#Lägger till så vi kommer till train mappen
train_path = r'dataset\faces\train'
#Sätter ihop så vi kommer till mappen för train faces
DIR = os.path.join(dir_path, train_path)
people = []
for i in os.listdir(DIR):
    people.append(i)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def header():
    print(r"______                   _      _            _             ")
    print(r"|  ___|                 | |    | |          | | ")
    print(r"| |_ __ _  ___ ___    __| | ___| |_ ___  ___| |_ ___  _ __")
    print(r"|  _/ _` |/ __/ _ \  / _` |/ _ \ __/ _ \/ __| __/ _ \| '__|")
    print(r"| || (_| | (_|  __/ | (_| |  __/ ||  __/ (__| || (_) | |")
    print(r"\_| \__,_|\___\___|  \__,_|\___|\__\___|\___|\__\___/|_|   ")
    print()
    
def menu():
    print(f'+———————————————( Face Detector)——————————————+')
    print('| 1. Info (How it works)                      |')
    print('| 2. Face trainer                             |')
    print('| 3. Face detector                            |')
    print('| 4. Exit program                             |')
    print(f'+—————————————————————————————————————————————+')
    
def info():
    
    print(f'+————————————————————————————( Information )—————————————————————————————+')
    print(f'|Images are downloaded with help of:                                     |')
    print(f'|"https://github.com/debadridtt/Scraping-Google-Images-using-Python"     |')
    print(f'|                                                                        |')
    print(f'|So first you use "Scraping-Google-Images-using-Python" to get the images|')
    print(f'|Then you use it to download the faces you wanna train/validate.         |')
    print(f'|                                                                        |')
    print(f'|Next the images have been resized and scaled (500x500px) in gimp        |')
    print(f'|And those are the images you want to use when you train the program     |')
    print(f'|                                                                        |')
    print(f'|To add more faces                                                       |')
    print(f'|Add images in folder named after that person in /dataset/faces/train/   |')
    print(f'|When you have trained the face detector and you want to validate images.|')
    print(f'|Put the images you want to validate in /dataset/faces/validate/         |')
    print(f'|                           Good Luck :D                                 |')
    input(f'|                           Press Enter to continue                      |')
    print(f'+————————————————————————————————————————————————————————————————————————+')
    
def face_training():
    print('————————————————————————————( Face training )————————————————————————————')
    features = []
    labels = []

    print('(Working)')
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in face_rect:
                faces_area = gray[y:y + h, x:x + w]
                features.append(faces_area)
                labels.append(label)
    print('\n———————————————————————( Face training finished )————————————————————————')

    features = np.array(features, dtype='object')
    labels = np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    # Train the Recognizer on the features list and the labels list
    face_recognizer.train(features, labels)
    face_recognizer.save('trainer.yml') 
    input(('———————————————————————( Press enter to continue )———————————————————————'))
    
def face_detect():
    print('——————————————————————————— ( Face recognition ) ———————————————————————————')
    print('Loops through all images in /dataset/faces/validate')
    print('Images should appear in a new window, close image to see the next image.')
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainer.yml')

    dir_path = os.getcwd()
    validate_path = r'dataset\faces\validate'
    path = os.path.join(dir_path, validate_path)

    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        img = cv.imread(img_path)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # hittar ansiktet i bilden
        face_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

        for (x, y, w, h) in face_rectangle:
            face_area = gray[y:y + h, x:x + w]

            label, confidence = face_recognizer.predict(face_area)
            # print(f'Label = {people[label]} with a confidence of {confidence}')
            img_label = f'{people[label]} {confidence:.2f}%'
            cv.putText(img, img_label, (30, 40), cv.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(0, 230, 0), thickness=2)
            cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 230, 0), thickness=2)

        cv.imshow('Detected Face', img)
        cv.waitKey(0)   
#Meny
while True:
    clear()
    header()
    menu()
    choice = input("Select a menu item: ")
    if choice == '1':
        info()
    elif choice == '2':
        face_training()
    elif choice == '3':
        face_detect()
    elif choice == '4':
        # Stänger av programmet
        break
    else:
        print("Invalid selection item, please try again.")