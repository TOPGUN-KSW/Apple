import cv2
import numpy as np
import glob
import pandas as pd
import natsort
images = natsort.natsorted(glob.glob('./Machine_Learning/new_rembg_apples/*.png')) #폴더에 있는 파일들 숫자 순서대로 불러오기
text=open('./Machine_Learning/Apple_attribute6.txt', 'w')
print("red, green, blue, H, S, V, r, rg, most_red, least_red, most_yellow", file=text) #특성
for fname in images:
  im = cv2.imread(fname)
  red_sum = 0
  green_sum = 0
  blue_sum = 0
  H_sum = 0
  S_sum = 0
  V_sum = 0
  least_red = 0
  most_yellow = 0
  most_red = 0
  count = 0
  HSV = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
  for i in range(1, im.shape[0], 10):
    for j in range(1, im.shape[1], 10):
      if im[i, j][2] > 1:
        red_sum = red_sum + im[i, j][2]
        green_sum = green_sum + im[i, j][1]
        blue_sum = blue_sum + im[i, j][0]
        H_sum = H_sum + HSV[i, j][0]
        S_sum = S_sum + HSV[i, j][1]
        V_sum = V_sum + HSV[i, j][2]
        red = float(im[i, j][2])
        green = float(im[i, j][1])
        blue = float(im[i, j][0])
        if red - green - blue > most_red:
          most_red = round(red - green - blue, 2)
        if red - green - blue < least_red:
          least_red = round(red - green - blue, 2)
        if red + green - blue > most_yellow:
          most_yellow = round(red + green - blue, 2)
        count += 1
  average_red = round(red_sum / count, 2)
  average_green = round(green_sum / count, 2)
  average_blue = round(blue_sum / count, 2)
  H = round(H_sum / count, 2)
  S = round(S_sum / count, 2)
  V = round(V_sum / count, 2)
  rg = round(average_red + average_green - average_blue, 2)
  r = round(average_red - average_green - average_blue, 2)
  print(average_red, file=text, end =', ')
  print(average_green, file=text, end =', ')
  print(average_blue, file=text, end =', ')
  print(H, file=text, end =', ')
  print(S, file=text, end =', ')
  print(V, file=text, end =', ')  
  print(r, file=text, end =', ')
  print(rg, file=text, end =', ')  
  print(most_red, file=text, end =', ')
  print(least_red, file=text, end =', ')
  print(most_yellow, file=text)
text.close