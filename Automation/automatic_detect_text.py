import pyautogui
import time
import datetime
import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['db']
collection = db['collection']

pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def click():
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def get_frames():
    img = ImageGrab.grab(bbox=(354, 803, 402, 830))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    show = pytesseract.image_to_string(frame, lang='eng', config='--psm 6')
    show = show.strip()
    return show

exito = 0
fracaso = 0
hasta = 400
for _ in range(0, hasta):
    pyautogui.write("1")
    click()
    time.sleep(4)
    day = datetime.datetime.now().strftime("%d")
    tiempo = datetime.datetime.now().strftime("%H:%M:%S")
    time.sleep(1.5)
    sucess = get_frames()
    
    if sucess == "raised":
        print(tiempo)
        exito +=1
        dic = {"day":day, "weekday": "Friday", "tiempo": datetime.datetime.now(), "tiempo_humano": tiempo,"success": 1, "string": sucess}
    else:
        dic = {"day":day, "weekday": "Friday", "tiempo": datetime.datetime.now(), "tiempo_humano": tiempo,"success": 0, "string": sucess}
        fracaso +=1
    collection.insert_one(dic)

collection = db['promedio']
promedio = exito/331
dic = {"promedio": promedio, "exito":exito, "fracaso":fracaso, "exito-fracaso" : exito/hasta}
collection.insert_one(dic)
print(exito)
print(fracaso)
print(exito/hasta)