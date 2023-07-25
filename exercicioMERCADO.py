import pyautogui as py
import time
import os
#importou a biblioteca para o arquivo que eu criei

x = 226  # coordenada horizontal
y = 396  # coordenada vertical

py.press('win') #press = pressiona, 'win' = windows
time.sleep(1) #descanse 1 seg, você tem que colocar 1 seg, pq se n colocar, ele fará em velocidade de maquina
py.write("excel") #digite notepad
time.sleep(1)# espere 1 seg
py.press("enter")#pressione enter
time.sleep(1)
py.moveTo(x, y)
time.sleep(1)
py.click(226, 396)
py.press("enter")
time.sleep(9)
py.click(310, 360)
py.hotkey('ctrl','c') #hotkey é para apertar mais de 2 teclas ao mesmo tempo
time.sleep(1)

py.press('win')
py.write("bloco de notas")
time.sleep(1)
py.press("enter")
py.hotkey('ctrl','v')

os.system("pause") #pause