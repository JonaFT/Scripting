import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab
from twilio.rest import Client


pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def whatsupp(boss):
        account_sid = 'secret_sid'
        auth_token = 'secret_token'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                body=f'{boss}',
                                from_='whatsapp:+14155238886',
                                to='whatsapp:+34mynumber'
                                )

        print(message.sid)

while (True):
        img = ImageGrab.grab(bbox=(800, 700, 1300, 900))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
        show = pytesseract.image_to_string(frame, lang='eng', config='--psm 6')
        show = show.strip()
        with open(r"C:\Users\User\Desktop\twilio\abc.txt", "a") as f:
                f.write(show)
        print(show)
        if "Sis" in show:
                print("GOOD IT")
                whatsupp(show)
                break

