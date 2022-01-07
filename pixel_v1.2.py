from PyQt5 import QtWidgets, uic, QtGui
import os
import serial
import time
from PIL import ImageGrab
import win32gui
import win32con
import ctypes




import psutil
# название программы
process_to_kill = "pixel.exe"

# получение id нашей программы
my_pid = os.getpid()

# удаляем другие копии программы
for p in psutil.process_iter():

    if p.name() == process_to_kill:

        if not p.pid == my_pid:
            p.kill()





r=0
g=0
b=0



x=1919       #разрешение
y=1079       #разрешение
lightsX=33   # вмещаемое количество светодиодов по X
lightsY=17   # вмещаемое количество светодиодов по Y
pixelsSum=lightsY+lightsY+lightsX+lightsX
# for i in range(1,1000):
#     pix = pyautogui.pixel(1, 1) #МЕДЛЕННО
# print(pix)

The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
# дизайн и кнопки
app=QtWidgets.QApplication([])
ui=uic.loadUi('pixel.ui')
app.setWindowIcon(QtGui.QIcon('q.png'))

for i in range(0,15):
    try:
        ser = serial.Serial("com"+str(i), 170200)
        break
    except:
        pass




# изменение цвета
def changeColor():
    for i in range(0,pixelsSum):
        if i%2==0:
            fillColor1()
        else:
            fillColor2()

# изменение цвета
def changeColor2():
    for i in range(0,pixelsSum):
        if i%2==0:
            fillColor1()
        else:
            fillColor2()





# заполнение цветом 1
def fillColor1():
    r=ui.red1.value()
    g=ui.green1.value()
    b=ui.blue1.value()
    sender(r,g,b)
    print(r,g,b)
# заполнение цветом 2
def fillColor2():
    r=ui.red2.value()
    g=ui.green2.value()
    b=ui.blue2.value()
    sender(r,g,b)
    print(r,g,b)
# скрыть программу
def hideAndShow():
    The_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
    while True:
        changeColor()
        changeColor2()



# отправка цвета
def sender(r,g,b):
    send=str(r)+'@'+str(g)+'#'+str(b)+'\n'
    ser.write(send.encode())
# sender=str(str(i)+'!'+str(color[0])+'@'+str(color[1])+'#'+str(color[2])+'\n')

# режим переливания
def colorful():
    r=0
    g=0
    b=0
    while True:

        for i in range(0,256,2):
            r=255-i
            g=i
            b=0
            for q in range(0,pixelsSum):
                sender(r,g,b)


        for i in range(0,256,2):
            g=255-i
            b=i
            r=0
            for q in range(0,pixelsSum):
                sender(r,g,b)




        for i in range(0,256,2):
            b=255-i
            r=i
            g=0
            for q in range(0,pixelsSum):
                sender(r,g,b)





# ambilight (самый главный режим)
def qww():
    The_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)




    px = ImageGrab.grab().load()



    while True:
        px = ImageGrab.grab().load()
        a=0

        for i in range(0,x,x//lightsX):
            color=px[i,y-30]
            sender(color[0],color[1],color[2])

            a+=1

        for i in range(y,0,-y//lightsY):
            color=px[x-30,i]
            sender(color[0],color[1],color[2])

            a+=1

        for i in range(x,0,-x//lightsX):
            color=px[i,30]
            sender(color[0],color[1],color[2])

            a+=1

        for i in range(0,y,y//lightsY):
            color=px[30,i]
            sender(color[0],color[1],color[2])

            a+=1

# The_program_to_hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
# дизайн и кнопки
ui.button.clicked.connect(qww)
ui.hideButton.clicked.connect(hideAndShow)
ui.colorfulQWW.clicked.connect(colorful)

ui.red1.valueChanged.connect(changeColor)
ui.green1.valueChanged.connect(changeColor)
ui.blue1.valueChanged.connect(changeColor)

ui.red2.valueChanged.connect(changeColor)
ui.green2.valueChanged.connect(changeColor)
ui.blue2.valueChanged.connect(changeColor)

ui.show()
app.exec()
