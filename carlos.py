import pyautogui as py
import time
import os
#importou a biblioteca para o arquivo que eu criei

py.press('win') #press = pressiona, 'win' = windows
time.sleep(1) #descanse 1 seg, você tem que colocar 1 seg, pq se n colocar, ele fará em velocidade de maquina
py.write("google") #digite notepad
time.sleep(1)# espere 1 seg
py.press("enter")#pressione enter
time.sleep(1) #espere 2 seg
py.click(1896, 97)
py.click(1632, 205)
py.write("youtube google")
py.press("enter")
time.sleep(1)
py.click(245, 687)
time.sleep(1)
py.click(718, 134)
py.write("rabetao mc lan")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.click(380, 770)
os.system("pause") #pauseOl viadinho, gostou da minha tecnologia