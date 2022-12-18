#### KSW 2022 Fall Program
# 🍎 Predicting the sweetness of multiple apples by applying apple images on Hybrid Machine Learning: Machine Learning and Deep Learning    


## Team TopGun
    
| Name         |Call sign| University               | Department                                   | Email               | Github    |
| :-----------------:| :---------: | :------------------------: | :------------------------------------: | :-------------------: | :-------------------------: |
| Heejun Park |YODA   | Yeonsei Univ.| Computer and Telecommunications Engineering|parkie0517@gmail.com| https://github.com/parkie0517|
| Hanbi Kim |PHEONIX  | Chungbuk Nat'l Univ.   | Computer Science | hanbikim20@g.cbnu.ac.kr  | https://github.com/hanbikim    |
| Jeongho Ha |JAY | Jeju Nat'l Univ.       | Computer Engineering | hjh4212@naver.com| https://github.com/hjh1248    |
| Seokkhyeon Heo|EASY | Jeju Nat'l Univ.   | Blockchain Security |gj4535@gmail.com| https://github.com/gj1515   |
| Taeyun Kim |KAMTAE  | Jeju Nat'l Univ.  | Tourism Management & Big Data Science |persimm0ncrack@gmail.com| https://github.com/kamtae |
| Jeffrey Tsai| GOKU | Purdue Univ.  | Computer & Information Technology | jeffrey051622@gmail.com    ||
| Kyungrock Kwon| ROCK | Purdue Univ.  | Systems Analysis & Design |kyungrock99@gmail.com |  |

<br>

## Research problem statement
Farmers harvest apples without checking the sweetness level. They pick all apples and send them to Agricultural Products Processing Center (APC). Then a machine in APC measures their level. The problem is to harvest apples without knowing the Brix value, i.e., not checking whether it has commercial value. it is challenging for farmers to predict the optimal harvesting time based only on their experience. For consumers, it is difficult to select the best apples in terms of sugar level or sweetness.     

There are two universal ways to measure sugar levels: The destructive sugar levels measurement method (DM) and the Non-destructive sugar levels measurement method (NDM). DM measures sugar levels by testing the juice from cut fruits. It is a more affordable method than NDM. A disadvantage is that cut fruits lose their value to be sold. NDM displays sugar levels by detecting the reflected wavelength from the apples that were irradiated to near-infrared. It measures the sweetness of apples without damaging the fruits and shows the sugar levels immediately. However, the method is expensive, and the accuracy of the outputs is not stable. 

<br>

## Overview
<img src="https://user-images.githubusercontent.com/74577775/208288156-982ce322-40cf-445e-b77b-bc0fa2b04fef.png" width="1000" height="400"></img>


## Research novelty
    1. Develop a Hybrid Machine Learning (HML) model that combines ML and DL models.
    2. Predict apple sweetness(Brix level) from apple images taken by a smartphone.
    3. Detect multiple apples and provide appel sweetness(Brix level) of apples at once.

<br>

## How to run the project
#### Download the Dataset folder from google Drive

### Machine Learning
1. You can set the terminal path to '.../Machine_Learning/' and execute it.
### Deep Learning
1. Insert the Final_3Class_Effiv2_l file into the decompressed Dataset folder.
### HML

### Android
1. Run the Android application after running the server.


<br>

## Environment Setting
### Preprocessing
    - YOLO V4
### Machine Learning
    - Python 3.8.2
    - scikit-learn
### Deep Learning    
    - Python 3.8.16
    - Pytorch 1.13.0+cu116
    - EfficientNetV2-l
### Andriod Application
    - Gradle version 7.4
    - Android sdk 32
    - Glide 4.14.2
### Server
    - Flask okhttp 4.10.0


   
