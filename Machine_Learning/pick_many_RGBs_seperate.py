from PIL import Image
import numpy as np
import glob
import pandas as pd
import natsort
images = natsort.natsorted(glob.glob('./Machine_Learning/new_rembg_apples/*.png')) #폴더에 있는 파일들 숫자 순서대로 불러오기
text=open('./Machine_Learning/Apple_attribute_seperate.txt', 'w')
print("red, green, blue, r, rg, most_red, least_red, most_yellow, size", file=text) #특성
for fname in images:
  im = Image.open(fname)
  pix = np.array(im)
  c = np.arange(1,im.size[0],10)
  d = np.arange(1,im.size[1],10)
  red_sum = 0
  green_sum = 0
  blue_sum = 0
  least_red = 0
  most_yellow = 0
  most_red = 0
  count = 0
  for i in c:
    for j in d:
      if pix[j][i][0] > 1:
        red_sum = red_sum + pix[j][i][0]
        green_sum = green_sum + pix[j][i][1]
        blue_sum = blue_sum + pix[j][i][2]
        red = float(pix[j][i][0])
        green = float(pix[j][i][1])
        blue = float(pix[j][i][2])
        if red - green - blue > most_red:
          most_red = round(red - green - blue, 2)
        if red - green - blue < least_red:
          least_red = round(red - green - blue, 2)
        if red + green - blue > most_yellow:
          most_yellow = round(red + green - blue, 2)
        count = count + 1
  average_red = round(red_sum / count, 2)
  average_green = round(green_sum / count, 2)
  average_blue = round(blue_sum / count, 2)
  rg = round(average_red + average_green - average_blue, 2)
  r = round(average_red - average_green - average_blue, 2)
  print(average_red, file=text, end =', ')
  print(average_green, file=text, end =', ')
  print(average_blue, file=text, end =', ')
  print(r, file=text, end =', ')
  print(rg, file=text, end =', ')  
  print(most_red, file=text, end =', ')
  print(least_red, file=text, end =', ')
  print(most_yellow, file=text, end =', ')
  print(count, file=text,)
text.close