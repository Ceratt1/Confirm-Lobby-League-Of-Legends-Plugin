import pyautogui as PA
import cv2
import numpy as np
import pyscreenshot as ImageGrab

class CapAndReference:
    def __init__(self):
        self.RefImg = cv2.imread('img/aceitaradaptado.jpg')
        self.img = None
        self.ScreenResult = None
        self.location = None

    def capture_screen(self):
        screen = ImageGrab.grab()
        screen_np = np.array(screen)
        gray_image = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        bw_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        self.img = cv2.cvtColor(bw_image, cv2.COLOR_RGB2BGR)

        
    def find_image_on_screen(self):
        result = cv2.matchTemplate(self.img, self.RefImg, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        threshold = 0.4  # Valor de limiar para correspondência
        self.location = max_loc
        if max_val >= threshold:
            self.ScreenResult = True
        else:
            self.ScreenResult = False

    def click(self):
        if self.ScreenResult :
            PA.click(self.location)
        else:
            print('Tente ler a documentacao para ler seu possivel erro, caso precise de ajude mande mensagem\ngabrielceratticabral@gmail.com')

# test = CapAndReference()

# test.capture_screen()
# test.find_image_on_screen()
# test.click()