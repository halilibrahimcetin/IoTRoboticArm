import tkinter as tk
import matplotlib.pyplot as plt
import math
import numpy as np
import time
from time import sleep
import numpy as np
from piservo import Servo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
##########################################
from tkinter.ttk import Combobox
from ntpath import join
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider
from matplotlib import animation
from gpiozero import AngularServo
##########################################

x=Servo(18, min_value=0, max_value=180, min_pulse=0.5, max_pulse=2.4, frequency=50)
y=Servo(12,min_value=0, max_value=180, min_pulse=0.5, max_pulse=2.4, frequency=50)
z=Servo(13,min_value=0, max_value=160, min_pulse=0.659, max_pulse=2.56, frequency=50)

#servox=AngularServo(18, min_angle=0, max_angle=200, min_pulse_width=0.0005, max_pulse_width=0.0025)
#servoy=AngularServo(12, min_angle=0, max_angle=200, min_pulse_width=0.0005, max_pulse_width=0.0025)
#servoz=AngularServo(13, min_angle=0, max_angle=200, min_pulse_width=0.0005, max_pulse_width=0.0025)
#x.start()
#y.start()
#z.start()

form=tk.Tk()
form.title('Robot Kol Arayüz v1"')
form.resizable(False,False)
form.config(bg='gray')
form.geometry('500x500+100+100')
servoderece=tk.IntVar()
secilenservo=tk.StringVar()

label=tk.Label(text='HANGİ SERVO?',bg='gray',fg='black').pack()
values=['X','Y','Z']
servosec=Combobox(form,values=values,height=3,textvariable=secilenservo,).pack()
label2=tk.Label(text='Kaç derece döndürmek istiyorsunuz?',bg='gray',fg='black').pack()
spin=tk.Spinbox(form,from_=0,to=180,textvariable=servoderece).pack()
label3=tk.Label(text='X ve Y için 0 ile 180 derece arası\nZ için 0 ile 160 derece arası bir değer giriniz',bg='gray',fg='black').pack()

def yazdır():
    if secilenservo.get() == 'X':
        #servox.angle = int((servoderece.get()))
        x.start()
        x.write(int(servoderece.get()))
        Xguncelle(int(x.read()))
        if (servoderece.get() > 140):
            pass
        elif (servoderece.get() < 25):
            pass
        else:
            x.stop()
    elif secilenservo.get() == 'Y':
        #servoy.angle = int((servoderece.get()))
        y.start()
        y.write(int(servoderece.get()))
        Yguncelle(int(y.read()))
        if (servoderece.get() > 140):
            pass
        elif (servoderece.get() < 25):
            pass
        else:
            y.stop()
    elif secilenservo.get() == 'Z':
        #servoz.angle = int((servoderece.get()))
        z.start()
        z.write(int(servoderece.get()))
        Zguncelle(int(z.read()))
        if (servoderece.get() > 140):
            pass
        elif (servoderece.get() < 25):
            pass
        else:
            z.stop()
    print(secilenservo.get(),',',servoderece.get(),'derece döndürüldü')

buton=tk.Button(form,text='DÖNDÜR',command=yazdır,activebackground='blue',activeforeground='green').pack()

home = [0 , 0, 0]
alt_kısım =0
uzun_kol_uzunluk=15
kucuk_kol_uzunluk=5
eklem1 = 0
eklem2 = 0
eklem3 = 0
nokta1 = [0,0,0]
nokta2 = [0,0,0]
nokta3 = [0,0,0]

#xplot=x.read()
#yplot=y.read()
#zplot=z.read()

#xSlider = plt.axes([0.2, 0.1, 0.65, 0.03])
#ySlider = plt.axes([0.2, 0.065, 0.65, 0.03])
#zSlider = plt.axes([0.2, 0.03, 0.65, 0.03])

#sliderX = Slider(xSlider, 'X', 0, 180.0, valinit=0, valstep=1)
#sliderY = Slider(ySlider, 'Y', 0, 180.0, valinit=-90,valstep=1)
#sliderZ = Slider(zSlider, 'Z', -90, 90.0, valinit=-90, valstep=1)


figure = plt.figure(figsize=(7,7))
Axes = figure.add_subplot(111,projection='3d')

