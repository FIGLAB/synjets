import pyaudio
import wave
import sys
import serial
import time
import threading
import numpy as np
import random
import cv2

CHUNK = 1024
baud = 115200
timestart = time.time()
cv2.namedWindow("distance", cv2.WINDOW_AUTOSIZE)
detent_time = False

# no hand found background
nohand = np.zeros((780,450))+255
nohand = cv2.putText(nohand, str("NO HAND FOUND"), (50,350), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0,0,0), 4)

# detents background
det_bg = np.zeros((780,450,3)) + 255
cv2.rectangle(det_bg, (100,90), (350,95), (0,0,0), -1)
cv2.rectangle(det_bg, (100,130), (350,135), (0,0,0), -1)
cv2.rectangle(det_bg, (100,170), (350,175), (0,0,0), -1)
cv2.rectangle(det_bg, (100,210), (350,215), (0,0,0), -1)
cv2.rectangle(det_bg, (100,250), (350,255), (0,0,0), -1)
cv2.rectangle(det_bg, (100,290), (350,295), (0,0,0), -1)
cv2.rectangle(det_bg, (100,330), (350,335), (0,0,0), -1)
cv2.rectangle(det_bg, (100,370), (350,375), (0,0,0), -1)
cv2.rectangle(det_bg, (100,410), (350,415), (0,0,0), -1)
cv2.rectangle(det_bg, (100,450), (350,455), (0,0,0), -1)
cv2.rectangle(det_bg, (100,490), (350,495), (0,0,0), -1)
cv2.rectangle(det_bg, (100,530), (350,535), (0,0,0), -1)
cv2.rectangle(det_bg, (100,570), (350,575), (0,0,0), -1)
cv2.rectangle(det_bg, (100,610), (350,615), (0,0,0), -1)
cv2.rectangle(det_bg, (100,650), (350,655), (0,0,0), -1)
cv2.rectangle(det_bg, (100,690), (350,695), (0,0,0), -1)
cv2.rectangle(det_bg, (100,730), (350,780), (0,0,0), -1)

# button background
but_bg = np.zeros((780,450,3)) + 255
cv2.rectangle(but_bg, (100,500), (350,580), (0,0,255), -1)
cv2.rectangle(but_bg, (100,700), (350,780), (0,0,0), -1)

def click(ser, sec=25):
    global detent_time
    print("click!")
    timestart = time.time()
    disp = but_bg
    prevdist = 0
    while True:
        feedback = ser.readline().decode('utf-8')
        print(feedback)
        if "ERROR" in feedback.strip() or feedback.strip()=="":
            cv2.imshow("distance", nohand)
            key = cv2.waitKey(1)
            if key==ord('d'):
                detent_time=True
                break
            dist = 0.0
            continue
        # disp = np.copy(but_bg)
        dist = float(feedback)
        if dist > 42 and dist < 60:
            cv2.rectangle(disp, (100,400), (350,680), (255,255,255), -1)
            cv2.rectangle(disp, (100,500), (350,580), (0,255,0), -1)
        elif dist < 42 or dist > 60:
            cv2.rectangle(disp, (100,500), (350,580), (0,0,255), -1)
            cv2.circle(disp,(225,int(700-(prevdist-20)*700/140)),15,(255,255,255),-1)

        cv2.circle(disp,(225,int(700-(dist-20)*700/140)),15,(255,0,0),-1)
        cv2.rectangle(disp, (0,0),(100,100), (255,255,255), -1)
        cv2.putText(disp, str(int(dist)), (0,50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0,0,0), 3)
        cv2.imshow("distance", disp)
        prevdist = dist
        key = cv2.waitKey(1)
        if key==ord('d'):
            print("detent_time")
            detent_time=True
            break

prevdist = 120
dists = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def detents(ser, sec=25):
    print("detents!")
    dist = 0
    prevdist = 120
    disp = det_bg
    prevy = 0
    while True:
        feedback = ser.readline().decode('utf-8')
        if "ERROR" in feedback.strip():
            cv2.imshow("distance", nohand)
            key = cv2.waitKey(5)
            if key==("d"):
                detent_time=True
                break
            dist = 0.0
            continue
        dist = float(feedback)
        cen_y = int(700-(dist-20)*700/140)
        if abs(prevdist-dist) > 10:
            timestart = time.time()
            prevdist = closest(dists, dist)
            cv2.circle(disp,(225,cen_y),15,(0,255,0),-1)
        else:
            cv2.circle(disp,(225,cen_y),15,(255,0,0),-1)

        cv2.circle(disp,(225,prevy),15,(255,255,255),-1)
        cv2.rectangle(disp, (0,0),(100,100), (255,255,255), -1)
        cv2.putText(disp, str(int(dist)), (0,50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0,0,0), 3)
        prevy = cen_y
        cv2.imshow("distance", disp)
        key = cv2.waitKey(1)

if __name__ == "__main__":
    # instantiate Serial
    ser = serial.Serial('COM13', baud, timeout=1)
    time.sleep(3)

    click(ser)
    detents(ser)

    # close everything
    ser.close()