def forwKinematik(aci1,aci2,aci3):
    # 1.nokta
    trans = np.dot(np.matrix([[1,0,0,alt_kısım],
                             [0,1,0,0],
                             [0,0,1,0],
                             [0,0,0,1]]),np.matrix([home[0],home[1],home[2],1]).transpose())
    nokta1[0] = trans[(0,0)]
    nokta1[1] = trans[(1,0)]
    nokta1[2] = trans[(2,0)]

    rot = np.dot(np.matrix([[math.cos(math.radians(aci1)),-math.sin(math.radians(aci1)),0,0],
                        [math.sin(math.radians(aci1)),math.cos(math.radians(aci1)),0,0],
                        [0,0,1,0],
                        [0,0,0,1]]),np.matrix([nokta1[0],nokta1[1],nokta1[2],1]).transpose())
    nokta1[0] = rot[(0,0)]
    nokta1[1] = rot[(1,0)]
    nokta1[2] = rot[(2,0)]
    
    # 2.nokta
    trans = np.dot(np.matrix([[1,0,0,uzun_kol_uzunluk],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]]),np.matrix([home[0],home[1],home[2],1]).transpose())
    nokta2[0] = trans[(0,0)]
    nokta2[1] = trans[(1,0)]
    nokta2[2] = trans[(2,0)]

    rot = np.dot(np.matrix([[math.cos(math.radians(aci2)),0,math.sin(math.radians(aci2)),0],
                        [0,1,0,0],
                        [-math.sin(math.radians(aci2)),0,math.cos(math.radians(aci2)),0],
                        [0,0,0,1]]),np.matrix([nokta2[0],nokta2[1],nokta2[2],1]).transpose())
    
    nokta2[0] = rot[(0,0)]
    nokta2[1] = rot[(1,0)]
    nokta2[2] = rot[(2,0)]

    trans = np.dot(np.matrix([[1,0,0,alt_kısım],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]]),np.matrix([nokta2[0],nokta2[1],nokta2[2],1]).transpose())
    nokta2[0] = trans[(0,0)]
    nokta2[1] = trans[(1,0)]
    nokta2[2] = trans[(2,0)]

    rot = np.dot(np.matrix([[math.cos(math.radians(aci1)),-math.sin(math.radians(aci1)),0,0],
                        [math.sin(math.radians(aci1)),math.cos(math.radians(aci1)),0,0],
                        [0,0,1,0],
                        [0,0,0,1]]),np.matrix([nokta2[0],nokta2[1],nokta2[2],1]).transpose())
    
    nokta2[0] = rot[(0,0)]
    nokta2[1] = rot[(1,0)]
    nokta2[2] = rot[(2,0)]

    # 3.nokta
    trans = np.dot(np.matrix([[1,0,0,kucuk_kol_uzunluk],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]]),np.matrix([home[0],home[1],home[2],1]).transpose())
    nokta3[0] = trans[(0,0)]
    nokta3[1] = trans[(1,0)]
    nokta3[2] = trans[(2,0)]

    rot = np.dot(np.matrix([[math.cos(math.radians(aci3)),0,math.sin(math.radians(aci3)),0],
                        [0,1,0,0],
                        [-math.sin(math.radians(aci3)),0,math.cos(math.radians(aci3)),0],
                        [0,0,0,1]]),np.matrix([nokta3[0],nokta3[1],nokta3[2],1]).transpose())
    
    nokta3[0] = rot[(0,0)]
    nokta3[1] = rot[(1,0)]
    nokta3[2] = rot[(2,0)]

    trans = np.dot(np.matrix([[1,0,0,uzun_kol_uzunluk],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]]),np.matrix([nokta3[0],nokta3[1],nokta3[2],1]).transpose())
    nokta3[0] = trans[(0,0)]
    nokta3[1] = trans[(1,0)]
    nokta3[2] = trans[(2,0)]

    rot = np.dot(np.matrix([[math.cos(math.radians(aci2)),0,math.sin(math.radians(aci2)),0],
                        [0,1,0,0],
                        [-math.sin(math.radians(aci2)),0,math.cos(math.radians(aci2)),0],
                        [0,0,0,1]]),np.matrix([nokta3[0],nokta3[1],nokta3[2],1]).transpose())

    nokta3[0] = rot[(0,0)]
    nokta3[1] = rot[(1,0)]
    nokta3[2] = rot[(2,0)] 
    
    trans = np.dot(np.matrix([[1,0,0,alt_kısım],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]]),np.matrix([nokta3[0],nokta3[1],nokta3[2],1]).transpose())
    nokta3[0] = trans[(0,0)]
    nokta3[1] = trans[(1,0)]
    nokta3[2] = trans[(2,0)]

    rot = np.dot(np.matrix([[math.cos(math.radians(aci1)),-math.sin(math.radians(aci1)),0,0],
                        [math.sin(math.radians(aci1)),math.cos(math.radians(aci1)),0,0],
                        [0,0,1,0],
                        [0,0,0,1]]),np.matrix([nokta3[0],nokta3[1],nokta3[2],1]).transpose())
    
    nokta3[0] = rot[(0,0)]
    nokta3[1] = rot[(1,0)]
    nokta3[2] = rot[(2,0)]


    return nokta1, nokta2, nokta3


def Xguncelle(value):
    global eklem1
    if value >180:
        value = 180
    elif value <0:
        value = 0
    eklem1 = value
    Axes.clear()

    nokta1, nokta2, nokta3 = forwKinematik(-eklem1, -eklem2, -eklem3)

    Axes.plot([home[0], nokta1[0]], [home[1], nokta1[1]], [home[2], nokta1[2]])
    Axes.plot([nokta1[0], nokta2[0]], [nokta1[1], nokta2[1]], [nokta1[2], nokta2[2]])
    Axes.plot([nokta2[0], nokta3[0]], [nokta2[1], nokta3[1]], [nokta2[2], nokta3[2]])

    Axes.plot([-10,10],[0,0],[0,0], color='red',linewidth=1)
    Axes.plot([0,0],[-10,10],[0,0], color='green',linewidth=1)
    Axes.plot([0,0],[0,0],[-10,10], color='blue',linewidth=1)
    canvas.draw()

def Yguncelle(value):
    global eklem2
    if value > 180:
        value = 180
    elif value < 0:
        value = 0
    eklem2 = value
    Axes.clear()
    canvas.draw()

    nokta1, nokta2, nokta3 = forwKinematik(-eklem1, -eklem2, -eklem3)

    Axes.plot([home[0], nokta1[0]], [home[1], nokta1[1]], [home[2], nokta1[2]])
    Axes.plot([nokta1[0], nokta2[0]], [nokta1[1], nokta2[1]], [nokta1[2], nokta2[2]])
    Axes.plot([nokta2[0], nokta3[0]], [nokta2[1], nokta3[1]], [nokta2[2], nokta3[2]])

    Axes.plot([-10,10], [0,0], [0,0], color='red',linewidth=1)
    Axes.plot([0,0], [-10,10], [0,0], color='green',linewidth=1)
    Axes.plot([0,0], [0,0], [-10,10], color='blue',linewidth=1)
    canvas.draw()


def Zguncelle(value=z.read()):
    value=value-90
    global eklem3
    if value > 160:
        value = 160
    elif value < -90:
        value = -90
    eklem3 = -value
    Axes.clear()

    nokta1, nokta2, nokta3 = forwKinematik(-eklem1, -eklem2, -eklem3)

    Axes.plot([home[0], nokta1[0]], [home[1], nokta1[1]], [home[2], nokta1[2]])
    Axes.plot([nokta1[0], nokta2[0]], [nokta1[1], nokta2[1]], [nokta1[2], nokta2[2]])
    Axes.plot([nokta2[0], nokta3[0]], [nokta2[1], nokta3[1]], [nokta2[2], nokta3[2]])

    Axes.plot([-10,10],[0,0],[0,0], color='red',linewidth=1)
    Axes.plot([0,0],[-10,10],[0,0], color='green',linewidth=1)
    Axes.plot([0,0],[0,0],[-10,10], color='blue',linewidth=1)
    canvas.draw()

canvas = FigureCanvasTkAgg(figure, form)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
toolbar = NavigationToolbar2Tk(canvas, form)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#sliderX.on_changed(Xguncelle)
#sliderY.on_changed(Yguncelle)
#sliderZ.on_changed(Zguncelle)


form.mainloop()